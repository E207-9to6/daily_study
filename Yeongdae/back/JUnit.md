### JUnit

#### TDD
- 테스트 주도 개발
- 테스트를 먼저 설계 및 구축 후 테스트를 통과할 수 있는 코드를 작성하는 것
- 애자일 개발 방식 중 하나
    - 코드 설계시 원하는 단계적 목표에 대해 설정하여 진행하고자 하는 것에 대한 방향의 갭을 줄이고자 함.
    - 최초 목표에 맞춘 테스트를 구축하여 그에 맞게 코드를 설계하기 때문에 보다 적은 의견 충돌을 기대할 수 있음.

- 코드의 안정성 향상
- 기능을 추가하거나 변경하는 과정에서 발생할 수 있는 Side-Effect를 줄일 수 있음.
- 해당 코드가 작성된 목적을 명확하게 표현할 수 있음.

*애자일 개발 방식 : 


#### JUnit

- Test Framework
- 단위 테스트(Unit Test)를 위한 도구를 제공
    - 코드의 특정 모듈이 의도된 대로 동작하는지 테스트 하는 절차를 의미
    - 모든 함수와 메소드에 대한 각각의 테스트 케이스를 작성하는 것
- Annotation을 기반으로 테스트를 지원
- Assert로 테스트 케이스의 기대값에 대한 수행 결과를 확인
- Jupiter, Platform, Vintage 모듈로 구성
    - JUnit Jupiter
    - JUnit Platform
    - JUnit Vintage


##### JUnit LifeCucle Annotation

@Test
@BeforEach
@AfterEach
@BeforeAll
@AfterAll

##### JUnit Main Annotation

@SpringBootTest
@ExtendWith
@WebMVCTest(.class)
@MockBean
@AutoConfigureMockMvc
@Import


#### 통합 테스트


#### 단위 테스트
