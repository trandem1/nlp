# def levenshteinDistance(s1, s2):
#     """
#     :param s1:la chuoi ki tu
#     :param s2:la chuoi ki tu
#     :return: khoang cach cua 2 chuoi dau vao
#     """
#     if len(s1) > len(s2):
#         s1, s2 = s2, s1
#     distances = range(len(s1) + 1)
#     for i2, c2 in enumerate(s2):
#         distances_ = [i2 + 1]
#         for i1, c1 in enumerate(s1):
#             if c1 == c2:
#                 distances_.append(distances[i1])
#             else:
#                 distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
#         distances = distances_
#     distac = 1 - distances[-1] / max(len(s1), len(s2))
#     return distac
#
#
#
# def dectectMyLogic(s1):
#     arr = s1.split()
#     s2 = ""
#     index = -1
#     for i in range(len(arr)):
#         if arr[i] == "học" and arr[i - 1] == "môn":
#             index = i
#         if arr[i] == "học" and arr[i - 1] == "lớp":
#             index = i
#         if arr[i] == "phần" and arr[i - 1] == "học":
#             index = i
#         if arr[i] == "lớp" and arr[i - 1] == "mã":
#             index = i
#     if index != -1:
#         for i in range(index + 1, len(arr)):
#             s2 += " " + arr[i]
#     return index, s2
#
# print(dectectMyLogic("tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học").__getitem__(0))
#
# """
# dung de sua loi chinh ta cho nguoi nhap vao
# vi du: ngôn ngữ tự niên -> ngôn ngữ tự nhiên.
# """
#
#
# def choseSenetence( s1):
#     tenHp = set()
#     import MySQLdb
#     con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
#                                        user="root",  # your username
#                                        passwd="anhdem96",  # your password
#                                        db="test_it4421",
#                                        charset='utf8')
#     query = con.cursor()
#     query.execute("SELECT monhoc FROM tenmonhoc;")
#     for row in query.fetchall() :
#         tenHp.add(row[0].lower())
#     con.close()
#     # tenHp = set(['xử lý ngôn ngữ tự nhiên', 'kĩ thuật hóa học', 'lập trình hướng đối tượng', 'lập trình c#',"tâm lý học"])
#     monhoc=""
#     kc = 0.0
#     for hp in tenHp:
#         temp = levenshteinDistance(hp, s1)
#         if temp > kc:
#             kc = temp
#             monhoc = hp
#     if kc >= 0.5:
#         return monhoc
#     else:
#         return 0
#
#
# """
# khi ham choseSentence khong the tra lai dc 1 ket qua hop ly,
# ta se thu sua các từ nằm trong môn học họ nhập vào để đưa ra đc 1 kết quả mới
# có thể dùng để chạy lại hàm choseSenten 1 lần nữa. trước khi ta nhận định
# nguời dùng đã quá sai chinh tả
# """
#
#
# def choseword( s1):
#     """
#     :param s1:
#     :return: 1 chuỗi đã được sử lý
#     ví dụ  xư lí ngôn tư niên -> xử lý ngôn tự nhiên
#     threshold sẽ là 0.5 cho từ có 2 kí tụ
#     threshold sẽ là 2/3 cho từ có 3 kí tụ trở lên
#     """
#     words = set()
#     import MySQLdb
#     con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
#                                        user="root",  # your username
#                                        passwd="anhdem96",  # your password
#                                        db="test_it4421",
#                                        charset='utf8')
#     query = con.cursor()
#     query.execute("SELECT vocab FROM vocabulary;")
#     for row in query.fetchall() :
#         words.add(row[0].lower())
#     con.close()
#     words1 = s1.split()
#     s2 = ""
#     for temp in words1:
#         if (len(temp) > 2):
#             for temp1 in words:
#                 kc = levenshteinDistance(temp, temp1)
#                 if kc >= 2 / 3:
#                     s2 += " " + temp1
#                     break
#         else:
#             for temp1 in words:
#                 kc = levenshteinDistance(temp, temp1)
#                 if kc >= 0.5:
#                     s2 += " " + temp1
#                     break
#     return s2
#
# testDectect ="xử lý ngôn ngữ tự niên, tam lý học, giai tich ii và dai so"
#
# def detecttenLop(s1) :
#     t = s1.split(',')
#     t1 = t[-1].split("và")
#     t.remove(t[-1])
#     if len(t1) > 1 :
#         for text in t1 :
#             t.append(text)
#     for i in range(len(t)):
#         t[i] = t[i].strip()
#     return t
#
# def fixtenlop(s1):
#     t = choseSenetence(s1)
#     if t == False:
#         t1 = choseword(s1)
#         t = choseSenetence(t1)
#     return t
# def processTenLop(s1):
#     t = detecttenLop(s1)
#     rs =[]
#     for text in t:
#         rs.append(fixtenlop(text.lower()))
#     return rs
# print(processTenLop(testDectect))
#
