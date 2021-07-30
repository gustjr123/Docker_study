import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='devops-cd.cldqdwlkg9c1.ap-northeast-2.rds.amazonaws.com',
                                  user='admin',
                                  password='admin1234',
                                  db='flask_db',
                                  charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)

    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()

