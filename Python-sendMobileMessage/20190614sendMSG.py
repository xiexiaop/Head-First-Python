from twilio.rest import Client

account_id = 'AC383c91bd31e19354ef47e644dddddde1'
auth_token = '19717d68ecb03e1f920aa63adc1491e8'
client = Client(account_id, auth_token)

# 开始发短信


def send_msg(message):
    message = client.messages.create(
        to='+8613521446300',
        from_='+12565703006',
        body=message
    )

# 开始打电话


def call_num(number):
    '自定义打电话的号码'
    call = client.calls.create(
        to=number,
        from_='+12565703006',
        url="http://demo.twilio.com/docs/voice.xml"
    )


if __name__ == '__main__':
    send_msg('伤心')
    # call_num('+8613521446300')
