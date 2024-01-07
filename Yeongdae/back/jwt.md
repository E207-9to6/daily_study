### spring security jwt

*Spring Security는 Spring에서 인증, 인가 등의 기능을 지원하는 보안 프레임워크.

#### JWT(Json Web Token)

##### 개념
- Json 포맷을 이용하여 사용자에 대한 속성을 저장하는 Claim 기반의 Web Token이다.
- 토큰 자체를 정보로 사용하는 Self-Contained 방식으로 정보를 안전하게 전달한다.

##### 구조
- Header, Payload, Signature의 3 부분으로 이루어진다.
- 각 부분은 Base64Url로 인코딩 되어 표현되며, 각각의 부분을 이어 주기 위해 . 구분자를 사용한다.

- Header
    - 토큰의 헤더는 typ과 alg 두 가지 정보로 구성된다.
    - alg는 헤더(Header)를 암호화 하는 것이 아니고, Signature를 해싱하기 위한 알고리즘을 지정하는 것이다.
        - typ : 토큰의 타입을 지정 ex) JWT
        - alg : 알고리즘 방식을 지정하며, 서명(Signature) 및 토큰 검증에 사용 ex) HS256(SHA256) 또는 RSA

- Payload
    - 토큰의 페이로드에는 토큰에서 사용할 정보의 조각들인 클레임(Claim)이 담겨 있다. 
    - 클레임은 총 3가지로 나누어지며, Json(Key/Value) 형태로 다수의 정보를 넣을 수 있다.
        - 등록된 클래임(Registered Claim)
            - 토큰 정보를 표현하기 위해 이미 정해진 종류의 데이터들
        - 공개 클레임(Public Claim)
            - 사용자 정의 클레임으로, 공개용 정보를 위해 사용
            - 충돌 방지를 위해 URI 포맷을 이용
        - 비공개 클레임(Private Claim)
            - 사용자 정의 클레임으로, 서버와 클라이언트 사이에 임의로 지정한 정보를 저장

- Signature
    - 토큰을 인코딩하거나 유효성 검증을 할 때 사용하는 고유한 암호화 코드.
    - Header와 Payload의 값을 각각 BASE64Url로 인코딩하고, 인코딩한 값을 비밀 키를 이용해 Header에서 정의한 알고리즘으로 해싱을 하고, 이 값을 다시 BASE64Url로 인코딩하여 생성한다.

생성된 토큰(JWT)은 HTTP 통신을 할 때 Authorization이라는 key의 value로 사용된다.

##### 특징
- 토큰 자체에 정보를 담고 있으므로 보안상 취약할 수 있다.
- Payload가 암호화된 것이 아니라 인코딩 된 것이므로 중요 데이터를 넣지 않거나 JWE로 암호화 하여야 한다.
- Stateless : 상태를 저장하지 않기 때문에 생성 후 제어가 불가능하다. 토큰 만료 시간을 꼭 넣어주어야 한다.
- 정보가 많아질수록 토큰의 길이가 늘어나 네트워크에 부하를 줄 수 있다.




