# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import pprint

# Create a new instance of a ChatBot
chatbot = ChatBot(
    'mon hoc',

    logic_adapters=[
        'CourseLogic.myCourseLogic'
    ]
)


# Get a response for some unexpected input
response = chatbot.get_response('môn học')

pprint.pprint(response)