import requests as req

'''
Facebook Messenger client
'''
class Messenger:

    send_msg_url = 'https://graph.facebook.com/v2.6/me/messages?access_token='

    def __init__(self, access_token):
        self.access_token = access_token

    def send(self, recipient, message, notif_type='REGULAR'):
        json = {'recipient': recipient, 'message': message, 'notification_type': notif_type}
        response = req.request('POST', send_msg_url + self.access_token, json = json)
        return response

    def receive(self):
        pass
