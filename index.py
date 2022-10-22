from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome'

@app.route('/create/')
def create():
    return 'Create'

# id라는 변수의 값을 URL에서 얻어와 동적으로 반영하기
@app.route('/read/<id>')
def read(id):
    return 'Reading ' + id


app.run()