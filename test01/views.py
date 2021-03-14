from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
#from views.handle import Handle

from werobot import WeRoBot
robot=WeRoBot(enable_session=False,
                token='qidong123',
                APP_ID='wxbdffa8b28352f100',
                APP_SECRET='591bfdbc7c387a0f34a46730664c806c')

# Create your views here.
def index(request):
    print(111)
    """主页"""
    return render(request,'index.html')

def handle_wx(request):
    if request.method == 'GET':
        try:
            signature = request.GET.get('signature', '')
            timestamp = request.GET.get('timestamp', '')
            nonce = request.GET.get('nonce', '')
            echostr = request.GET.get('echostr', '')

            token = "qidong123" #请按照公众平台官网\基本配置中信息填写

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(list[0].encode("utf-8"))
            sha1.update(list[1].encode("utf-8"))
            sha1.update(list[2].encode("utf-8"))

            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                print("验证成功")
                return HttpResponse(echostr)
            else:
                return HttpResponse("")
        except Exception as e:
            return HttpResponse(e)


@robot.handler
def hello(message):
    return 'Hello world'
