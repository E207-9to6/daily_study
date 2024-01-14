# Client & Server
## 1. Client
서버로 요청을 보내는 모든 프로그램  
ex. 웹 브라우저

## 2. Server
클라이언트의 요청을 받아 처리하는 주체  
클라이언트가 데이터를 요청 시 데이터를, 서버 내 처리를 요청 했다면 해당 요청만 처리한다.

# DataBase
여러 사람이 데이터를 같은 곳에 모아두고 여러 사람이 사용할 목적으로 관리하는 데이터 저장소  
**데이터 베이스 관리 시스템**: MySQL, oracle, postgreSQL  

### RDB (Relation Database)
데이터를 행과 열로 이루어진 테이블로 관리하며, 기본키를 사용해 각 행을 식별하고, 테이블 간 관계를 지을 수 있다.  
ex. oracle, MySQL, SQL server, postgreSQL

### NoSQL (Not Only SQL)
RDB는 데이터 저장, 질의, 수정, 삭제가 용이하지만 성능을 올리는 것이 어려움.  
NoSQL은 데이터 모델링을 어떻게 하느냐에 따라 다이나모디비, 카우치베이스, 몽고디비와 같은 다양한 DB가 존재한다.

# Library & FrameWork
## 1. Library
클래스, 함수 등을 모아놓은 코드의 모음  
독립적이기 때문에 다른 라이브러리끼리 영향을 주지 않는다.

## 2. Framework
애플리케이션을 개발할 때 전체적인 구조를 잡기 위해 사용하는 도구  
정해진 틀에서 개발해야 한다는 단점이 있지만, 개발 효율이 높다.

# Java Annotation
잦바로 작성한 코드에 추가하는 주석  
다양한 목적으로 사용하지만 보통 메타 데이터로 사용하는 경우가 많다.  
ex. @Override, @Deprecated, @SuppressWarnings
