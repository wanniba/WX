from wechat.xmlType.ImgMsg import ImgMsg
from wechat.xmlType.TextMsg import TextMsg


def normalreply(xmlData):
    print('进入普通请求')
    try:
        msg_type = xmlData.find('MsgType').text
        ToUserName = xmlData.find('ToUserName').text
        FromUserName = xmlData.find('FromUserName').text
        CreateTime = xmlData.find('CreateTime').text
        MsgId = xmlData.find('MsgId').text

        toUser = FromUserName
        fromUser = ToUserName
        if msg_type == 'text':
            Content = xmlData.find('Content').text
            if Content == '小可爱':

                mediaId = "irVyazYwpl0aW6EZB5j6M8PAelWEzmaFVBlEvdeYxeLsqYFOpvhUKkbZj3p7inwg"
                replyMsg = ImgMsg(toUser, fromUser, mediaId)
                print("成功了!!!!!!!!!!!!!!!!!!!")
                print(replyMsg.send())
                return replyMsg.send()
            else:
                print(Content.text)
                content = "发送小可爱试试"
                replyMsg = TextMsg(toUser, fromUser, content)

                return replyMsg.send()

        elif msg_type == 'image':
            content = "图片已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'voice':
            content = "语音已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'video':
            content = "视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'shortvideo':
            content = "小视频已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'location':
            content = "位置已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        elif msg_type == 'link':
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()
        else:
            content = "链接已收到,谢谢"
            replyMsg = TextMsg(toUser, fromUser, content)
            return replyMsg.send()


    except Exception as e:
        return e
