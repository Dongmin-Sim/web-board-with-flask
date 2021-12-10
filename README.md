# Flask를 활용한 자유게시판 프로젝트

## 프로젝트 소개

Flask를 활용하여 로그인, 게시글 포스트, 삭제 등 여러 기능을 구현하고 게시글을 게시하고 확인할 수 있는 게시판 프로젝트입니다.

## 프로젝트 목적

- Flask 웹 서버의 동작과정을 이해합니다.
- 데이터 베이스와 연동하는 방법을 이해합니다.
- ORM을 활용하여 데이터베이스 저장/수정/삭제를 할 수 있습니다.
- 웹 서버를 구축하여 배포할 수 있습니다.

- MVC 패턴
- restful한 API
- 에러헨들러 사용
- flask LoginManager, flask-Login
- flask session
- flask decorator
- flask-WTF(폼)
- flask-Mail
- git branch 활용

## 주요 기능

- 회원가입 기능

  - sqlalchemy를 활용하여 ORM 객체로 DB 저장
  - 비밀번호 암호화
  - 회원 가입 후 로그인 화면으로 이동
  - validation

- 로그인 기능

  - 회원 DB에 정보 가져오기
  - 비밀번호 확인 및 본인 인증
  - 로그인 후 로그인 유지 (Session에 정보 저장)

- 게시글

  - 작성 기능
  - 삭제 기능
  - 수정 기능

- 댓글 기능
- 팔로우 기능
- 좋아요 기능

## 화면구성

## API

- /home
- /feed
- /post

## 개발환경

- python 3.8
- Flask 2.0.1
- MySQL
- SQLAlchemy

## DB

## 테스팅 환경

postman

##
