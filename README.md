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
  * **Generic APIView** &#x1F34E;
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
  * **ViewSet** &#x1F34E;
    * 하나의 단일클래스에 제공합니다.
    * 하나의 헬퍼클래스로 두 개 이상의 URL 처리가 가능한 것입니다.
    * ReadOnlyModelViewSet - list / detail
    * ModelViewSet - list, create / detail, update, partial_update, delete
    * Generic APIView와의 차이점은 queryset 과 serializer_class 를 지정해주고, url을 매핑하면 됩니다. url 을 매핑하는 방법은 두 가지가 있다.
      * 보통 'Router 를 통해 일괄적으로 등록'을 사용한다. 
![image](https://user-images.githubusercontent.com/47213853/172044072-25f41057-963f-43d5-bdb8-4e7a72537622.png)

# 일지(2022-06-06)

* Github commit https://underflow101.tistory.com/31
  * type, body, footer

# 일지(2022-06-08)

* Github actions
  * https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions 
  * GitHub Actions는 빌드, 테스트 및 도입 파이프라인을 자동화할 수 있는 지속적인 통합 및 연속 전달(CI/CD) 플랫폼입니다.
  * **Actions - 직접 액션을 작성하거나 GitHub 마켓플레이스에서 워크플로우에서 사용할 액션을 찾을 수 있습니다.**
  * YAMI 파일로 정의

# 일자(2022-06-09)

* Github Actions
  * Github CI AWS, Docker, ECR 한마디로 actions로 돌리는 것들까지가 CI
  * GIthub CD deploy(helm install or helm upgrade) 배포

# 일자(2022-06-10)

* https://dingrr.com/blog/post/drf%EB%8A%94-%EC%9D%B4%EC%A0%9C-%EC%9E%8A%EC%9C%BC%EC%84%B8%EC%9A%94-django-ninja-%EC%9D%98-%ED%83%84%EC%83%9D
* INTERESTING, Django DRF Serializer가 느리다. Django Ninga를 개인 프로젝트에서 구현 시도!
  * 기본적으로 스웨거를 지원한다.
* io.BytedIO() 객체를 넘겨주면 객체 내에 저장된 bytes 정보를 불러와 이미지로 읽어주는 흐름인 것 같다.
* io.BytesIO() 이름에서 짐작할 수 있듯이 **바이트 배열을 이진 파일로 다룰 수 있게 해주는 클래스**입니다.
  * 바이트 배열은 8 비트 (이진 데이터) 
  * 바이트 배열을 사용하여 이진 데이터 모음 (예 : 파일 내용)을 저장할 수 있습니다. 단점은 전체 파일 내용을 메모리에로드해야한다는 것입니다.
