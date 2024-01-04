# Lombok

어노테이션 기반으로 코드를 **자동완성** 해주는 라이브러리
Getter, Setter, Equals, ToString과 같은 코드를 자동완성 시킬 수 있다.

Java를 이용해 아래와 같은 클래스를 생성했다.

```java
public class Student {

    private String name;
    private int age;
    private String address;

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public int getAge(){
        return age;
    }

    public void setAge(int age){
        this.age = age;
    }

    public String getAddress(){
        return address;
    }

    public void setAddress(String address){
        this.address = address;
    }
}
```

Lombok을 통해 위의 코드를 아래와 같이 간단하게 바꿀 수 있다.

```java
@Getter
@Setter
public class Student {
    private String name;
    private int age;
    private String address;
}
```

---

## Lombok의 장점

- 어노테이션 기반의 코드 자동 생성을 통한 **생산성 향상**
- **반복되는 코드를 줄여** 가독성 및 유지보수성을 향상
- 빌더 패턴이나 로그 생성 등 다양한 방면에서 활용 가능

## Lombok 기능

##### [ @Getter @Setter ]
클래스 이름 위에 적용 시 모든 변수에 적용이 가능하고, 변수 이름 위에 적용 시 해당 변수들만 적용이 가능

##### [ @Data ]
getter(), setter(), equals(), hasCode(), toString() 메서드를 사용하게 해준다.
_@Getter @Setter @toString @EqualsAndHashCode @RequiredArgsConstructor 자동생성_

##### [ @AllArgsConstructor ]

모든 인자를 가지는 생성자 구성
Ex. 아래와 같은 코드를 자동완성 시켜준다.

```java
public Student(String name, int age, String address){
    this.name = name;
    this.age = age;
    this.address = address;
}
```

##### [ @NoArgsConstructor ]
인자가 없는 생성자 구성
```java
public Student(){

}
```

##### [ @RequiredArgsConstructor ]
필수 인자를 가지는 생성자 구성
  
---
해당 Lombok을 사용하기 위해 Spring에서 다운을 받았지만, 현재 사용 중인 Intellij ultimate 버전에서는 스프링부트 파일 생성 시 간단한 설정을 통해 사용 가능하다.