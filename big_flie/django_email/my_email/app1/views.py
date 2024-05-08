from django.shortcuts import render,HttpResponse


# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from . import email_day1
def send_email(request):
    substance = request.POST.get('substance')
    print(substance)
    username = request.POST.get('username')
    print(username)
    if substance =='' or username =='':
        return HttpResponse("参数不能为空")
    success = send_mail("重要去宾馆", substance, settings.EMAIL_HOST_USER, [username])
    email_day1.file_email(r"C:\Users\林显豪\Desktop\day1.jpg",'3113217659@qq.com')
    return HttpResponse("send email success")


def views_email(request):
    return render(request, "email.html")
