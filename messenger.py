from flask import Flask, request
import requests as req
from json import loads as parsejson

'''
Facebook Messenger client
'''
class Messenger:

    send_urlbase = 'https://graph.facebook.com/v2.6/me/messages?access_token='

    def __init__(self, access_token):
        self.access_token = access_token

    def send(self, recipient, message, notif_type='REGULAR'):
        json = {'recipient': recipient, 'message': message, 'notification_type': notif_type}
        response = req.request('POST', send_urlbase + self.access_token, json = json)
        return response

    def receive(self, message):
        pass

webhook = Flask(__name__)

m = Messenger('CAAIssfqefiEBADsr33gZBIxxg2rUHjkVr105lR5dLiNv82spmZAZCikvcfEumsDv09TGZCmkNdLyZAU3rkSTSWMZADHwNn1ZAUdqDZARH6VNL3TwiGKORs9kaA36DS5Ug3gURYiZC9XinMQlWe7H71rZBomgrgQmXKT9UjIxgOTJwIuipxvEve6iZByKiQnrAGSyDARfvzCTkpe6QZDZD')

@webhook.route('/', methods=['POST'])
def callback():
    text = request.data
    json = parsejson(text)
    messages = []
    for entry in json['entry']:
        for msg in entry['messaging']:
            m.receive(msg)
    return "Yo"

@webhook.route('/', methods=['GET'])
def verify():
    return request.args.get('hub.challenge')

if __name__ == "__main__":
    webhook.run(host = 'lifebot-webhook.herokuapp.com', port = 80)
