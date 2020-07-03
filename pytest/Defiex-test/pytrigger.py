import os
import sqlite3


class SqlSave(object):
    def __init__(self):
        self.table_list = ['general', 'supernode', 'Admin_testname', 'url']

    def __enter__(self):
        workpath = os.getcwd()
        '''
        os.path.realpath(__file__) 获取当前文件绝对路径
        os.path.split(os.path.realpath(__file__)) 获取当前文件绝对路径跟文件名
        os.getcwd() 获取当前工作路径
        '''
        self.conn = sqlite3.connect(workpath + '\\test.db')
        self.curse = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_t):

        self.curse.close()
        self.conn.commit()
        self.conn.close()

    def testview(self):
        create_sql = 'create view testview as select * from Name_ResponseMsg'
        self.curse.execute(create_sql)

    def trigger(self):
        create_sql = 'create trigger testview_trigger before insert on Name_ResponseMsg ' \
                     'for each row ' \
                     'begin ' \
                     'insert into Name_ResponseMsg_from(name, userid, token, invitecode, gettime, evviromment) ' \
                     'values(NEW.name, NEW.userid, NEW.token, NEW.invitecode, NEW.gettime, NEW.evviromment);' \
                     'end;'

        print(create_sql)
        self.curse.execute(create_sql)

with SqlSave() as execute:
    # execute.testview()
    execute.trigger()