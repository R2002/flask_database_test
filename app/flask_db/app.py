from flask import Flask
import config
import models
from database import init_database, db_insert, db_delete

def create_app():
    # Flask
    app = Flask(__name__)
    # config
    app.config.update(config.cf)
    # DB初期化
    init_database(app)
    return app

app = create_app()

#--------------------------------------#
# データベース参照（view）
#--------------------------------------#
@app.route('/')
def index():
    html_list = ""
    list_Tests = models.Test.query.all()
    html_list += "<table border><tr><th>Id</th><th>Data</th></tr>\n"
    for i in list_Tests:
        html_list += "<tr><th>%s</th><td>%s</td></tr>\n" % (str(i.id), i.data)
    html_list += "</table>\n"
    return "Hello Flask<br>"+html_list

#--------------------------------------#
# 一行追加（insert）
#--------------------------------------#
@app.route('/insert/<param>')
def insert(param):
    test_new = models.Test(data=param)
    db_insert(test_new)
    return "insert: %s" % (param)

#--------------------------------------#
# 一行変更（update）
#--------------------------------------#
@app.route('/update/<id>/<param>')
def update(id, param):
    test_up = models.Test.query.filter_by(id=id).first()
    test_up.data=param
    db_insert(test_up)
    return "update(id:%s): to %s" % (id, param)

#--------------------------------------#
# 一行削除（delete）
#--------------------------------------#
@app.route('/delete/<id>')
def delete(id):
    test_del = models.Test.query.filter_by(id=id).first()
    db_delete(test_del)
    return "delete: id:%s" % (id)
