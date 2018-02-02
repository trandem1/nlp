# -*- coding: utf-8 -*-
from chatterbot.logic import LogicAdapter
class myCourseLogic (LogicAdapter):
    def __init__(self, **kwargs):
        super(myCourseLogic, self).__init__(**kwargs)

    def changeWordBeforePre(self,s1):
        wordInit = set(["môn", "học", "phần", "lớp", "mã", "lịch", "và"])
        max = 0.0
        for text in wordInit:
            if len(s1) == 2:
                t = self.levenshteinDistance(s1, text)
                if t > 0.33 and t > max and len(text) == 2:
                    max = t
                    s1 = text
                if t > 0.4 and t > max and len(text) > 2:
                    max = t
                    s1 = text
            else:
                t = self.levenshteinDistance(s1, text)
                if t > 0.4 and t > max:
                    max = t
                    s1 = text
        return s1

    """
    sử dụng cả chuỗi input nhập vào 
    tìm cho tôi mon hocj và  max lớp xử lý ngôn ngữ tự niên và tâm lý học 
    -> tìm cho tôi môn học và mã lớp xử lý môn ngữ tự niên và tâm lý học
    """

    def changeInput(self,s1):
        arr = s1.split()
        s2 = ""
        for t in arr:
            s2 += " " + self.changeWordBeforePre(t)
        return s2.strip()

    def can_process(self, statement):
        t = self.replaceMlop(self.replacemaHP(statement.text))
        if self.detectMlop(statement.text) != False:
            return True
        elif self.detectmaHp(statement.text) != False:
            return True
        elif self.processTenLop(t).__getitem__(0) != False:
            return True
        else:
            return False

    def dectectMyLogic(self,s1):
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

    def levenshteinDistance(self,s1, s2):
        """
        :param s1:la chuoi ki tu
        :param s2:la chuoi ki tu
        :return: khoang cach cua 2 chuoi dau vao
        """
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        distances = range(len(s1) + 1)
        for i2, c2 in enumerate(s2):
            distances_ = [i2 + 1]
            for i1, c1 in enumerate(s1):
                if c1 == c2:
                    distances_.append(distances[i1])
                else:
                    distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
            distances = distances_
        distac = 1 - distances[-1] / max(len(s1), len(s2))
        return distac

    def detectmaHp(self,s1):
        import re
        t = re.findall(r"[a-zA-Z]{2,3}[0-9]{4}[a-zA-Z]?", s1)
        if len(t) == 0:
            return False
        else:
            return t

    def replacemaHP(self,s1):
        import re
        t1 = re.sub(r"[a-zA-Z]{2,3}[0-9]{4}[a-zA-Z]?", "", s1)
        return t1

    def detectMlop(self,s1):
        import re
        t = re.findall(r"[0-9]{5,6}", s1)
        if len(t) == 0:
            return False
        else:
            return t

    def replaceMlop(self,s1):
        import re
        t1 = re.sub(r"[0-9]{5,6}", "", s1)
        return  t1

    """
    dung de sua loi chinh ta cho nguoi nhap vao
    vi du: ngôn ngữ tự niên -> ngôn ngữ tự nhiên.
    """

    def choseSenetence(self ,s1):
        tenHp = set()
        import MySQLdb
        con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                                   user="root",  # your username
                                   passwd="291096",  # your password
                                   db="nlp",
                                   charset='utf8')
        query = con.cursor()
        query.execute("SELECT monhoc FROM tenmonhoc;")
        for row in query.fetchall():
            tenHp.add(row[0].lower())
        con.close()
        kc = 0.0
        for hp in tenHp:
            temp = self.levenshteinDistance(hp, s1)
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
    def choseword(self,s1):
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
                                   passwd="291096",  # your password
                                   db="nlp",
                                   charset='utf8')
        query = con.cursor()
        query.execute("SELECT vocab FROM vocabulary;")
        for row in query.fetchall():
            words.add(row[0].lower())
        con.close()
        words1 = s1.split()
        s2 = ""
        max1 =0.0
        nearlest=""
        for temp in words1:
            for temp1 in words:
                kc = self.levenshteinDistance(temp, temp1)
                if kc >= max1:
                    max1 = kc
                    nearlest = temp1
                if max1 == 1:
                    break
            if max1 >= 0.5:
                s2 +=" " + nearlest
            else:
                s2 += " " + temp
            # if (len(temp) > 2):
            #     for temp1 in words:
            #         kc = self.levenshteinDistance(temp, temp1)
            #         if kc >= 2 / 3:
            #             s2 += " " + temp1
            #             break
            # else:
            #     for temp1 in words:
            #         kc = self.levenshteinDistance(temp, temp1)
            #         if kc >= 0.5:
            #             s2 += " " + temp1
            #             break
        return s2
    def process(self, statement):
        # out = self.dectectMyLogic(statement.text).__getitem__(1)
        from chatterbot.conversation import Statement
        outhp =self.outputhp(statement.text)
        outMl = self.outputMlop(statement.text)
        t = self.replacemaHP(statement.text)
        t1 = self.replaceMlop(t)
        t = Statement('ket qua la \n '+outhp +"\n"+outMl +"\n"+self.outputTenlop(self.changeInput(t1)))
        t.confidence = 1
        return t
    """
    ham nay dung de cat ten lop tu 1 chuoi
    """
    def detecttenLop(self,s1):
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
    def fixtenlop(self,s1):
        t = self.choseSenetence(s1)
        if t == False:
            return False
            # t1 = self.choseword(s1)
            # t = self.choseSenetence(t1)
        else:
            return t
    """
    lay ten lop hoan thien vao mang
    """
    def processTenLop(self,s1):
        # print(s1)
        t = self.detecttenLop(s1)
        rs = []
        firstTenlop = self.fixtenlop(t[0].lower())
        if firstTenlop == False:
            t1 = self.fixtenlop(self.dectectMyLogic(self.changeInput(t[0])).__getitem__(1))
            if t1 != False:
                rs.append(t1)
        for i in range(1, len(t)):
            tenlop = self.fixtenlop(t[i].lower())
            if tenlop != False:
                rs.append(tenlop)
        if len(rs) != 0:
            return True, rs
        return False

    def outputhp(self,s1):
        str1 = "ma hoc phan: "
        mahp = self.detectmaHp(s1)
        if mahp != False :
            for text in mahp:
                str1 += "\n " + str(text)
            return str1
        else:
            return "0"
    def outputMlop(self,s1):
        str2 = "ma lop: "
        malop = self.detectMlop(s1)
        if malop != False :
            if malop != False:
                for text in malop:
                    str2 += "\n" + str(text)
            return str2
        return "0"

    def outputTenlop(self,s1):
        if self.processTenLop(s1) != False:
            str1 ="tên lớp học \n"
            for text in self.processTenLop(s1).__getitem__(1):
                str1 +=text+"\n"
            return str1
        else:
            return "0"


    # def output(self,s1):
    #     str1 = "ma hoc phan: "
    #     mahp =self.detectmaHp(s1)
    #     if mahp != False:
    #         for text in mahp:
    #             str1 += "\n " + str(text)
    #         newS = self.replacemaHP(s1)
    #     else:
    #         newS = s1
    #     str1 += "\n ma lop: "
    #     malop = self.detectMlop(newS)
    #     if malop !=False:
    #         newS1 = self.replaceMlop(newS)
    #         for text in malop:
    #             str1 += "\n" + str(text)
    #     else:
    #         newS1 = newS
    #     tenlop = self.processTenLop(newS1)
    #     str1 +="\n ten lop:"
    #     for text in tenlop:
    #         str1 +="\n "+str(text)
    #     return str1




