from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse, Http404

def home(request):
    return render(request, 'home.html')

def regist(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user.pk:
            return render(request, 'regist.html', {'error': '用户名已经存在!'})
        else:
            User.objects.create_user(username=username,password=password)
            return HttpResponse("<p>create succeed</p>")
    return render(request, 'regist.html')

def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # 保存登录会话,将登陆的信息封装到request.user,包括session
            return redirect("/index")
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误!'})
    return render(request, 'login.html')

@login_required
def my_logout(request):
    """
    :param request
    :return: 退出并重定向到登录页面
    """
    logout(request)
    return redirect("/login/")


@login_required
def index(request):
    return render(request, "index.html")

@login_required
def insert_data(request):
    # 需要全部字段来插入一条数据
    if request.method == 'POST':
        title = request.POST["title"]
        price = request.POST["price"]
        publish = request.POST["publish"]
        models.Book.objects.create(title=title, price=price, publish=publish)
        return render(request, 'insert.html', {'message':'insert successfully'})
    return render(request, 'insert.html')

@login_required
def delete_data(request):
    # 依据条件判断
    if request.method == 'POST':
        title = request.POST["title"]
        
        price = request.POST["price"]
        
        publish = request.POST["publish"]
        
        if (title == '' and price == '' and publish == ''):
            return render(request, 'delete.html')
        else:
            if title == '' and price == '':
                models.Book.objects.filter(publish=publish).delete()  
            elif title == '' and publish == '':
                models.Book.objects.filter(price=price).delete()
            elif price == '' and publish == '':
                models.Book.objects.filter(title=title).delete()
            elif title == '' and price != '' and publish != '':
                models.Book.objects.filter(price=price, publish=publish).delete()
            elif price == '' and title != '' and publish != '':
                models.Book.objects.filter(title=title, publish=publish).delete()
            elif publish == '' and price != '' and title != '':
                models.Book.objects.filter(title=title, price=price).delete()
            else:
                models.Book.objects.filter(title=title, price=price, publish=publish).delete()
        return render(request, 'delete.html', {'message':'delete successfully'})
    return render(request, 'delete.html')

@login_required
def update_data(request):
    if request.method == 'POST':
        title = request.POST["title"]
        price = request.POST["price"]
        publish = request.POST["publish"]
        
        updatetitle = request.POST["updatetitle"]
        updateprice = request.POST["updateprice"]
        updatepublish = request.POST["updatepublish"]

        if (title == '' and price == '' and publish == ''):
            return render(request, 'update.html')
        else:
            if title == '' and price == '':
                target_books = models.Book.objects.filter(publish=publish)  
            elif title == '' and publish == '':
                target_books = models.Book.objects.filter(price=price)
            elif price == '' and publish == '':
                target_books = models.Book.objects.filter(title=title)
            elif title == '' and price != '' and publish != '':
                target_books = models.Book.objects.filter(price=price, publish=publish)
            elif price == '' and title != '' and publish != '':
                target_books = models.Book.objects.filter(title=title, publish=publish)
            elif publish == '' and price != '' and title != '':
                target_books = models.Book.objects.filter(title=title, price=price)
            else:
                target_books = models.Book.objects.filter(title=title, price=price, publish=publish)
        
        if (updatetitle == '' and updateprice == '' and updatepublish == ''):
            return render(request, 'update.html')
        else:
            if updatetitle == '' and updateprice == '':
                target_books.update(publish=updatepublish) 
            elif updatetitle == '' and updatepublish == '':
                target_books.update(price=updateprice)
            elif updateprice == '' and updatepublish == '':
                target_books.update(title=updatetitle)
            elif updatetitle == '' and updateprice != '' and updatepublish != '':
                target_books.update(price=updateprice, publish=updatepublish)
            elif updateprice == '' and updatetitle != '' and updatepublish != '':
                target_books.update(title=updatetitle, publish=updatepublish)
            elif updatepublish == '' and updateprice != '' and updatetitle != '':
                target_books.update(title=updatetitle, price=updateprice)
            else:
                target_books.update(title=updatetitle, price=updateprice, publish=updatepublish)
        return render(request, 'update.html', {'message':'update successfully'})
    return render(request, 'update.html')

@login_required
def query_data(request):
    if request.method == 'POST':
        title = request.POST["title"]
        price = request.POST["price"]
        publish = request.POST["publish"]

        if (title == '' and price == '' and publish == ''):
            return render(request, 'select.html')
        else:
            if title == '' and price == '':
                target_books = models.Book.objects.filter(publish=publish)  
            elif title == '' and publish == '':
                target_books = models.Book.objects.filter(price=price)
            elif price == '' and publish == '':
                target_books = models.Book.objects.filter(title=title)
            elif title == '' and price != '' and publish != '':
                target_books = models.Book.objects.filter(price=price, publish=publish)
            elif price == '' and title != '' and publish != '':
                target_books = models.Book.objects.filter(title=title, publish=publish)
            elif publish == '' and price != '' and title != '':
                target_books = models.Book.objects.filter(title=title, price=price)
            else:
                target_books = models.Book.objects.filter(title=title, price=price, publish=publish)
            book_list = [i.title for i in target_books]
            return render(request, 'select.html', {'book_list':book_list})
    return render(request, 'select.html')

@login_required
def download_small_file(request):
    file_path = "/project/resource/small.jpg"
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=small.jpg"
        return r
    except Exception:
        raise Http404("Download error")

@login_required
def download_big_file(request):
    file_path = "/project/resource/big.jpg"
    try:
        r = StreamingHttpResponse(open(file_path, "rb"))
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=big.jpg"
        return r
    except Exception:
        raise Http404("Download error")

@login_required
def download_page(request):
    return render(request, 'download.html')

@login_required
def upload_file(request):
    if request.method == 'POST':
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse("No upload file needed")
        else:
            with open("/project/upload/%s" % File.name, 'wb+') as f:
                for chunk in File.chunks():
                    f.write(chunk)
            return render(request, 'upload.html', {'message':'upload successfully'})
    return render(request, 'upload.html')

def createSingleUser(request):
    User.objects.create_user(username='fortest',password='123')
    return HttpResponse("<p>create succeed</p>")

def createMutipleUser(request):
    for i in range(0,100):
        User.objects.create_user(username="tester" + str(i),password='123')
    return HttpResponse("<p>create 100 user succeed</p>")

def insertSingleBook(request):
    models.Book.objects.create(title="Book", price=22, publish="publisher1")
    return HttpResponse("<p>insert succeed</p>")

def insertMultipleBook(request):
    for i in range(0,10000):
        models.Book.objects.create(title="Book" + str(i), price=100 + i, publish="publisher1")
    for i in range(0,10000):
        models.Book.objects.create(title="Book" + str(10000 + i), price=100 + i, publish="publisher2")
    for i in range(0,10000):
        models.Book.objects.create(title="Book" + str(20000 + i), price=100 + i, publish="publisher3")
    return HttpResponse("<p>insert multi data succeed</p>")