# import MySQLdb
# con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
#                                    user="root",  # your username
#                                    passwd="anhdem96",  # your password
#                                    db="test_it4421",
#                                    charset='utf8')
# query = con.cursor();
# query.execute("SELECT distinct(ten_hp) FROM test_it4421.tkb;")
# for row in query.fetchall():
#     print(row[0])
#     query1 = con.cursor()
#     query1.execute("insert into tenmonhoc(monhoc) values ( '" + row[0] +"');")

# print(query.rowcount)
# for row in query.fetchall():
#     print(row[0])
#
# testRe = "anh học các học phần TEX5103 , TE5060 , TE4650,SSH1110,MI5113,IT5030E,IT5021E,TEX5103"
# import re
# t = re.finditer(r"[a-zA-Z]{2,3}[0-9]{4}[a-zA-Z]?",testRe)
# for x in t:
#     print(x)
# rs = re.findall(r"[a-zA-Z]{2,3}[0-9]{4}[a-zA-Z]?",testRe)
#
# """
# code nhung chua toi uu, don thuan doc thuat toan de code
# import time
# t = time.time()
# Distance('dva','dave')
# te=time.time()-t
# t2= time.time()
# levenshteinDistance('dva','dave')
# te1 = time.time()-t2
# print(te/te1)
# # print(t)
# """
# def distance(s1,s2):
#     nStt = [0 for i in range(len(s1)+1)]
#     for x in range(len(nStt)):
#         nStt[x] =[0 for i in range(len(s2) +1)]
#     for x in range(len(s2)+1):
#         nStt[0][x] =x
#     for x in range(len(s1)+1):
#         nStt[x][0] =x
#     for i in range(len(s1)):
#         for j in range(len(s2)):
#             if s1[i]==s2[j] :
#                 nStt[i+1][j+1] = nStt[i][j]
#             else:
#                 nStt[i+1][j+1] = 1 + min(nStt[i][j],nStt[i][j+1],nStt[i+1][j])
#     distac = 1 - nStt[len(s1)][len(s2)] / max(len(s1),len(s2))
#     return distac
#
# """
# tham khao code tren mang, thay code rat ngan
# no se chay nhanh hon tam 3 lan code ben tren
# """
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
#
# """
# dung de sua loi chinh ta cho nguoi nhap vao
# vi du: ngôn ngữ tự niên -> ngôn ngữ tự nhiên.
# """
#
# def choseSenetence (s1):
#     tenHp = set(['xử lý ngôn ngữ tự nhiên', 'kĩ thuật hóa học','lập trình hướng đối tượng','lập trình c#'])
#     kc = 0
#     for hp in tenHp :
#         temp =levenshteinDistance(hp,s1)
#         if  temp > kc :
#             kc = temp
#             monhoc= hp
#         if kc > 0.6 :
#             break
#     if kc > 0.6 :
#         return monhoc
#     else :
#         return 0
# """
# khi ham choseSentence khong the tra lai dc 1 ket qua hop ly,
# ta se thu sua các từ nằm trong môn học họ nhập vào để đưa ra đc 1 kết quả mới
# có thể dùng để chạy lại hàm choseSenten 1 lần nữa. trước khi ta nhận định
# nguời dùng đã quá sai chinh tả
# """
#
# def choseword(s1):
#     """
#     :param s1:
#     :return: 1 chuỗi đã được sử lý
#     ví dụ  xư lí ngôn tư niên -> xử lý ngôn tự nhiên
#     threshold sẽ là 0.5 cho từ có 2 kí tụ
#     threshold sẽ là 2/3 cho từ có 3 kí tụ trở lên
#     """
#     words = set(['xử','lý','ngôn','ngữ','tự','nhiên','lập','trình'])
#     words1 = s1.split()
#     s2=""
#     for temp in words1:
#         if(len(temp)>2):
#             for temp1 in words :
#                 kc = levenshteinDistance(temp,temp1)
#                 if kc >=2/3 :
#                     s2+=" " +temp1
#                     break
#         else:
#             for temp1 in words :
#                 kc = levenshteinDistance(temp,temp1)
#                 if kc >=0.5 :
#                     s2 += " " + temp1
#                     break
#     return s2
#

