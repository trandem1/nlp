

testDectect ="tìm cho tôi môn học và lớp học xử lý ngôn ngữ tự niên và tâm lý học"

arr = testDectect.split()

for i in range(len(arr)):
    if arr[i] == "học" and arr[i-1] == "môn":
        index =i
    if arr[i] == "học" and arr[i-1] == "lớp":
        index = i
    if arr[i] == "phần" and arr[i-1] == "học":
        index = i
print(index)


# print(testDectect.split())
# def subString(s1):
#     arr = s1.split()
#     for i in range(len(arr)):
#         if detectmaHp(arr[i]):
#             break
#         if detectMlop(arr[])
#
#
#
# def detectmaHp(s1):
#     import re
#     t = re.findall(r"[a-zA-Z]{2,3}[0-9]{4}[a-zA-Z]?", s1)
#     if len(t) == 0:
#         return False
#     else:
#         return t
#     return 1
#
# def detectMlop(s1):
#     import re
#     t = re.findall(r"[0-9]{5,6}",s1)
#     if len(t) == 0:
#         return False
#     else:
#         return t


# def replacedau(s1):
#     import re
#     t = re.sub(r"[,]"," ",s1)
#     print(t)
#     return t
# print(detectmaHp(testDectect))
# print(detectMlop(testDectect))
# print(replacedau(testDectect))
#
# if "môn" in testDectect.split():
#     print("ok")