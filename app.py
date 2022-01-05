from flask import Flask
from flask_restful import Api
from resources.login import UserLoginResource

from resources.register import UserRegisterResource

app = Flask(__name__)

api = Api(app)
# api.add_resource(,'')
api.add_resource(UserRegisterResource, '/user/register') #가입
# api.add_resource(UserLoginResource,'/user/login') #로그인
# api.add_resource(,'/user/logout') #로그아웃
# api.add_resource(,'/memo') #메모 불러오기
# api.add_resource(,'/memo/<int:memo_id>') #메모 작성, 수정, 삭제


if __name__ == "__main__":
    app.run