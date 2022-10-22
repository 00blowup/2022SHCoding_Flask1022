from flask import Flask


app = Flask(__name__)


topics = [
    {'id': 1, 'title': 'A', 'content': 'This is page A.'},
    {'id': 2, 'title': 'B', 'content': 'This is page B.'},
    {'id': 3, 'title': 'C', 'content': 'This is page C.'}
]


# 중복되는 부분을 함수화함
def template(content):

    str= '' # html 코드를 담을 문자열

    # for문을 사용하여 str의 내용을 만들기
    for topic in topics:
        str = str + f'<li><a href = "/read/{topic["id"]}/">{topic["title"]}</a></li>'
    
    # 리턴
    return f'''<!doctype html>
    <html>
        <body>
            <h1><a href = "/">Main</a></h1>
            <ol>
                {str}
            </ol>
            {content}
        </body>
    </html>
    '''


# 메인 페이지
@app.route('/')
def index():
    return template('<span>Welcome!</span>')


# A, B, C를 눌러 들어간 페이지
@app.route('/read/<int:id>/')
def read(id):

    content = ''

    for topic in topics:
        if topic['id'] == id:
            content = topic['content']

    return template(content)



app.run()
