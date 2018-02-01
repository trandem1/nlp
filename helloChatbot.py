# -*- coding: utf-8 -*-
from chatterbot import ChatBot


# Create a new instance of a ChatBot
chatbot = ChatBot(
    'mon hoc',

    logic_adapters=[
        'CourseLogic.myCourseLogic'
    ]
)

"""
tham khao code tren mang, thay code rat ngan
no se chay nhanh hon tam 3 lan code ben tren
"""
def levenshteinDistance(s1, s2):
    """
    :param s1:la chuoi ki tu
    :param s2:la chuoi ki tu
    :return: khoang cach cua 2 chuoi dau vao
    """
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    distac = 1- distances[-1]/max(len(s1),len(s2))
    return distac

"""
hàm này sử dụng để sửa lỗi chính tả đầu vào ví dụ max -> mã
"""
def changeWordBeforePre(s1):
    wordInit = set(["môn", "học", "phần", "lớp", "mã", "lịch,và"])
    max =0
    for text in wordInit :
        if len(text) == 2:
            t = levenshteinDistance(s1, text)
            if  t > 0.33 and t > max:
                max =t
                s1 = text
        else :
            t = levenshteinDistance(s1, text)
            if t > 0.4 and t >max:
                max =t
                s1 = text
    return s1
"""
sử dụng cả chuỗi input nhập vào 
tìm cho tôi mon hocj và  max lớp xử lý ngôn ngữ tự niên và tâm lý học 
-> tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học
"""

def changeInput(s1):
    arr = s1.split()
    s2 =""
    for t in arr :
        s2 += " " + changeWordBeforePre(t)
    return s2.strip()



# Get a response for some unexpected input
response = chatbot.get_response("tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học")

print(response)