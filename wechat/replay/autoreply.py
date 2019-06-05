#微信服务器推送消息是xml的，根据利用ElementTree来解析出的不同xml内容返回不同的回复信息，就实现了基本的自动回复功能了，也可以按照需求用其他的XML解析方法
import xml.etree.ElementTree as ET

from wechat.replay.eventreply import eventreply
from wechat.replay.normalreply import normalreply
from wechat.xmlType.TextMsg import TextMsg


def autoreply(request):
    try:
        print('进入自动回复')
        webData = bytes.decode(request.body, encoding='utf-8')

        xmlData = ET.fromstring(webData)

        msg_type = xmlData.find('MsgType').text

        if msg_type == 'event':
            return eventreply(xmlData)
        else:
            return normalreply(xmlData)


    except Exception as e:
        return e




