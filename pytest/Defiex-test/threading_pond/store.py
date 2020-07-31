import pymysql


class MysqlSave(object):
    def __init__(self):
        """
        数据库参数配置区域
        """
        # self.path = 'localhost'
        # self.port = 3306
        # self.username = 'root'
        # self.password = '19990728'
        # self.dbname = 'pymysql_defiex'
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

    def store(self):
        self.cursor.callproc('select_lever', ['389863294@qq.com'])
        result = self.cursor.fetchall()
        print(result)


excute = MysqlSave()
excute.store()

