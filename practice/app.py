# flask 호출
from flask import Flask

# app: Flask에 있는 웹 서버 객체
# __name__: 특수 변수, 현재 실행 중인 모듈(파일) 이름
app = Flask(__name__)

# 라우팅, 데코레이터
# @: 데코레이터, 기존 함수의 기능을 확장해 주는 역할
# route('/'): 라우팅, 이정표
# '/': 대문
@app.route('/')

# 데코레이터 및에 나오는 함수를 뷰 함수라고 부름
# 사용자가 메인 주소 '/'로 접속하는 순간, 플라스크는 뷰 함수 자동 호출
# return은 응답데이터
def hello_world():
    # 웹사이트 문자열
    return "안녕하세요!"