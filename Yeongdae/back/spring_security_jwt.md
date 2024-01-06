### Spring Security JWT


#### 의존성

- Gradle
```
dependencies {
    ...

    //security
    implementation 'org.springframework.boot:spring-boot-starter-security'
    
    //jwt
    implementation("io.jsonwebtoken:jjwt-api:0.11.5")
    runtimeOnly("io.jsonwebtoken:jjwt-impl:0.11.5")
    runtimeOnly("io.jsonwebtoken:jjwt-jackson:0.11.5")
    ...
}
```

#### .



##### JWT Setting
- SecurityConfig
    - SecurityFilterChain
        - Request를 사용하는 요청들에 대해 접근제한 설정

- TokenProvider
    - 추가된 라이브러리를 사용해서 jwt를 생성하고, 검증하는 컴포넌트
    - Token 생성
    - Token -> Claim -> User -> Authentication
    - 토큰의 유효성 검증

- JwtAuthenticationEntryPoint
    - 유효한 자격증명을 제공하지 않고 접근하려 할떄 401 Unauthorized 에러를 리턴하는 클래스

- JwtAccessDeniedHandler
    - 필요한 권한이 존재하지 않는 경우에 403 Forbidden 에러를 리턴하는 클래스

- JwtFilter
    - .

- JwtSecurityConfig
    - 

##### config
- data.sql
    - server h2-db 기초 data sql
- application.yml
    - h2-db, jpa, jwt 설정

##### 외
- UserDto
    - Annotation으로 NotNulll, Size(min, max) 설정이 가능하네요 ㅎㄷ






