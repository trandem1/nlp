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

response = chatbot.get_response("tìm cho tao môn học it4421 , 21412, xử lý ngôn ngữ tự nhiên, tâm lý học")
#
print(response)


