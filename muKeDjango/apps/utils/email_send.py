from random import Random

from  users.models import EmailVerifyRecord
# 导入Django自带的邮件模块
from django.core.mail import send_mail,EmailMessage
# 导入setting中发送邮件的配置
from muKeDjango.settings import EMAIL_FROM
# 发送html格式的邮件:
from django.template import loader


# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str


# 发送注册邮件
def send_register_eamil(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 定义邮件内容:
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕课"
        email_body = loader.render_to_string(
                "email_register.html",  # 需要渲染的html模板
                {
                    "active_code": code  # 参数
                }
            )

        msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
        msg.content_subtype = "html"
        send_status = msg.send()

        # 如果发送成功
        if send_status:
                pass
    elif send_type == "forget":
        email_title = "慕课网 找回密码链接"
        email_body = loader.render_to_string(
            "email_forget.html",  # 需要渲染的html模板
            {
                "active_code": code  # 参数
            }
        )
        msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
        msg.content_subtype = "html"
        send_status = msg.send()
    elif send_type == "update_email":
        email_title = "慕课网 修改邮箱验证码"
        email_body = loader.render_to_string(
            "email_update_email.html",  # 需要渲染的html模板
            {
                "active_code": code  # 参数
            }
        )
        msg = EmailMessage(email_title, email_body, EMAIL_FROM, [email])
        msg.content_subtype = "html"
        send_status = msg.send()