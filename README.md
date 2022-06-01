# b-l1

# backend(Django(Serializer, Settings, Database, Middleware), Docker, Github)
- low - b-l1 - Django 튜토리얼 페이지 띄우기, git clone or package download 부터 튜토리얼 페이지에 기술된 기본 backend 페이지 생성 (done) <br/>
- low - b-l2 - Docker를 이용하여 Django app 띄우기, Dockerfile 및 script 를 이용하여 Django app container 생성 (done) <br/>
- mid - b-m1 - Django Endpoint 생성, serializer, view 등의 구성을 통한 endpoint 구성 (done) <br/>
- mid - b-m2 - Django Setting 변경, Django 내에서 사용되는 settings 값 조정(DEBUG, APPEND_SLASH 등) (done) <br/>
- high - b-h1 - Django model 을 활용한 DB 연결, Django model 을 활용하여 DB 연결 및 데이터 전송, DB는 로컬 DB 생성하여 사용 (done) <br/>
- high - b-h2 - Error Log 용 middleware 구성, 400, 500대 에러 리턴을 잡기위한 Middleware 구성 (done) <br/>

# 추가 과제 발생

1. serializer constraint 조건 넣고 잘 동작하는지 확인 (done)
2. 추후 추가 확인사항 전달 예정
3. Api에서 exception을 raise하는게 아니라 특정 에러코드(ex. 400/404/500) 발생 시 middleware에서 에러로깅
