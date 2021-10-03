# company
fastapi project

-----
# 1. Framework 선택
## Flask vs Fastapi
## 1.1. Flask
~~~
* WSGI(Web sever gateway interface)
* 동기식만지원 (Guniorn 으로 어느정도까지는 비동기 커버 가능)
* 롱폴링, 웹 소켓같은 긴 커넥션 연결에는 부적절
* request/response

* + 모든 ORM 지원
* + 쿠키, 클라이언트 사이드 지원
* + 유닛테스트, 디버거
~~~

## 1.2. Fastapi
~~~
* ASGI(Asyncronous sever gayeway interface) - WSGI의 상위집합
* 비동기식도 지원
* Go와 Node.JS에 필적할 만큼 빠름
* send/sevice

* +OpenAPI문서지원
* 언블락킹 ORM
* starlette uvicorn
~~~

## -> 구현은 플라스크가 쉬워보이지만 트랜드에 맞춰 FastAPI 사용해보려고함
### 선택에 참고한 글 https://jybaek.tistory.com/890

-----

# 2. 기본 개발환경 구축
## 2.1기존에 작업하던 암호화모듈때문에 파이썬 인터프리터에 명령어가 안깔림
### 파이썬 설치 경로 강체 세팅
~~~
pip3 config set global.target /Users/kogayoung/company/lib/python3.7/site-packages
~~~

## 2.2 Configuration 
~~~
### Module name: unicorn
### Parameter : main:app --reload
### * 127.0.0.1:8000 접속

### 참고 자동으로 만들어진 Swagger
### * 127.0.0.1:8000/docs 접속
### 127.0.0.1:8000/redoc 접속
~~~

-----

# 3. Git 연동
## 3.1. 새 레파지토리 만들기
~~~
git init
깃에서 New repository 생성
Url 복사

Git remote add origin “url”
git add .
git commit -m “커밋메시지”
git push origin master
~~~
## 3.2. 소스트리 연결
~~~
새로만들기-> 로컬저장소 추가 -> 작업디렉토리 선택
(필요에따라 디폴트 브랜치 변경)

나중에 필요한경우 pip3 install -r requirements.txt
~~~

## 3.3. Git ignore 생성
~~~
https://www.toptal.com/developers/gitignore
~~~

-----
# 4. 문제파악
## 4.1. pytest이해
~~~
https://binux.tistory.com/47
~~~

## 4.2. Fastapi 공식문서 
~~~ 
https://fastapi.tiangolo.com/ko/
~~~

## 4.3. ORM 연결 
~~~
 * Mssql
https://dingrr.com/blog/post/python-fastapi-%EB%A1%9C-%EB%B0%B1%EC%97%94%EB%93%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0-3%ED%99%94-mysql-%EC%97%B0%EA%B2%B0
 * postgreSQL
https://blog.neonkid.xyz/253
~~~
