import json

from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_eamil
from django.urls import reverse

from .models import UserProfile,EmailVerifyRecord,Banner
from course.models import Course
from operation.models import UserCourse, UserFavorite, UserMessage
from organization.models import CourseOrg, Teacher
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm,ActiveForm,ForgetForm,ModifyPwdForm



# 实现用户名邮箱均可登录
# 继承ModelBackend类，自定义authenticate方法
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None

# 用户登录
class LoginView(View):
    def get(self, request):
        redirect_url = request.GET.get('next', '')
        return render(request, "login.html", {
            "redirect_url": redirect_url
        })

    def post(self, request):


        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")

            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    redirect_url = request.POST.get('next', '')
                    if redirect_url:
                        return HttpResponseRedirect(redirect_url)
                    return HttpResponseRedirect(reverse("index"))
                else:
                    return render(
                        request, "login.html", {
                            "msg": "用户名未激活! 请前往邮箱进行激活"})
            else:
                return render(request, "login.html", {"msg": "用户名或密码错误!"})
        else:
            return render(
                request, "login.html", {
                    "login_form": login_form})

# 退出
class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse("index"))


# 用户注册

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request,'register.html',{'register_form':register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email','')
            if UserProfile.objects.filter(email=user_name):
                return render(
                    request, "register.html", {
                        "register_form": register_form, "msg": "用户已存在"})
            pass_word = request.POST.get('password','')

            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False

            user_profile.password = make_password(pass_word)
            user_profile.save()

            user_message = UserMessage()
            user_message.user = user_profile.id
            user_message.message = "欢迎注册慕课网!! --系统自动消息"
            user_message.save()

            send_register_eamil(user_name, "register")

            return render(request,"login.html",{})
        else:
            return render(request,"register.html",{
                "register_form":register_form
            })

# 激活用户
class ActiveUserView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code = active_code)
        active_form = ActiveForm(request.GET)
        if all_record:
            for record in all_record:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()

                return render(request, "login.html", )
        else:
            return render(request, "register.html", {"msg": "您的激活链接无效", "active_form": active_form})


# 忘记密码

class ForgetPwdView(View):

    def get(self, request):
        active_form = ActiveForm(request.POST)
        return render(request, "forgetpwd.html", {"active_form": active_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get("email", "")

            send_register_eamil(email, "forget")
            return render(request, "login.html", {"msg": "重置密码邮件已发送,请注意查收"})
        else:
            return render(
                request, "forgetpwd.html", {
                    "forget_from": forget_form})


# 重置密码的view
class ResetView(View):
    def get(self, request, active_code):
        all_record = EmailVerifyRecord.objects.filter(code=active_code)
        active_form = ActiveForm(request.GET)
        if all_record:
            for record in all_record:
                email = record.email
                return render(request, "password_reset.html", {"email":email})
        # 自己瞎输的验证码
        else:
            return render(
                request, "forgetpwd.html", {
                    "msg": "您的重置密码链接无效,请重新请求", "active_form": active_form})

# 改变密码的view


class ModifyPwdView(View):
    def post(self, request):
        modiypwd_form = ModifyPwdForm(request.POST)
        if modiypwd_form.is_valid():
            pwd1 = request.POST.get("password1", "")
            pwd2 = request.POST.get("password2", "")
            active_code = request.POST.get("active_code", "")
            email = request.POST.get("email", "")
            # 如果两次密码不相等，返回错误信息
            if pwd1 != pwd2:
                return render(
                    request, "password_reset.html", {
                        "email": email, "msg": "密码不一致"})
            # 如果密码一致
            # 找到激活码对应的邮箱
            all_record = EmailVerifyRecord.objects.filter(code=active_code)
            for record in all_record:
                email = record.email
            user = UserProfile.objects.get(email=email)
            # 加密成密文
            user.password = make_password(pwd2)
            # save保存到数据库
            user.save()
            return render(request, "login.html", {"msg": "密码修改成功，请登录"})
        # 验证失败说明密码位数不够。
        else:
            email = request.POST.get("email", "")
            return render(
                request, "password_reset.html", {
                    "email": email, "modiypwd_form": modiypwd_form})

