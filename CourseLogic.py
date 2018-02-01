# -*- coding: utf-8 -*-
from chatterbot.logic import LogicAdapter
class myCourseLogic (LogicAdapter):
    def __init__(self, **kwargs):
        super(myCourseLogic, self).__init__(**kwargs)

    # def can_process(self, statement):
    #     arr = statement.text.split()
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
    #         return True
    #     else:
    #         return False

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
        t1 = re.sub(r"[a-zA-Z]{2,3}[0-9]{4}[a-zA-Z]?", "",s1)
        if len(t) == 0:
            return False
        else:
            return t,t1

    def detectMlop(self,s1):
        import re
        t = re.findall(r"[0-9]{5,6}", s1)
        if len(t) == 0:
            return False
        else:
            return t

    """
    dung de sua loi chinh ta cho nguoi nhap vao
    vi du: ngôn ngữ tự niên -> ngôn ngữ tự nhiên.
    """

    def choseSenetence(self ,s1):
        tenHp = set(['xử lý ngôn ngữ tự nhiên', 'kĩ thuật hóa học', 'lập trình hướng đối tượng', 'lập trình c#'])
        kc = 0
        for hp in tenHp:
            temp = self.levenshteinDistance(hp, s1)
            if temp > kc:
                kc = temp
                monhoc = hp
            if kc > 0.6:
                break
        if kc > 0.6:
            return monhoc
        else:
            return 0

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
        words = set(['xử', 'lý', 'ngôn', 'ngữ', 'tự', 'nhiên', 'lập', 'trình'])
        words1 = s1.split()
        s2 = ""
        for temp in words1:
            if (len(temp) > 2):
                for temp1 in words:
                    kc = self.levenshteinDistance(temp, temp1)
                    if kc >= 2 / 3:
                        s2 += " " + temp1
                        break
            else:
                for temp1 in words:
                    kc = self.levenshteinDistance(temp, temp1)
                    if kc >= 0.5:
                        s2 += " " + temp1
                        break
        return s2
    def process(self, statement):

        # out = self.dectectMyLogic(statement.text).__getitem__(1)
        from chatterbot.conversation import Statement
        return 1, Statement('số lớp là ')

    def output(self,s1):
        newS=""
        newS1=""
        mahp=[]
        malop=[]
        if self.detectmaHp(s1) != False:
            mahp = self.detectmaHp(s1).__getitem__(0)
            newS = self.detectmaHp(s1).__getitem__(1)
        if self.detectMlop(newS) !=False:
            malop = self.detectMlop(newS).__getitem__(0)
            newS1 = self.detectMlop(newS).__getitem__(1)
        str1 =""
        for text in mahp :
            str1 += " " + str(text)
        for text in malop :
            str1 += " " + str(text)
        return str1 + " "+ newS1

