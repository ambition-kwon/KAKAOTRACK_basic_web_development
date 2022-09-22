# 2주차 학습내용

## IntelliJ IDEA를 이용한 Spring-boot Project만들기(수업시간 복습)

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



## IntelliJ IDEA를 이용한 HTML Project만들기(수업시간 복습)

- IntelliJ IDEA실행 -> New Project -> HTML선택 -> Create -> 오른쪽 아래 `Run npm install`클릭(만약 node가 설치 되어있지 않다면 에러) -> index.html파일 선택 -> Hello world! This is HTML5 Boilerplate. 부분을 Hello world!로 수정 -> Run -> 결과출력 확인



## IntelliJ IDEA 단축키 정리(수업시간 복습)

- `cmd+1` : 왼쪽 메뉴바(프로젝트 뷰) 숨김 ON/OFF
- `shift+shift` : 만능 단축키(전체 검색창 : 뭐든지 검색 가능하고, 실행할 수도 있음)
- `cmd+n` : 새 파일 추가
- `cmd+w` : 현재 창(탭) 닫기
- `cmd+o` : 파일 네비게이션(shitf+shitf랑 같은 창 띄우지만 focus가 class로 가 있음)
- `cmd+e` : 최근 파일 보기(단순 파일 이외에도, Git, Commnad line tool 등 여러개 선택가능)
- `cmd+f` : 특정 단어 찾기
- `//todo ` : todo로 주석입력시, 추후에 본인이 해야할 일 확인 가능
- IDEAVIM : vim을 IntelliJ에서 사용할 수 있도록 도와주는 plugin
- Key promoto X : 모든 행위에 있어 사용가능한 단축키가 있다면 pop-up시켜주는 plugin
- `option+enter` : 자동수정기능(bug발생시 ide로 하여금 해결 가능한 오류면(ex.문법) 바로 버그 찾아서 변경 해줌)
- `cmd+/` : 라인 단위로 주석처리
- `cmd+r` : 찾아서 변경(replace)
- `esc` : focusing이 어디에 있던, code editing 진행중인 창으로 이동시킴
- `cmd+b` : 어떠한 변수 or 함수가 선언된 위치로 이동할 수 있음
- **editor에서 사용 가능한 단축키는 대다수 vim으로 대체할 수 있으므로 정리하지 않음**



















