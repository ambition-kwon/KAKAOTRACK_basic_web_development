# 2주차 학습내용

## IntelliJ IDEA를 이용한 Spring-boot Project만들기

- IntelliJ IDEA실행 -> New Project -> Spring Initializr선택 -> JDK(17이상)선택 -> Maven선택 -> Spring Web선택 -> Create -> Maven선택 후 새로고침(자동 install)
- src/main/java/com.example.demo에 새로운 클래스 생성(RestController.java) -> 아래의 코드 작성

~~~java
package com.example.demo;

import org.springframework.web.bind.annotation.RequestMapping;

@org.springframework.web.bind.annotation.RestController //중요
public class RestController {
    @RequestMapping //중요
    public String Test(){
        return "Hello, World!";
    }
}
~~~

- [localhost:8080](localhost:8080)접속하여 "Hello, World!"출력 확인

> **Maven** : 프로젝트를 위해 작성한 Java코드나 여러 자원들(.xml, .jar, .properties)를 JVM이나 톰캣같은 WAS가 인식할 수 있는 구조로 패키징 하는 과정, 테스팅, 검사, 배포까지 일련의 작업들을 통틀어 빌드라고 하는데, Maven은 자바언어에 대한 프로젝트 관리도구로 빌드툴(build tool)이라고 한다.



## IntelliJ IDEA를 이용한 HTML Project만들기

- IntelliJ IDEA실행 -> New Project -> HTML선택 -> Create -> 오른쪽 아래 `Run npm install`클릭(만약 node가 설치 되어있지 않다면 에러) -> index.html파일 선택 -> Hello world! This is HTML5 Boilerplate. 부분을 Hello world!로 수정 -> Run -> 결과출력 확인



