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
            # Zac个人微信公众号
            "appid": "wx1bc7a9091ef8b5d5",
            "secret": "2e822d37038d323f00b15d995f8a0da0",

            # # # 公司付费微信公众号
            # "appid": "wxdfa7b347df1b265c",
            # "secret": "3d4f4eca67fe3238ac08c21a213ae905",
        }
    ).json()

    if result.get("access_token"):
        access_token = result.get('access_token')
    else:
        access_token = None
    return access_token


def sendmsg(openid, msg):

    access_token = get_access_token()

# # ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
# # 测试发送消息内容
#     body = {
#         "touser": openid,
#         "msgtype": "text",
#         "text": {
#             "content": msg
#         }
#     }

#     response = requests.post(
#         url="https://api.weixin.qq.com/cgi-bin/message/custom/send",
#         params={
#             'access_token': access_token
#         },
#         data=bytes(json.dumps(body, ensure_ascii=False), encoding='utf-8')
#     )
# # ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
    # 发送消息模版
    # data = {
    #     "touser": openid,
    #     "template_id": 'Jh0VlTjCerWnqHi46llE7gIKg-8Z1sV9yqOVbXCimok',
    #     # "page": ' ‘,
    #     # "form_id": ' ',
    #     # "data": {
    #     #     'keyword1': {
    #     #         'value': 'value1'
    #     #     }
    #     # },
    #     # "emphasis_keyword": '电饭锅回家'
    # }

    data = {
        "touser": openid,
        "template_id": "Jh0VlTjCerWnqHi46llE7gIKg-8Z1sV9yqOVbXCimok",  # 模板ID
        # "miniprogram":{
        #   "appid":"wx67afc56d7f6cfac0",  #待使用上线小程序appid
        #   "path":"pages/reserve/mgr/mgr"
        # },
        "data": {
            "PARA1": {
                "value": "参数1内容",
                "color": "#173177"
            },
            "PARA2": {
                "value": "参数2内容",
                "color": "#173177"
            },
            "PARA3": {
                "value": "参数3内容",
                "color": "#173177"
            },
            "PARA4": {
                "value": "参数4内容",
                "color": "#173177"
            }
        }
    }

    json_template = json.dumps(data)

    response = requests.post(
        url="https://api.weixin.qq.com/cgi-bin/message/template/send",
        params={
            'access_token': access_token
        },
        data=json_template
    )
# ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊

# 这里可根据回执code进行判定是否发送成功(也可以根据code根据错误信息)
    result = response.json()
    print(result)


if __name__ == '__main__':
    # sendmsg('personality19900901', '发送消息内容')
    # sendmsg('oJ-t35NgoS2pOgL8QN-8Q1Wr8OmY', '发送消息内容')／／公司OpenID
    # ／／个人账号－谢Zac
    sendmsg('oeApP1GbWjUFiDkz5_fpCG76XyhA', '测试发送非模版消息内容')
    # ／／个人账号－赵梓良
    # sendmsg('oeApP1Lo6s5nJ5ZhP6W0F0OEcoBM', '测试发送非模版消息内容')
