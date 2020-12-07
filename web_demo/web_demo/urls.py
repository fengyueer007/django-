"""web_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('helloworld.urls'))

]
# http://itheihei.com/order/index
# http://itheihei.com/index


'''
有多个项目 老的1.x  新的2.x
区分一些 package 版本
1. 每个项目创建一个python 虚拟环境 mkvirtualenv -p python  h1 虚拟环境名称
2. workon h1    下载对应项目的 第三方框架 Django  
3. 创建项目  django-admin startproject s1 项目名
4. 创建项目中的子项目或子模块  django-admin startapp a1 模块名
5. 在项目中  先运行一下manage.py    修改启动项目配置文件  runserver
6. 在主模块的settings.py中配置  将子模块的配置到  INSTALLED_APPS 中a1.apps.A1Config
7. 子模块中views.py 编写代码 返回用户请求想要的数据
8. 在子模块中 新建urls.py文件  将子文件中方法与 具体接口名 对应上
9. 主urls.py中 导入子模块中的urls文件  为了访问具体的接口  path('order/', include('helloworld.urls'))
'''