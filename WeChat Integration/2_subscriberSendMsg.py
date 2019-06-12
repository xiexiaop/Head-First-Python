# pip3 install requests
import requests
import json


def get_access_token():
    """
    获取微信全局接口的凭证(默认有效期俩个小时)
    如果不每天请求次数过多, 通过设置缓存即可
    """
    result = requests.get(
        url="https://api.weixin.qq.com/cgi-bin/token",
        params={
            "grant_type": "client_credential",
            # # Zac个人微信公众号
            # "appid": "wx3a026a0fbe15d5cb",
            # "secret": "90fe03cc0d1680ef21dcae12f4d0b762",

            # # 公司付费微信公众号
            "appid": "wxdfa7b347df1b265c",
            "secret": "3d4f4eca67fe3238ac08c21a213ae905",
        }
    ).json()

    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token


def sendmsg(openid, msg):

    access_token = get_access_token()

    body = {
        "touser": openid,
        "msgtype": "text",
        "text": {
            "content": msg
        }
    }

    # 发送消息模版
    # data = {
    #     "touser": 'openid',
    #     "template_id": 'template_id',
    #     "page": 'pages/index/index',
    #     "form_id": 'aaa',
    #     "data": {
    #         'keyword1': {
    #             'value': 'value1'
    #         }
    #     },
    #     "emphasis_keyword": ''
    # }

    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
        params={
            'access_token': access_token
        },
        data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
        # data=data

    )
    # 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)


if __name__ == '__main__':
    # sendmsg('personality19900901', '发送消息内容')
    sendmsg('oJ-t35NgoS2pOgL8QN-8Q1Wr8OmY', '发送消息内容')
