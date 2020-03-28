import apiai


import json


def send_massage(message):
    request = apiai.ApiAI('enter your token from DialogFlow').text_request()
    request.lang = 'ru'
    request.session_id = 'session 1'
    request.query = message
    response = json.loads(request.getresponse().read())
    print(response['result']['fulfillment']['speech'])
    return response['result']['action']

print('Напишите сообщение или напишите выход')
message = input()
action = None
while True:
    action = send_massage(message)
    if action == 'asmalltalk.greetings.bye':
        break
    message = input()
