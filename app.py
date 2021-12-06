from flask import Flask, render_template
import pymysql
from db_connect import db
from main.join import join_bp
from main.board import board_bp
from main.login import login_bp
from main.docs import docs_bp
from main.faqs import faqs_bp
from main.about import about_bp
import json

app = Flask(__name__)

# blueprint
app.register_blueprint(join_bp)
app.register_blueprint(board_bp)
app.register_blueprint(login_bp)
app.register_blueprint(docs_bp)
app.register_blueprint(faqs_bp)
app.register_blueprint(about_bp)


# root
@app.route('/')
def main():
    return render_template('home.html')


# db config 파일 불러오기
with open("./db_config.json", 'r') as f:
    dbConfig = json.load(f)

print(dbConfig['name'])

# db 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    dbConfig['name'], dbConfig['dbPassword'], dbConfig['address'], dbConfig['port'], dbConfig['dbName'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db 지정
db.init_app(app)

# table 생성
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(port=5000, debug=True)
