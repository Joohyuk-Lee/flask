from flask import Flask

# 이 어플리케이션
# 여기가 시작이야 가르쳐주는 것
# 이걸 상속 받아서 다 진행된다. 어디서 시작하는 지 표시해 주는 __name__
# 던더는 개발자를 위해 클래스에서 자동으로 생성된느 것들

# Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다.
app = Flask(__name__)

# 선으로 접속되어 있는 인터넷을 연결해주는 router
@app.route("/")
def hello():
    return f"Hello, {__name__}"


@app.route("/lee")
def hello_lee():
    return f"Hello, Lee!"

# 우리가 뭔가를 변경하면 새로고침하여 바로 적용이 되게 하는 것 : debug mode???