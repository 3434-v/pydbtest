import pymysql
import contextlib


class MysqlSave(object):
    def __init__(self):
        """
        数据库参数配置区域
        """
        self.path = 'localhost'
        self.username = 'root'
        self.password = '19990728'
        self.dbname = 'pymysql_defiex'

    def __enter__(self):

        self.db = pymysql.connect(
            self.path, self.username, self.password, self.dbname, charset='utf8'
        )
        self.cursor = self.db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db.close()

    def user(self, name: str, password: str, environment: str) -> None:
        createsql = """
            CREATE TABLE user(id )
        
        """