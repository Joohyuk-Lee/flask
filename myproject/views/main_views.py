from flask import Blueprint


# Blueprint 클래스를 통해 임의의 객체를 만듭니다
# bp = Blueprint('앱 내부에서 부를 별명', 전달되는 파일명, url_prefix = 해당 blueprint가 전달할 최상위 경로)
bp = Blueprint('main', __name__, url_prefix='/')

# 선으로 접속되어 있는 인터넷을 연결해주는 router
@app.route("/")
def hello():
    return f"Hello, {__name__}"


@app.route("/lee")
def hello_lee():
    return f"Hello, Lee!"

# 우리가 뭔가를 변경하면 새로고침하여 바로 적용이 되게 하는 것 : debug mode???

@app.route('/jjangu')
def hello_jjangu():
    return f'<b> JJANGGU </b>'
