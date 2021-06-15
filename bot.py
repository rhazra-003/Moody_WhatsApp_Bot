from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time. Sorry!'
        msg.body(quote)
        responded = True
    
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    #if not responded:
    #    msg.body('I only know about famous quotes, cute cats and dogs. Sorry!')
    
    if 'dog' in incoming_msg:
        # return a dog pic
        msg.media('https://images.dog.ceo/breeds/frise-bichon/7.jpg')
        responded = True
    #if not responded:
    #    msg.body('I only know about famous quotes, cute cats and dogs. Sorry!')
    
    if 'hello' in incoming_msg:
        msg.body('Hello! I am Moody! I know about famous quotes, cute cats and dogs. What do you want to see?')
    
    if 'hi' in incoming_msg:
        msg.body('Hello! I am Moody! I know about famous quotes, cute cats and dogs. What do you want to see?')
    
    return str(resp)


if __name__ == '__main__':
    app.run()