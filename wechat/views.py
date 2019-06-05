import hashlib

from django.http import HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from wechat.replay.autoreply import autoreply


@csrf_exempt
def weixin_main(request):


    if request.method == "GET":
        #接收微信服务器get请求发过来的参数
        signature = request.GET.get('signature', str)
        timestamp = request.GET.get('timestamp', str)
        nonce = request.GET.get('nonce', str)
        echostr = request.GET.get('echostr', str)
        #服务器配置中的token
        token = 'spq123456'
        #把参数放到list中排序后合成一个字符串，再用sha1加密得到新的字符串与微信发来的signature对比，如果相同就返回echostr给服务器，校验通过
        hashlist = [token, timestamp, nonce]
        print(type(token))
        print(type(timestamp))
        print(type(nonce))
        hashlist.sort()
        hashstr = ''.join([s for s in hashlist])
        print(hashstr)
        hashstr.encode('utf-8')
        print(hashstr)
        sha1 = hashlib.sha1()
        sha1.update(hashstr.encode('utf-8'))
        # md5 = hashlib.md5()  # 应用MD5算法
        # data = "hello world"
        # md5.update(data.encode('utf-8'))
        # print(md5.hexdigest()
        hashstr = sha1.hexdigest()
        if hashstr == signature:
            print('验证成功')
            return HttpResponse(echostr)
        else:
            return HttpResponse("field")
    else:

        print(bytes.decode(request.body, encoding='utf-8'))
        # return  HttpResponse("field")
        reply = autoreply(request)

        return HttpResponse(reply)




#
@csrf_exempt
def favicon(request):
    return HttpResponse("favicon-20190302023358386")
