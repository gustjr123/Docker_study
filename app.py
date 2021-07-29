from flask import Flask, render_template
import pymysql

app = Flask(__name__)

@app.route('/')
def index() :
    return render_template('index.html', dbdata = rundb())

def rundb():
    # DB 연결
    mydb = pymysql.connect(
        user='DB_USER',
        password='DB_PASSWORD',
        table='DB_NAME',
        hosts='DB_HOST',
        charset='utf8'
    )

    # 커서이용 데이터 프레임을 쉽게 반환
    cursor = mydb.cursor(pymysql.cursors.DictCursor)

    sql = "SELECT * FROM 'test';"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

if __name__ == '__main__' :
    app.run(debug=True)

