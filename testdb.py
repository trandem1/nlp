# import MySQLdb
# con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
#                                    user="root",  # your username
#                                    passwd="anhdem96",  # your password
#                                    db="test_it4421",
#                                    charset='utf8')
# query = con.cursor();
# query.execute("SELECT distinct(ten_hp) FROM test_it4421.tkb;")
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

"""
code nhung chua toi uu, don thuan doc thuat toan de code
import time
t = time.time()
Distance('dva','dave')
te=time.time()-t
t2= time.time()
levenshteinDistance('dva','dave')
te1 = time.time()-t2
print(te/te1)
# print(t)
"""
def Distance(s1,s2):
    nStt = [0 for i in range(len(s1)+1)]
    for x in range(len(nStt)):
        nStt[x] =[0 for i in range(len(s2) +1)]
    for x in range(len(s2)+1):
        nStt[0][x] =x
    for x in range(len(s1)+1):
        nStt[x][0] =x
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j] :
                nStt[i+1][j+1] = nStt[i][j]
            else:
                nStt[i+1][j+1] = 1 + min(nStt[i][j],nStt[i][j+1],nStt[i+1][j])
    return nStt[len(s1)][len(s2)]

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
    distac = 1- distances[-1]/len(s1)
    return distac

"""
dung de sua loi chinh ta cho nguoi nhap vao
vi du: ngôn ngữ tự niên -> ngôn ngữ tự nhiên.
"""

def choseSenetence (s1):
    tenHp = set(['xử lý ngôn ngữ tự nhiên', 'kĩ thuật hóa học','lập trình hướng đối tượng','lập trình c#'])
    kc = 0
    for hp in tenHp :
        temp =levenshteinDistance(hp,s1)
        if  temp > kc :
            kc = temp
            monhoc= hp
    return monhoc
print(choseSenetence("ngon ngữ tự niên"))


