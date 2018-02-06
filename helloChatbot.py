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

# print( chatbot.get_response("tâm lý học , 102936.0 , bf2110"))
print(chatbot.get_response("xin lich mon hoc"))



