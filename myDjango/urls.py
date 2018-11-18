"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#include语法相当于多级路由，它把接收到的url地址去除前面的正则表达式，将剩下的字符串传递给下一级路由进行判断
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^myAPP/',include('myAPP.urls')),
    url(r'^admin/', admin.site.urls),
]
