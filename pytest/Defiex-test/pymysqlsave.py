import pymysql
import contextlib


class MysqlSave(object):
    def __init__(self):
        """
        数据库参数配置区域
        """
        # self.path = 'localhost'
        # self.port = 3306
        # self.username = 'root'
        # self.password = '19990728'
        self.path = 'rm-uf6649g51fy20qmpyno.mysql.rds.aliyuncs.com'
        self.port = 3306
        self.username = 'pl'
        self.password = 'wjrzm19990728'
        self.dbname = 'pymysql_defiex'
        self.db = pymysql.connect(
            host=self.path, port=self.port, db=self.dbname,
            user=self.username, password=self.password, charset='utf8'
        )
        """
        Cursor
        普通的游标对象，默认创建的游标对象
        SSCursor
        不缓存游标，主要用于当操作需要返回大量数据的时候
        DictCursor
        以字典的形式返回操作结果
        SSDictCursor
        不缓存游标，将结果以字典的形式进行返回
        """
        # 创建游标，操作返回数据为字典类型
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def __enter__(self):
        # 返回self全局变量
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 提交数据库并执行
        self.db.commit()
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.db.close()

    def __dictchangesql(self, message: dict) -> str and tuple:
        keylist = []
        valuelist = []
        for key, value in message.items():
            keylist.append(key)
            valuelist.append(value)
        keytuple = tuple(keylist)
        valuetuple = tuple(valuelist)
        keystr = str(keytuple).replace('\'', "")
        return keystr, valuetuple

    def insert(self, tablename: str, message: dict) -> None:
        keystr, valuetuple = self.__dictchangesql(message)
        insertsql = """INSERT INTO {}{} VALUES{}
        """.format(tablename, keystr, valuetuple).replace("\n", "")
        print(insertsql)
        self.cursor.execute(insertsql)

    def create(self, tablename: str, message: list) -> dict:
        messages = tuple(message)
        message_str = str(messages).replace('\'', "")
        createsql = """CREATE TABLE {}{}""".format(tablename, message_str)
        print(createsql)
        self.cursor.execute(createsql)

    def select(self, selectfield: list, tablename: str, condition: dict):
        selectfieldstr = str(','.join(selectfield))
        conditionlist = []
        for key, value in condition.items():
            conditionlist.append(key + '="' + value + '"')
        conditionstr = str(' or '.join(conditionlist))
        selectsql = """SELECT {} FROM {} WHERE {}
            """.format(selectfieldstr, tablename, conditionstr)
        # print(selectsql)
        self.cursor.execute(selectsql)
        data = self.cursor.fetchall()
        # print(data)
        return data

    def update(self, tablename: str, message: dict, condition: dict) -> None:
        conditionlsit = []
        for key, value in condition.items():
            conditionlsit.append(key + '="' + value + '"')
        conditionstr = str(' or '.join(conditionlsit)).replace('\'', "")
        messagelist = []
        for key, value in message.items():
            messagelist.append(key + '="' + value + '"')
        # print(messagelist)
        messagestr = str(','.join(messagelist)).replace('\'', "")
        # print(messagestr)
        updatesql = """UPDATE {} SET {} WHERE {}""".format(
            tablename, messagestr, conditionstr
        ).replace('\n', "")
        # print(updatesql)
        self.cursor.execute(updatesql)

    def delete(self, tablename: str, condition: dict) -> None:
        conditionlsit = []
        for key, value in condition.items():
            conditionlsit.append(key + '="' + value + '"')
        conditionstr = str(' or '.join(conditionlsit)).replace('\'', "")
        delete_sql = """DELETE FROM {} WHERE {}""".format(tablename, conditionstr)
        print(delete_sql)
        self.cursor.execute(delete_sql)

    # REPLACE INTO
    def replace(self, tablename: str, message: dict) -> None:
        message_list = []
        for key, value in message.items():
            message_list.append(key + '="' + value + '"')
        message_str = str(','.join(message_list)).replace('\'', "")
        replace_sql = """REPLACE INTO {}{}""".format(
            tablename, message_str
        ).replace('\n', "")
        self.cursor.execute(replace_sql)


with MysqlSave() as db:
    create_message = [
        'username varchar(50) not null',
        'orderid varchar(50) not null',
        'BTC varchar(200) not null',
        'ETH varchar(100) not null',
        'TRX varchar(100) not null',
        'environment varchar(30) not null',
        'get_time varchar(30)'
    ]

    # db.delete('granary_message', message)
    # db.create('recharge_site', create_message)
    # db.insert('user', insert_message)
    # db.update('xxx',message_update,update_condition)
    # db.select(select_message, 'domain', select_dict)
