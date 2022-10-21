## **■서론**

Mysql이란, 현재 전 세계적으로 가장 많이 쓰이는 DBMS이다. Oracle사에서 관리하고 있으며, 데이터베이스를 관리하거나 자료를 관리하기 위한 언어이다. 원래 GUI를 통해 CLI환경을 대신 할 수 있는 툴은 없었지만, Oracle사에 의해 Mysql Workbench라는 프론트엔드 툴이 개발되어 현재는 개발자의 성향과 주어진 환경에 맞게 GUI / CLI 중 선택 혹은 동시에 사용할 수 있다. GUI툴인 Mysql Workbench 사용법에 대해 간략히 정리해 보고자 한다.





## **■본론**

\- 데이터베이스를 관리하기 위해 Mysql Workbench를 이용하고자 할 때, 가장 먼저 할 일은 Mysql언어를 설치하는 것이다. Mysql Workbench는 단지 Mysql언어를 쉽게 다룰 수 있도록 GUI환경을 제공해주는 툴로서 Mysql언어가 설치되어 있지 않다면 사용할 수 없다.

●Windows : Mysql홈페이지에서 Mysql언어와 GUI툴인 Workbench를 한 번에 다운 받을 수 있다.

●MAC OS : 일반적으로 Homebrew(패키지 관리자)를 통해 Mysql언어를 먼저 다운 받고, Mysql홈페이지에서 GUI툴인 Workbench를 다운받아 사용한다.



\- 현재 내 개발환경은 MAC OS이기 때문에 이 환경에 맞춰 기술하고자 한다. Windows와 달리 MAC OS는 Workbench 프로그램을 실행시키고 ‘Local instance 3306’에 접속해도 자동으로 서버가 실행되지 않는다. 서버를 동작시키는 방법 2가지는 아래와 같다.

●CLI : mysql.server start

●GUI : Administaration – ISTANCE – Startup / Shutdown - ‘Start Server’



\- 참고 : 서버 관련 명령어

| mysql.server start   | Mysql Local Host 서버를 시작   |
| -------------------- | ------------------------------ |
| mysql.server stop    | Mysql Local Host 서버를 중단   |
| mysql.server restart | Mysql Local Host 서버를 재시작 |





\- 서버를 정상적으로 동작시키고 가장 먼저 해야할 것은 TABLE을 만들기 위한 DATABASE를 생성하는 것이다. Mysql Workbench에선 이를 ‘Schema’라고 부르는데, 이를 생성하는 방법은 다음과 같다.

●화면 상단 원통형 모양 클릭(Schema Editor) – Schema Name입력(madang) – Apply – Apply

● CREATE DATABASE madang;



\- DATABASE를 성공적으로 생성하였다면, 방금 생성한 DATABASE를 사용하겠다고 프로그램 상에서 지정해 줘야 한다. 방법은 다음과 같다.

●화면좌측 Schemas – madang 오른쪽 클릭 – Set as Defualt Schema

●use madang;



\- 다음으로 해야 할 것은 사용하기로 지정한 madang DATABASE에 TABLE을 만드는 것이다. 방법은 다음과 같다.(Table name : book)

●Schemas – madang 아래 화살표 클릭 – Tables오른쪽 클릭 – Create Table... - Name : 테이블 명 - Column Name 및 Datatype, 각종 설정 지정 - Apply

●CREATE TABLE 테이블명(Colum Name Datatype 각종 설정);



\- Mysql의 Datatype에는 여러 가지가 있으나, 실습을 하면서 많이 쓰이는 type은 대표적으로 아래와 같다. 이 중 CHAR와 VARCHAR의 차이는 구분 해 놓도록 하자.

| **INT(INTEGER)** | 정수형 데이터를 저장                                         |
| :--------------- | ------------------------------------------------------------ |
| **VARCHAR**      | **가변길이**로 문자열을 저장                                 |
| **CHAR**         | **고정길이**로 문자열을 저장                                 |
| **TEXT**         | 긴 글을 저장 시 사용, 수백 자 이내의 문자열은 VARCHAR, 이상은 TEXT |
| **DATATIME**     | 날짜와 시간정보를 저장                                       |





\- 명령어 문을 실행했음에도 Schemas상에 아무런 변화가 없다면 좌측 상단에 있는 ‘Refresh Icon’을 클릭하여 새로고침 해 주면 된다(명령어의 실행에 오류가 있던 것이 아님).



\- 내가 생성한 TABLE에 대해 GUI적으로 보고 싶다면 두 가지 방법 중 하나를 선택하여 동작시키면 된다. 방법은 다음과 같다.

●Schemas – madnag – Tables – book 좌측클릭 – 회색으로 강조 된 부분에서 맨 오른쪽 표 모양 Icon클릭

●SELECT * FROM book;



\- 내가 생성한 TABLE의 설정을 변경하고 싶다면 두 가지 방법 중 하나를 선택하여 동작시키면 된다. 방법은 다음과 같다.

●Schemas – madnag – Tables – book 좌측클릭 – 회색으로 강조 된 부분에서 중간지점 스패너 모양 Icon클릭

●ALTER TABLE book(~~~~);



\- Mysql Workbench를 설치하고 이용하다 보면 가장 먼저 드는 생각은 명령어를 입력할 때 Font의 크기가 너무 작아 가시적이지 못하다는 것이다. 이를 해결하기 위한 방법은 다음과 같다.

●Edit – Preferences – Font & Colors – SQL Editor 부분 변경



\- Mysql언어를 사용하는 이유는 수천, 수만 혹은 우리가 생각하는 것 이상의 데이터를 처리하는 효율에 그 의미가 있다. 때문에 내가 만든 DATABASE가 얼마나 효율적으로 동작하는지 개발자는 확인해야하는 의무가 있고, 이를 편리하게 확인하는 방법역시 Mysql Workbench는 제공하고 있다. 방법은 다음과 같다.

●Administration – PERFORMANCE – Dashboard







## **■결론 및 느낀 점**



데이터베이스 수업시간에 학습하면서, 그리고 이번 레포트를 작성하면서 공통적으로 느낀 것은 Mysql Workbench는 ‘다양함에 사용자를 현혹시키지 않고 정말 필요한 기능만 구현했구나’ 였다. 보통 프로그램들을 사용하다 보면 사용 하면서도 내가 모르는 기능들이 넘치기 마련인데, Mysql Workbench같은 경우 효율을 중시하는 개발자들이 사용하는 Tool이라 그런지 Essential하게 프로그램이 구성되어 있다는 점을 느꼈다.

Mysql Workbench를 이용한다면 명령문을 하나도 모르는 상태로도 데이터베이스를 관리할 수 있다는 생각이 들었다. 하지만 GUI환경 말고 CLI환경에서도 데이터베이스를 동작시키고 수정할 줄 알아야 한다고 생각한다. 개발자는 항상 본인이 원하는 Homeground환경에서만 개발을 해야 하는 것이 아니기 때문이다. 특히 Database와 같은 BACKEND는 더 더욱이 말이다.