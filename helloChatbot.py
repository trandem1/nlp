# -*- coding: utf-8 -*-
from chatterbot import ChatBot

# Create a new instance of a ChatBot
chatbot = ChatBot(
    'mon hoc',

    logic_adapters=[
        'CourseLogic.myCourseLogic'
    ]
)

# Get a response for some unexpected input



while True:
    print("nhap cai gi ban muon di nao")
    x = input()
    response = chatbot.get_response(x)

    print(response)




