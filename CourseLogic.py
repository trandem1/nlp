# -*- coding: utf-8 -*-
from chatterbot.logic import LogicAdapter
class myCourseLogic (LogicAdapter):
    def __init__(self, **kwargs):
        super(myCourseLogic, self).__init__(**kwargs)

    def can_process(self, statement):
        arrInput = statement.text.split()
        words = ['môn','lớp','học']
        if all(x in words for x in arrInput):
            return True

        return True


    def process(self, statement):
        """
        xu ly sau co y muon tim kiem khoa hoc
        :param statement:
        :return:
        """

        from chatterbot.conversation import Statement
        return 1, Statement('số lớp là ' + self.output('BF2011'))

    def output(self,name):
        print (name)
        import MySQLdb
        con = db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                                   user="root",  # your username
                                   passwd="anhdem96",  # your password
                                   db="test_it4421",
                                   charset='utf8')
        query = con.cursor();
        query.execute("SELECT * FROM tkb where ma_hp = 'BF2011'")
        row = query.fetchone()
        for col in row:
            print(col)
        return "1"


