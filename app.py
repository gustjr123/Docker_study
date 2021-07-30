from flask import Flask, render_template
import dbModule

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:admin1234@devops-cd.cldqdwlkg9c1.ap-northeast-2.rds.amazonaws.com/i-076916a094f016fbf'
# db = sqlalchemy(app)

# SELECT 함수 예제
@app.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()

    sql = "SELECT * FROM flask_db.test"
    row = db_class.executeAll(sql)

    print(row)

    return render_template('test.html', resultData=row)

@app.route('/')
def index() :
    return render_template('index.html')

if __name__ == '__main__' :
    app.run(debug=True)

