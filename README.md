# DRF-for-rental-brokerage-service-in-gachon
Django로 제작한 교내 물품 대여 중개 웹 DRF입니다.

## BaroBorrow
교내 물품 대여 중개 웹으로 교내 지역에 따라 대여 희망 글 작성 가능.


## 사용법
    pip install -r requirements.txt
    python manage.py runserver 

## API

### 로그인, 회원가입

#### 로그인
    http://127.0.0.1:8000/users/login/
> 액션 : post

> 형식 :
> {
> "username" ,
> "password" 
> }

> 반환 : 
> {
> "token",
> "userid"
> }

#### 회원가입
    http://127.0.0.1:8000/users/register/
> 액션 : post

> 형식 :
> {
"username",
"email",
"password",
"password2"
> }


### 장소별 게시글 페이지

#### 장소별 게시물 가져오기
    http://127.0.0.1:8000/posts/?location=장소이름
> 액션 : get

> 반환 :
> [
{
"pk",
"profile": {
"nickname",
"borrow_cnt",
"lend_cnt",
"image"
},
"title",
"category",
"body",
"location",
"deadline_date",
"return_date",
"published_date",
"done"
}
> ]

#### 기관의 대여 물품 등록
    http://127.0.0.1:8000/council_posts/
> 액션 : post

> 헤더 : 토큰

> 형식 :
> {
"council",
"title",
"category",
"location",
"remaining_cnt"
> }

#### 기관의 대여 물품 수정
    http://127.0.0.1:8000/council_posts/물품 아이디/
> 액션 : put

> 헤더 : 토큰

> 형식 :
> {
"council",
"title",
"category",
"location",
"remaining_cnt"
> }

#### 기관의 대여 물품 정보 가져오기
    http://127.0.0.1:8000/council_posts/?location=장소이름
> 액션 : get

> 반환 :
> [
{
"pk",
"council",
"title",
"category",
"location",
"remaining_cnt"
}
> ]

### 대여 글

#### 대여 글 생성
    http://127.0.0.1:8000/posts/
> 액션 : post

> 헤더 : 토큰

> 형식 :
> {
"title",
"category",
"body",
“location”,
“deadline_date”,
“return_date”
> }

#### 대여 글 수정
    http://127.0.0.1:8000/posts/대여 글 아이디/
> 액션 : put

> 헤더 : 토큰

> 형식 :
> {
"title",
"category",
"body",
“location”,
“deadline_date”,
“return_date”
> }

#### 대여 글 가져오기
    http://127.0.0.1:8000/posts/대여 글 아이디/
> 액션 : get

> 형식 :
> {
"pk",
"profile": {
"nickname",
"borrow_cnt",
"lend_cnt",
"image"
},
"title",
"category",
"body",
"location",
"deadline_date",
"return_date",
"published_date",
"done"
> }

### 대여 글의 댓글

#### 대여글의 댓글 작성
    http://127.0.0.1:8000/comments/
> 액션 : post

> 헤더 : 토큰

> 형식 :
> {
"postid",
"text"
> }

#### 대여글의 댓글 수정
    http://127.0.0.1:8000/comments/댓글 아이디/
> 액션 : put

> 헤더 : 토큰

> 형식 :
> {
"postid",
"text"
> }


#### 대여글의 댓글 가져오기
    http://127.0.0.1:8000/comments/?post=대여 글 아이디 
> 액션: get

> 반환 :
> [
{
"pk",
"council",
"title",
"category",
"location",
"remaining_cnt"
}
> ]

#### 대여 완료하기
    http://127.0.0.1:8000/comments/done/댓글작성자 아이디/댓글 아이디
> 액션: get

> 헤더 : 토큰

> 형식:
대여글 작성자만 접근 가능.
게시물 작성자면 done 반환
> 아니라면 nope 반환

> 설명 : 게시글 작성자는 빌린횟수 증가, 댓글 작성자는 빌려준 횟수 증가

### 마이페이지

#### 유저 프로필 가져오기
    http://127.0.0.1:8000/users/profile/유저 아이디
> 액션: get

> 반환 :
> [
{
"nickname",
"borrow_cnt",
"lend_cnt",
"image"
}
> ]

#### 유저 글 가져오기
    http://127.0.0.1:8000/posts/?author=유저 아이디
> 액션: get

> 반환 :
> [
{
"pk",
"profile": {
"nickname",
"borrow_cnt",
"lend_cnt",
"image"
},
"title",
"category",
"body",
"location",
"deadline_date",
"return_date",
"published_date",
"done"
}
> ]

#### 유저 댓글 가져오기
    http://127.0.0.1:8000/comments/?writer=유저 아이디
> 액션: get

> 반환 :
> [
{
"pk",
"postid",
"profile": {
"nickname",
"borrow_cnt",
"lend_cnt",
"image"
},
"text",
"created_date"
}
> ]

#### 닉네임 수정
    http://127.0.0.1:8000/users/profile/유저 아이디
> 액션 : put

> 헤더 : 토큰

> 형식 :
> {
"nickname"
> }
