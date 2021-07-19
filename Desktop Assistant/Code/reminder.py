from twilio.rest import Client
def message(msg):
    a_sid="AC3d3213132e6d9272e4d6c9b8ef294f00"
    auth_token="f3a92422aed2fd68d1800cc167b29d63 "
    client = Client(a_sid,auth_token)
    message = client.messages.create(body=msg,from_=' whatsapp: +14155238886',to=' whatsapp: +916200527307 ')
    print('message had been sand ')


message('hello')