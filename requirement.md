# requirement

- 登录：
  - 前台校验
    - 必填项是否填充
  - 后台校验
    - 用户名密码是否正确匹配数据库user表中的内容
- 页面1
  - 插入数据按钮
    - 实现单条数据的插入功能
  - input输入框
    - 插入条件
- 页面2
  - 删除数据按钮
    - 实现单条数据的删除功能
  - input输入框
    - 删除条件
- 页面3
  - 更新数据按钮
    - 实现数据的更新功能
  - input输入框
    - 更新条件
- 页面4
  - 查询数据按钮
    - 实现数据的查询功能
  - input输入框
    - 查询条件
- 页面5
  - 下载按钮
    - 实现服务器上一个较大文件的下载功能
- 页面6
  - 上传按钮
    - 实现上传一个较大文件到服务器的功能

## todo

- 在服务器 /project/resource 下准备一个大文件一个小文件 -- check
- 将views中关于download 的两个方法的filepath替换成上述的路径 -- check
- upload路径改成 /project/upload -- check
- 项目部署到服务器上
  - 安装依赖包 -- check
  - 安装uwsgi -- check
  - 配置uwsgi -- check
  - 匹配nginx -- check
  - 上线 -- check
- 写测试代码

## add for jenkins test