# arr = testDectect.split()
#
# for i in range(len(arr)):
#     if arr[i] == "học" and arr[i-1] == "môn":
#         index =i
#     if arr[i] == "học" and arr[i-1] == "lớp":
#         index = i
#     if arr[i] == "phần" and arr[i-1] == "học":
#         index = i
# print(index)

# """
# tham khao code tren mang, thay code rat ngan
# no se chay nhanh hon tam 3 lan code ben tren
# """
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
#         distances_ = [i2+1]
#         for i1, c1 in enumerate(s1):
#             if c1 == c2:
#                 distances_.append(distances[i1])
#             else:
#                 distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
#         distances = distances_
#     distac = 1- distances[-1]/max(len(s1),len(s2))
#     return distac
#
#
# """
# hàm này sử dụng để sửa lỗi chính tả đầu vào ví dụ max -> mã
# """
# def changeWordBeforePre(s1):
#     wordInit = set(["môn", "học", "phần", "lớp", "mã", "lịch,và"])
#     max =0
#     for text in wordInit :
#         if len(text) == 2:
#             t = levenshteinDistance(s1, text)
#             if  t > 0.33 and t > max:
#                 max =t
#                 s1 = text
#         else :
#             t = levenshteinDistance(s1, text)
#             if t > 0.4 and t >max:
#                 max =t
#                 s1 = text
#     return s1
# """
# sử dụng cả chuỗi input nhập vào
# tìm cho tôi mon hocj và  max lớp xử lý ngôn ngữ tự niên và tâm lý học
# -> tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học
# """
#
# def changeInput(s1):
#     arr = s1.split()
#     s2 =""
#     for t in arr :
#         s2 += " " + changeWordBeforePre(t)
#     return s2.strip()

#
# def dectectMyLogic(s1):
#         arr = s1.split()
#         s2 = ""
#         index = -1
#         for i in range(len(arr)):
#             if arr[i] == "học" and arr[i - 1] == "môn":
#                 index = i
#             if arr[i] == "học" and arr[i - 1] == "lớp":
#                 index = i
#             if arr[i] == "phần" and arr[i - 1] == "học":
#                 index = i
#             if arr[i] == "lớp" and arr[i - 1] == "mã":
#                 index = i
#         if index != -1:
#             for i in range(index + 1, len(arr)):
#                 s2 += " " + arr[i]
#         return index, s2
# print(dectectMyLogic("tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học").__getitem__(0))
"""
dung de sua loi chinh ta cho nguoi nhap vao
vi du: ngôn ngữ tự niên -> ngôn ngữ tự nhiên.
"""

def choseSenetence( s1):
    tenHp = set()
    import MySQLdb
    con = MySQLdb.connect(host="localhost",  user="root",  passwd="291096",  db="nlp",charset='utf8')
    query = con.cursor()
    query.execute("SELECT monhoc FROM tenmonhoc;")
    for row in query.fetchall():
        tenHp.add(row[0].lower())
    con.close()
    kc = 0.0
    for hp in tenHp:
        temp = levenshteinDistance(hp, s1)
        if temp > kc:
            kc = temp
            monhoc = hp
    if kc >= 0.5:
        return monhoc
    else:
        return False


"""
khi ham choseSentence khong the tra lai dc 1 ket qua hop ly,
ta se thu sua các từ nằm trong môn học họ nhập vào để đưa ra đc 1 kết quả mới
có thể dùng để chạy lại hàm choseSenten 1 lần nữa. trước khi ta nhận định
nguời dùng đã quá sai chinh tả
"""


