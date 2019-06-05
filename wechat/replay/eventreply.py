from wechat.xmlType.TextMsg import TextMsg


def eventreply(xmlData):
    print('进入事件请求')
    try:
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        Event = xmlData.find('Event').text

        toUser = FromUserName
        fromUser = ToUserName

        if Event == 'CLICK':
            EventKey = xmlData.find('EventKey').text
            print(EventKey)
            if EventKey == 'V1001_TODAY_MUSIC':
                content = "发送小可爱试试"
                replyMsg = TextMsg(toUser, fromUser, content)

                return replyMsg.send()


    except Exception as e:
        return e
