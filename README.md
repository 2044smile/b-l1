# b-l1

# backend(Django(Serializer, Settings, Database, Middleware), Docker, Github)
- low - b-l1 - Django 튜토리얼 페이지 띄우기, git clone or package download 부터 튜토리얼 페이지에 기술된 기본 backend 페이지 생성 (done) <br/>
- low - b-l2 - Docker를 이용하여 Django app 띄우기, Dockerfile 및 script 를 이용하여 Django app container 생성 (done) <br/>
- mid - b-m1 - Django Endpoint 생성, serializer, view 등의 구성을 통한 endpoint 구성 (done) <br/>
- mid - b-m2 - Django Setting 변경, Django 내에서 사용되는 settings 값 조정(DEBUG, APPEND_SLASH 등) (done) <br/>
- high - b-h1 - Django model 을 활용한 DB 연결, Django model 을 활용하여 DB 연결 및 데이터 전송, DB는 로컬 DB 생성하여 사용 (done) <br/>
- high - b-h2 - Error Log 용 middleware 구성, 400, 500대 에러 리턴을 잡기위한 Middleware 구성 (done) <br/>

# 추가 과제 발생

* serializer constraint 조건 넣고 잘 동작하는지 확인 (done)
* 추후 추가 확인사항 전달 예정
* Api에서 exception을 raise하는게 아니라 특정 에러코드(ex. 400/404/500) 발생 시 middleware에서 에러로깅

# 일지(2022-06-02)

* Django Serializer 
* Model(managed=False) 
* View(Call Serializer)
* request.META.get()를 이용하여 TOKEN 을 처리할 수 있음
* trim_whitespace=True, Default True 기본적으로 True를 가지고 있음

# 일지(2022-06-03)

* network token header
* permissions.BasePermission
* Serializer - allow_blank=True  # ''이 들어와도 된다면 True

# 일지(2022-06-05)

* allow_blank / 특이 케이스가 발생하였음, 아무런 데이터가 없어도 '' 로 들어오는 문제 때문에 True로 설정
* token / request.META.get('') 은 postman or swagger 기능을 이용하여 삽입할 수 있다. EX) headers
* DRF의 경우 Serializer를 Request와 Response를 할 때 검증해야 되는 것으로 확인
  * Django Rest Framework 따라서 RESTful 기능을 HTTP Method와 함께 사용해 웹, 데스크탑 앱, 스마트폰 어플들까지 하나의 API 서버를 생성
  * API View, Mixins, Generic APIView, ViewSet / 간단한 로직은 API View 데코레이터를 이용하여 '함수형 뷰'로 구현하는 것도 좋다.
  * DB data -> JSON 
  * Mixins
    * CreateModelMixin
    * ListModelMixin
    * RetrieveModelMixin
    * UpdataModelMixin
    * DestroyModelMixin
    * queryset 과 serializer_class 를 지정해 주고 상속받은 Mixins 와 연결만 해주면 됩니다.
  * Generic APIView
    * generics.CreateAPIView : 생성
    * generics.ListAPIView : 목록
    * generics.RetrieveAPIView : 조회
    * generics.DestroyAPIView : 삭제
    * generics.UpdateAPIView : 수정
    * generics.RetrieveUpdateAPIView : 조회 / 수정
    * generics.RetrieveDestroyAPIView : 조회 / 삭제
    * generics.ListCreateAPIView : 목록 / 생성
    * generics.RetrieveUpdateDestroyAPIView : 조회 / 수정 / 삭제
    * 위에서 언급한 Mixins와 APIView 함수형 보다는 Generic APIView가 좋은 것 같다.
    * Generic APIView vs ViewSet 이지 않을까 싶다.
  * 
