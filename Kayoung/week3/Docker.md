# Docker
**컨테이너 기반의 오픈소스 가상화 플랫폼**
- 컨테이너: 격리된 공간에서 프로세스가 동작하는 기술. 가상화 기술 중 하나
  ![image](https://github.com/E207-9to6/daily_study/assets/68316096/f10ff68d-3e60-455b-aa0a-fee7513ef0df)
  
  - 기존의 가상화 방식: OS를 가상화(VMWare, VirtualBox..)
    - 호스트 OS 위에 게스트 OS 전체를 가상화  
 
  - 프로세스 격리 방식: 단순히 프로세스를 격리시키기 때문에 가볍고 빠름. 프로세스가 필요한 만큼만 CPU, 메모리를 추가로 사용

- 이미지: 컨테이너 실행에 필요한 모든 것(코드, 시스템 라이브러리, 설정 등)을 포함하고 있는 것  
  - 컨테이너를 실행하기 위한 모든 정보를 가지고 있음  

  - Docker hub에 등록하거나 Docker Registry 저장소를 직접 만들어 관리
 
  - `docker build -t docker-example:0.0.1`
    - `build` 명령어는 Dockerfile를 읽어서 docker 데몬이 실행을 순차적으로 진행

- Dockerfile
  - 도커 이미지를 만들기 위해 Dockerfile 파일에 DSL(Domain Specific Language)로 이미지 생성 과정을 작성
 
  - `docker build` 명령어를 통해서 Docker가 Dockerfile를 읽고 자동으로 docker image를 빌드한다

  - Dockerfile은 최상위 루트 프로젝틑 경로에 위치하며 파일 이름은 `Dockerfile`이다
  
  - 예시
    ```
    FROM adoptopenjdk/openjdk11
    CMD ["./mvnw", "clean", "package"]
    ARG JAR_FILE_PATH=target/*.jar
    COPY ${JAR_FILE_PATH} app.jar
    ENTRYPOINT ["java", "-jar", "app.jar"]
    ```
  - 반드시 `FROM`으로 시작  
    - adoptopenjdk/openjdk11 버전을 pull받는다  
  - `CMD`는 한 번만 사용  
    - mvnw(maven wrapper)로 프로젝트 빌드  
  - `ARG(Argument)`: 변수 JAR_FILE_PATH에 `target/*.jar`의 경로를 저장
  - `COPY`: 위에서 할당한 변수명을 app.jar 이름으로 복사
  - `ENTRYPOINT`: java를 실행하는 parameter

- Dockerfile vs Docker image vs Docker Container
  ![image](https://github.com/E207-9to6/daily_study/assets/68316096/87ead10c-7f83-4f3c-8559-1b889e5057bc)
  - image는 container의 설계도. container는 image를 실행시켜야 존재할 수 있다.  
  - image는 한번만 생성하나, 같은 이미지로부터 다수의 컨테이너 생성 가능  
  - Dockerfile는 image를 빌드하는 데 필요한 명령어를 순서대로 기술한 텍스트 파일  

- Docker Hub
  - Docker 이미지 저장소 서비스
 
  - 소프트웨어 공급업체, 오픈 소스 프로젝트 및 커뮤니티에서 컨테이너 이미지 제공

- Docker Registry
  - 도커 이미지를 사용자들끼리 공유할 수 있는 플랫폼  
  
  - Public, private 레지스트리로 나뉨  

![image](https://github.com/E207-9to6/daily_study/assets/68316096/055d8339-6e02-49d7-93cb-ef2e6ebb5efd)  



[초보를 위한 도커 안내서 - 도커란 무엇인가?](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
[Dockerfile reference](https://docs.docker.com/engine/reference/builder/)  
[스프링부트 프로젝트 도커허브 이미지 빌드(feat. 인텔리제이)](https://devmango.tistory.com/180)
  
