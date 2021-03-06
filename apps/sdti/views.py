from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import xml.etree.cElementTree as ET
import hashlib
import time
import os


def log(text):  # 记录装饰器
    def decorator(function):
        def wrapper(*args, **kwargs):
            print('Pid:%s running %s [function:%s] at %s' % (
            os.getpid(), text, function.__name__, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
            return function(*args, **kwargs)

        return wrapper

    return decorator


def CheckSign(requests):
    os.getpid()
    form = {}
    form['signature'] = requests.GET.get('signature', None)
    form['timestamp'] = requests.GET.get('timestamp', None)
    form['nonce'] = requests.GET.get('nonce', None)
    form['token'] = settings.TOKEN
    Signature = form.pop('signature')
    Key = hashlib.sha1("".join(sorted([form[i] for i in form])).encode('utf-8')).hexdigest()  # 获得sha1加密后结果
    return True if Signature == Key else False


XMLtemplate = '<xml> <ToUserName>< ![CDATA[%s] ]></ToUserName> <FromUserName>< ![CDATA[%s] ]></FromUserName> <CreateTime>%s</CreateTime> <MsgType>< ![CDATA[%s] ]\
        ></MsgType> <Content>< ![CDATA[%s] ]></Content> </xml>'


def CreateXML(**kwds):  # 生成返回消息的XML
    return (XMLtemplate % (
    kwds['ToUserName'], kwds['FromUserName'], kwds['CreateTime'], kwds['MsgType'], kwds['Content'])).replace(' ', '')


@csrf_exempt
def checkwx(requests):  # URL路由入口
    if requests.method == "GET":
        EchoStr = requests.GET.get('echostr', None)  # 获取回应字符串
        return HttpResponse(EchoStr) if CheckSign(requests) else HttpResponse('vaild signature')
    elif requests.method == "POST":
        if CheckSign(requests) == False:
            print('check not pass')
            return None
        Res = autorely(requests).encode('utf-8')
        return HttpResponse(Res, content_type="text/xml")
    else:
        return HttpResponse('invaild requests')


# 预留处理接口
# 推荐直接返回XML
def DealTextMsg(*args, **kwds):  # 处理文本信息
    return '欢迎来到丰盛安防'


def DealImageMsg(*args, **kwds):  # 处理图片信息
    pass


def DealVoiceMsg(*args, **kwds):  # 处理声音信息
    pass


def DealVideoMsg(*args, **kwds):  # 处理视频信息
    pass


def DealShortVideoMsg(*args, **kwds):  # 处理短视频信息
    pass


def autorely(requests):
    webData = requests.body
    Root = ET.fromstring(webData)
    ToUserName = Root.find('ToUserName').text
    FromUserName = Root.find('FromUserName').text
    CreateTime = Root.find('CreateTime').text
    MsgType = Root.find('MsgType').text
    MsgId = Root.find('MsgId').text
    if MsgType == 'text':
        Content = Root.find('Content').text
        Content1 = DealTextMsg(Content)
        return CreateXML(ToUserName=requests.GET['openid'], FromUserName=ToUserName, CreateTime=int(time.time()),
                         MsgType='text', Content=Content1)
    elif MsgType == 'image':
        ResourceUrl = Root.find('PicUrl').text
        DealImageMsg()
        return CreateXML(ToUserName=requests.GET['openid'], FromUserName=ToUserName, CreateTime=int(time.time()),
                         MsgType='text', Content='图片已经接收\nUrl:%s' % ResourceUrl)
    elif MsgType == 'voice':
        DealVoiceMsg()
        return CreateXML(ToUserName=requests.GET['openid'], FromUserName=ToUserName, CreateTime=int(time.time()),
                         MsgType='text', Content='语音已接收到')
    elif MsgType == 'video':
        DealVideoMsg()
        return CreateXML(ToUserName=requests.GET['openid'], FromUserName=ToUserName, CreateTime=int(time.time()),
                         MsgType='text', Content='视频已接收到')
    elif MsgType == 'shortvideo':
        DealShortVideoMsg()
        return CreateXML(ToUserName=requests.GET['openid'], FromUserName=ToUserName, CreateTime=int(time.time()),
                         MsgType='text', Content='小视频已接收到')
    else:
        return CreateXML(ToUserName=requests.GET['openid'], FromUserName=ToUserName, CreateTime=int(time.time()),
                         MsgType='text', Content='不支持该数据类型')