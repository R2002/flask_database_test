import os
cf = {}
#--------------------------------------#
# 設定ファイル
#--------------------------------------#
# デバッグ有無
cf['DEBUG'] = 1

# 基礎設定
cf['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'host': os.getenv('DB_HOST', 'localhost'),
    'db_name': 'flask_db',
})
cf['SQLALCHEMY_TRACK_MODIFICATIONS'] = False