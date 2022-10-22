from flask import Flask


app = Flask(__name__)


topics = [
    {'id': 1, 'title': 'A', 'content': 'This is page A.'},
    {'id': 2, 'title': 'B', 'content': 'This is page B.'},
    {'id': 3, 'title': 'C', 'content': 'This is page C.'}
]


# 메인 페이지
@app.route('/')
def index():

    str= '' # html 코드를 담을 문자열

    # for문을 사용하여 str의 내용을 만들기
    for topic in topics:
        str = str + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>'

    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href = "/">Main</a></h1>
            <ol>
                {str}
            </ol>
        </body>
    </html>
    '''


# A, B, C를 눌러 들어간 페이지
@app.route('/read/<id>/')
def read(id):

    # URL에서 id 값 받아오기
    num = int(id)

    # 리스트의 인덱스는 0부터 시작하므로 1을 빼기
    num = num -1
    
    # num 값을 사용하여 content 값을 가져와 화면에 표시하기
    return f'{topics[num]["content"]}'


app.run()