def detecttenLop(s1):
    t = s1.split(',')
    t1 = t[-1].split("và")
    t.remove(t[-1])
    if len(t1) >= 1:
        for text in t1:
            t.append(text)
    for i in range(len(t)):
        t[i] = t[i].strip()
    return t


"""
su dung de sua ten lop
"""


def fixtenlop(s1):
    t = choseSenetence(s1)
    if t == False:
        return False
        # t1 = self.choseword(s1)
        # t = self.choseSenetence(t1)
    else:
        return t


def dectectMyLogic(s1):
    print(s1)
    arr = s1.split()
    s2 = ""
    index = -1
    for i in range(len(arr)):
        if arr[i] == "học" and arr[i - 1] == "môn":
            index = i
        if arr[i] == "học" and arr[i - 1] == "lớp":
            index = i
        if arr[i] == "phần" and arr[i - 1] == "học":
            index = i
        if arr[i] == "lớp" and arr[i - 1] == "mã":
            index = i
    if index != -1:
        for i in range(index + 1, len(arr)):
            s2 += " " + arr[i]
    return index, s2

"""
lay ten lop hoan thien vao mang
"""


def processTenLop(s1):
    t = detecttenLop(s1)
    rs = []
    firstTenlop = fixtenlop(t[0].lower())
    print(firstTenlop)
    if firstTenlop ==False:
        t1 = fixtenlop(dectectMyLogic(changeInput(t[0])).__getitem__(1))
        if t1 !=False:
            rs.append(t1)
    else:
        rs.append(firstTenlop)
    for i  in range(1,len(t)):
        tenlop = fixtenlop(t[i].lower())
        if tenlop != False:
            rs.append(tenlop)
    if len(rs) !=0:
        return True,rs
    return False



testdetect="tìm cho tao môn học tâm lý học, xử lý ngôn ngữ tự nhiên và học máy"


def changeWordBeforePre( s1):
    wordInit = set(["môn", "học", "phần", "lớp", "mã", "lịch", "và"])
    max = 0.0
    for text in wordInit:
        if len(s1) == 2:
            t = levenshteinDistance(s1, text)
            if t > 0.33 and t > max and len(text)==2:
                max = t
                s1 = text
            if t > 0.4 and t > max and len(text) > 2:
                max = t
                s1 = text
        else:
            t = levenshteinDistance(s1, text)
            if t > 0.4 and t > max:
                max = t
                s1 = text
    return s1


"""
sử dụng cả chuỗi input nhập vào 
tìm cho tôi mon hocj và  max lớp xử lý ngôn ngữ tự niên và tâm lý học 
-> tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học
"""


def changeInput( s1):
    arr = s1.split()
    s2 = ""
    for t in arr:
        s2 += " " + changeWordBeforePre(t)
    return s2.strip()

print(processTenLop("tâm lý học"))

def choseword(s1):
    """
    :param s1:
    :return: 1 chuỗi đã được sử lý
    ví dụ  xư lí ngôn tư niên -> xử lý ngôn tự nhiên
    threshold sẽ là 0.5 cho từ có 2 kí tụ
    threshold sẽ là 2/3 cho từ có 3 kí tụ trở lên
    """
    words = set()
    import MySQLdb
    con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                               user="root",  # your username
                               passwd="anhdem96",  # your password
                               db="nlp",
                               charset='utf8')
    query = con.cursor()
    query.execute("SELECT vocab FROM vocabulary;")
    for row in query.fetchall():
        words.add(row[0].lower())
    con.close()
    words1 = s1.split()
    s2 = ""
    max1 = 0.0
    nearlest = ""
    for temp in words1:
        for temp1 in words:
            kc = levenshteinDistance(temp, temp1)
            if kc >= max1:
                max1 = kc
                nearlest = temp1
            if max1 == 1:
                break
        if max1 >= 0.5:
            s2 += " " + nearlest
        else:
            s2 += " " + temp
print(levenshteinDistance("lý","lớp"))