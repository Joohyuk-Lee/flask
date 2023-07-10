from flask import Flask

# create_app() 이 실행되면 내부에 함수들이 모두 동작을 하게 된다
def create_app():
    # Flask는 우리가 지정하지 않으면 기본적으로 app.py를 시작점으로 인식해서 거기부터 코드를 찾아나갑니다.
    # Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다

    # 이 어플리케이션
    # 여기가 시작이야 가르쳐주는 것
    # 이걸 상속 받아서 다 진행된다. 어디서 시작하는 지 표시해 주는 __name__
    # 던더는 개발자를 위해 클래스에서 자동으로 생성된느 것들

    # Flask 패키지에 있는 클래스를 통해 어플리케이션의 입구를 만들어줍니다.
    app = Flask(__name__)

    # main_views 내부에 있는 bp를 통한 라우팅 함수들을 등록
    from views import main_views
    app.register_blueprint(main_views.bp)

    return app
