"""muKeDjango URL Configuration

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
import django
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve

from django.views.generic import TemplateView
from .settings import MEDIA_ROOT

import xadmin
from users.views import LoginView,RegisterView,LogoutView,ActiveUserView,ForgetPwdView,ResetView,IndexView

urlpatterns = [
    #url(r'^xadmin/', xadmin.site.urls),
    path('xadmin/',xadmin.site.urls),
    path('', IndexView.as_view(), name=  "index"),
    #path('', TemplateView.as_view(template_name= "index.html"), name= "index"),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),

    # 验证码url
    path("captcha/", include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name= "user_active"),
    path('forget/', ForgetPwdView.as_view(), name= "forgetpwd"),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),


    path("org/", include('organization.urls', namespace='org')),
    re_path(r'media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    path("course/", include('course.urls', namespace='course')),
    path("users/", include('users.urls', namespace='users'))


]
