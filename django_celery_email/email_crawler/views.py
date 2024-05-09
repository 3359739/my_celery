from django.shortcuts import render,HttpResponse
from .tasks import baidu
# Create your views here.
def test(request):
    print(baidu.delay())
    return HttpResponse("test测试")