# Database-mid

# 1장

- `데이터베이스`: 여러 사람들이 공유하고 사용할 목적으로 통합/관리되는 데이터들의 모임
- **데이터베이스의 개념(4가지)**
    - `통합된 데이터` : 여러 곳에서 사용하던 데이터를 통합하여 하나로 저장한 데이터를 의미한다. 각자 사용하던 데이터의 중복성을 최소화는 것이 가장 중요하다.
    - `저장된 데이터` : 디스크, 테이프 같은 실제 컴퓨터 저장장치에 저장된 데이터를 의미한다.
    - `운영데이터` : 업무를 위해 / 조직의 운영을 위해 사용되는 데이터를 의미한다.
    - `공용데이터` : 공동으로 사용하는 데이터를 의미한다.

- **데이터베이스의 특징(4가지)**
    - `실시간 접근성` : 데이터베이스는 실시간으로 서비스된다. 사용자가 데이터를 요청하면 수초 내에 결과를 서비스한다.
    - `계속적인 변화` : 데이터베이스에 저장된 내용은 시간에 따라 항상 바뀐다.
    - `동시 공유` : 데이터베이스는 여러 사용자에게 동시에 공유된다. 접근하는 사용자 데이터 요청 프로그램이 동시에 여러 개 있다는 의미이다.
    - `내용에 따른 참조` : 데이터베이스에 저장 된 데이터는 물리적인 위치가 아니라 내용에 의해 참조된다.(어떤 데이터가 어떤 메모리 주소에 저장되어있는 지 몰라도 검색시 원하는 결과를 얻을 수 있다)

- **데이터베이스 시스템의 구성(3개)**
    - `DBMS` : 사용자-데이터베이스 연결시켜주는 소프트웨어로 주기억장치에 상주한다.
    - `데이터베이스` : 데이터를 모아둔 토대를 말한다. 컴퓨터 내부의 하드디스크에 저장된다.
    - `데이터 모델` : 데이터가 저장되는 기법에 관한 내용으로, 눈에 보이지 않는 논리적인 개념이다.

- **데이터베이스 언어의 종류(3개)**
    - `DDL` : 데이터 정의어 → CREATE, ALTER, DROP
    - `DML` : 데이터 조작어 → SELECT, INSERT, DELETE, UPDATE
    - `DCL` : 데이터 제어어 → GRANT, REVOKE
    
- **데이터베이스 사용자(4가지)**
    - `일반 사용자` : 응용 프로그래머가 작성한 프로그램을 이용하는 사람, 자신이 DBMS를 이용하는지 모른다
    - `응용 프로그래머`(데이터베이스 프로그래머) : 일반사용자가 사용할 수 있도록 프로그램을 만드는 사람, SQL + Programming language를 사용하여 개발함
    - `SQL 사용자` : 응용프로그램으로 구현되어 있지 않은 업무를 SQL을 이용하여 처리한다
    - `데이터베이스 관리자`(DBA) : 데이터베이스 시스템을 총괄하는 사람이다. 보통 데이터베이스 마다 한명씩 둔다

- **DBMS의 구성**
    - `DDL Compiler` : SQL 번역
    - `DML Compiler` : SQL 번역
    - `Embedded DML Compiler` : 응용 프로그램 내의 SQL을 번역
    - `질의처리기` : 번역된 SQL을 처리하는 알고리즘

- **데이터 모델(5개)** : 데이터베이스에 데이터가 어떻게 구조화 되어 저장되는지를 결정
    - `계층 데이터 모델(포인터)` : 프로그램 속도 빠르다, 프로그래밍 어려워 개발 느리다
        
        ![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled.png)
        
    - `네트워크 데이터 모델(포인터)` : 프로그램 속도 빠르다, 프로그래밍 어려워 개발 느리다
    - `객체 데이터 모델(오브젝트 아이디)` : 강좌를 객체 개념으로 보고, 강좌에 대한 oid를 학생 테이블에 저장하는 방법
        
        ![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%201.png)
        
    - `관계 데이터 모델(속성 값)` : 속도 조금 느림, 프로그래밍 쉬움, 대부분 이거 사용, 강좌 번호를 학생 데이터에 직접적으로 저장하는 방법
        
        ![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%202.png)
        
    - `객체-관계 데이터 모델` : 객체지향 언어가 널리 보급됨에 따라 관계/객체 데이터 모델 중 장점만을 결합한 모델

- **스키마(Schema)** : 그리스어에서 유래된 단어로 구조를 의미함

- `ANSI의 3단계 데이터베이스 구조`(**특징 : 데이터 독립성)**
    
    ![필수암기](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%203.png)
    
    필수암기
    
    - `외부단계` : 일반사용자/응용 프로그래머 접근하는 계층, 외부 스키마(서브 스키마) 여러개
    - `개념단계` : 전체 데이터베이스의 정의를 의미, 개념 스키마 한개, DBA가 관리,
    - `내부단계` : 물리적 저장장치에 실제로 저장되는 방법을 표현, 내부 스키마 한개, 물리적인 구조를 뜻함
    - `외부/개념 매핑(사상)` : 외부 스키마의 데이터가 개념 스키마의 어떤 부분에 해당되는지 대응
    - `개념/내부 매핑(사상)` : 개념 스키마의 데이터가 내부 스키마의 물리적 장치 어디에 어떤 방법으로 저장되는지 대응

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%204.png)

- **데이터 독립성(3단계 데이터베이스 구조의 특징)** : 한 단계 내의 변경에 대해 다른 단계와 간섭이 없음
    - `논리적 데이터 독립성` : `외부-개념` 사이의 독립성, 논리적 구조가 변경되어도 응용 프로그램에는 영향이 없음
    - `물리적 데이터 독립성` : `개념-내부` 사이의 독립성, 물리적 저장장치를 재구성해도 개념 스키마에 영향이 없다.
    - 구현 난이도 : 논리적 데이터 독립성 <<< 물리적 데이터 독립성
    
    ---
    

# 2장

- 릴레이션(relation) : 행과 열로 구성된 테이블
- 릴레이션
    
    ![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%205.png)
    
    - 릴레이션 스키마 : 테이블 첫 행(헤더), 속성, 자료 타입, 어떤 정보가 담길지를 정의
        - 속성(attribute) : 각 열
        - 차수(degree) : 열의 갯수(속성의 갯수)
        - 도메인(domain) : 각 열이 가질 수 있는 데이터 타입
    - 릴레이션 인스턴스 : 릴레이션 스키마에 실제로 저장된 데이터의 집합
        - 투플(tuple) : 각 행
        - 카디날리티(cardinality) : 투플의 수(행의 수)(수시로 변한다)
    
- 릴레이션의 특징(6가지)
    - 속성은 단일 값을 가진다 : 도메인 = {혁원, 안녕, 잘가}일 경우 {혁원, 잘가}와 같이 한번에 여러개의 값을 가질 수 없다.
    - 속성은 서로 다른 이름을 가진다
    - 한 속성의 값은 모두 같은 도메인을 가진다
    - 속성의 순서는 상관없다 : (주소, 이름) == (이름, 주소)
    - 투플의 순서는 상관없다
    - 중복된 투플은 허용하지 않는다

---

![실습예제](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%206.png)

실습예제

| 고객번호 | 유일 식별 가능 |
| --- | --- |
| 주민번호 | 유일 식별 가능 |
| 주소 | 가족끼리 같으므로 유일 식별 불가능 |
| 이름 | 동명이인 존재하므로 유일 식별 불가능 |
| 핸드폰 | 핸드폰 없는사람이 있으므로 유일 식별 불가능 |

- 키(key) : 특정 투플을 식별할 때 사용된다 / 릴레이션간의 관계를 맺는데에도 사용된다
    - 슈퍼키 : 투플을 유일하게 식별할 수 있는 `하나의 속성 혹은 속성의 집합을` 말한다.
        - 고객릴레이션에서 : 만약 고객번호와 주민번호 하나의 속성만으로도 투플 식별이 가능하다고 가정하면, 고객번호 혹은 주민번호가 속한 모든 키 집합은 수퍼키라고 말할 수 있다(ex. (고객번호), (고객번호, 이름), (고객번호, 이름, 주소))
        - 주문릴레이션에서 : (고객번호, 도서번호)를 포함한 모든 속성집합이 슈퍼키이다
    - 후보키 : 투플을 유일하게 식별할 수 있는 속성의 `최소집합`
        - 고객릴레이션에서 : (고객번호), (주민번호)
        - 주문릴레이션에서 : (고객번호, 주민번호) → 복합키 (단, 한명의 고객이 동일한 도서 구입X)
    - 기본키 : 여러 후보키 중 하나를 선정하여 대표로 삼는 키(NULL허용X)(중복X)
        - 고객릴레이션에서 : 둘 중에 하나를 골라야 하는데, 주민번호와 같은 경우 개인정보보호에 취약하기 때문에 (고객번호)를 기본키로 삼는 것이 합리적이다.
        - 주문릴레이션에서 : (고객번호, 주민번호) 복합키 만이 유일하므로 저것이 기본키가 된다
    - 대체키 : 후보키 - 기본키
    - 대리키(인조키) : 기본키가 보안을 요하거나, 마땅한 기본키가 없을 경우 사용하며 일련번호, 주문번호같은 가상의 속성이 그 예이다, 사용자가 직관적으로 값의 의미를 알 수 없다.
    - 외래키 : 다른 릴레이션의 기본키를 참조하는 속성(특이한 경우로 자기자신의 기본키를 외래키로 삼을 수 도 있다)
        - 참조하는 릴레이션 : 자식 릴레이션(NULL허용)(중복허용)
        - 참조되는 릴레이션 : 부모 릴레이션(NULL비허용)(중복비허용)
            
            ![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%207.png)
            

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%208.png)

---

- 데이터 무결성 : 데이터베이스에 저장된 데이터의 일관성/정확성을 지키는 것
    - 학교에서 학생이 졸업했다고 학생 정보를 삭제해버리면 성적 및 수강 등 모든 관련 자료에 문제가 발생한다. 이와 같은 경우를 방지하기위해 데이터의 삽입, 수정, 삭제시 기본적인 제약조건을 DBMS가 알아서 지켜준다면 프로그래머의 부담이 줄지 않을까? → 무결성 제약조건
- 무결성 제약조건(3가지)(관계 데이터 모델 핵심개념 : 2,3번)
    - 도메인 무결성 제약조건 : 도메인 제약이라고 한다, 릴레이션 내 투플들이 각 속성의 도메인에 지정된 값만을 가져야 한다
    - 개체 무결성 제약조건 : 기본키 제약이라고 한다, 기본키는 NULL값을 가져서는 안된다, 릴레이션 내에 오직 한 개의 값만 즉, 같은 값이 존재해서는 안된다.
    - 참조 무결성 제약조건 : 외래키 제약이라고 한다, 자식릴레이션의 외래키는 부모릴레이션의 기본키와 도메인이 동일해야 한다.
        - (ex. 자식릴레이션의 외래키에 부모릴레이션의 기본키 도메인과 다른 값으로 넣으면 거부, 자식 릴레이션에서 참조되고 있는 값을 부모 릴레이션에서 삭제하려해도 거부)

💁‍♀️UNIQUE 제약조건 : 속성의 모든 값들에 서로 같은 값이 없어야 한다, NULL은 허용된다.

→ 개체 무결성 제약조건에서 NULL만 허용된 제약조건이라고 생각하자

---

- 관계대수 : 릴레이션에서 원하는 결과를 얻기 위해 수학의 대수와 같은 연산을 이용하여 질의하는 방법을 기술하는 언어이다
    - 단항 연산자 : 피연산자의 개수가 1개
    - 이항 연산자 : 피연산자의 개수가 2개
- 기본 관계대수 연산자(5개) : 셀렉션(σ)(단항), 프로젝션(π)(단항), 합집합(**∪**)(이항), 차집합(-)(이항), 카티전 프로덕트(X)(이항)
    - 나머지 연산자는 ‘유도’ 혹은 ‘추가’ 된 것이라고 생각하자

![기본 관계대수 연산자 예시, 조인을 유심히 볼것(카디전 프로덕트와 셀렉션으로 유도됨)](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%209.png)

기본 관계대수 연산자 예시, 조인을 유심히 볼것(카디전 프로덕트와 셀렉션으로 유도됨)

- 카티전 프로덕트(X) : 두 릴레이션을 하나로 합칠 때 사용하는 연산이다, 차수는 두 릴레이션 차수의 합이며, 카디널리티는 두 릴레이션 카디널리티의 곱이다
    - 두 릴레이션을 수평으로 합친 결과를 모조리 반환하기 때문에 결과가 의미가 없으며 유용한 자료로 사용하기 힘들다. 이때 셀렉션과 프로덕트 연산을 적절히 사용하면 의미있는 자료로 활용할 수 있다.
- 조인(**⋈**) : σ (릴레이션 X 릴레이션) == (릴레이션 **⋈** 릴레이션)
    - 세타조인(⋈θ) : 두 릴레이션 간 조건을 만족하는 릴레이션을 반환
    - 동등조인(⋈) : 두 릴레이션 간 같은 값을 가진 릴레이션을 반환
    - 자연조인(⋈N) : 두 릴레이션 간 같은 값을 가진 릴레이션에서 중복 속성을 제거하고 반환
        - 세미조인(⋉, ) : 자연조인 후, 닫힌쪽의 속성만 포함시키고 전부 제거(열 삭제), 속성 삭제하면 당연하지만 중복되는 것들이 생기는데, 중복되는 것들은 전부 1개씩만 남겨놓고 제거
        - 외부조인(⟕, ⟖, ⟗) : 자연조인시 조인에 실패한 투플을 모두 보여준다(왼쪽, 오른쪽, 완전) 대신 이때 NULL값을 채워서 반환한다.
            
            ![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2010.png)
            

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2011.png)

![실습해보자](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2012.png)

실습해보자

![실습해보자](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2013.png)

실습해보자

---

Q. 마당서점에서 판매하는 도서 중 8000원 이하인 도서를 검색하시오

: σ(price ≤ 8000)(book)

Q. 마당서점에서 판매하는 도서 중 8000원 이상이고 도서번호가 3이상인 도서를 검색하시오

: σ(price ≥ 8000 and bookid ≥ 3)(book)

Q. 신간도서 안내를 위해 (이름, 주소, 연락처)의 주소록을 만드시오

: π(name, address, phone)(customer)

Q. 고객 릴레이션과 주문 릴레이션의 카티전 프로덕트를 구하시오

: customer X orders

Q. 고객과 고객의 주문사항을 모두 보이시오

: customer ⋈θ(customer.custid = orders.custid) orders

: customer ⋈(customer.custid, orders.custid) orders

Q. 마당서점의 도서 중 가격이 8000원 이하인 도서이름과 출판사를 보이시오

: π(book, publisher)(σ(price ≤ 8000)(book))

Q. 마당서점A와 마당서점B의 도서 중 가격이 8000원 이하인 도서이름과 출판사를 보이시오

: π(book, publisher)(σ(price ≤ 8000)(A **∪ B))**

Q. 마당서점의 박지성 고객(고객정보)의 거래 내역(주문정보) 중 주문번호, 이름, 가격을 보이시오

: π(orderid, name, price)(σ(name = ‘박지성’)((customer ⋈(customer.custid = orders.custid) orders)))

---

# 3장

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2014.png)

Q. 모든 도서의 이름과 가격을 검색하시오

```sql
SELECT bookname, price FROM book;
```

Q. 모든 도서의 이름과 가격을 검색하시오

```sql
SELECT price, bookname FROM book;
```

Q. 도서 테이블에 있는 모든 출판사를 검색하시오

```sql
SELECT publisher FROM book;
```

Q. 가격이 10000원 이상, 20000원 이하인 도서를 검색하시오

```sql
SELECT * FROM book WHERE price <= 20000 AND price >= 10000;
```

Q. 출판사가 ‘굿스포츠’ 혹은 ‘대한미디어’인(아닌) 도서를 검색하시오

```sql
SELECT * FROM book WHERE publisher IN ('굿스포츠', '대한미디어'); //or써도 됨
SELECT * FROM book WHERE publisher NOT IN ('굿스포츠', '대한미디어');
```

Q. 축구의 역사를 출간한 출판사를 검색하시오

```sql
SELECT publisher FROM book WHERE bookname = '축구의 역사';
SELECT publisher FROM book WHERE bookname LIKE '축구의 역사';
```

Q. 도서이름에 축구가 포함된 출판사를 검색하시오

```sql
SELECT publisher FROM book WHERE bookname LIKE '%축구%';
```

Q. 도서이름의 왼쪽 세번째에 ‘구’라는 문자열을 갖는 도서를 검색하시오

```sql
SELECT publisher FROM book WHERE bookname LIKE '__구%';
```

Q. 도서를 이름순으로 검색하시오

```sql
SELECT * FROM book ORDER BY bookname;
```

Q. 도서를 가격순으로 검색하고 가격이 같으면 이름순으로 검색하시오

```sql
SELECT * FROM book ORDER BY price, bookname;
```

Q. 도서를 가격 내림차순으로 검색하고 가격이 같으면 이름순으로 검색하시오

```sql
SELECT * FROM book ORDER BY price DESC, bookname ASC;
```

Q. 고객이 주문한 도서의 총 판매액을 구하시오

⭐집계함수(5개) : SUM, MAX, MIN, AVG, COUNT

```sql
SELECT SUM(saleprice) AS '총매출' FROM orders;
```

Q. 2번 김연아 고객이 주문한 도서의 총 판매액을 구하시오

```sql
SELECT SUM(saleprice) AS '김연아 구매총액' FROM orders WHERE custid = 2; 
```

Q. 고객이 주문한 도서의 총 판매액, 평균값, 최저가, 최고가를 구하시오

```sql
SELECT SUM(saleprice), AVG(saleprice), MIN(saleprice), MAX(saleprice)
FROM orders;
```

Q. 마당서점의 책 전체 판매 건수를 구하시오

```sql
SELECT COUNT(*) FROM orders;
```

Q. ⭐고객별로 주문한 도서의 총 수량과 총 판매액을 구하시오

```sql
SELECT custid, COUNT(*), SUM(saleprice) FROM orders GROUP BY custid;
```

Q. ⭐고객별로 주문한 도서의 총 수량과 총 판매액을 구하시오(단, 2권이상 도서 구매자만 표시합니다)

- HAVING은 GROUP BY와 같이 사용해야한다, HAVING은 무조건 집계함수로 조건을 명시해야 한다, WHERE절 보다 뒤에 와야한다.

```sql
SELECT custid, COUNT(*), SUM(saleprice) FROM orders GROUP BY custid
HAVING COUNT(*) >= 2;//조건은 무조건 집계함수로
```

Q. 주문 릴레이션과 고객 릴레이션을 합쳐라(조건 없으면 카티전 프로덕트)

```sql
SELECT * FROM orders, customer;
```

Q.고객과 고객의 주문에 관한 데이터를 모두 검색하시오

```sql
SELECT * FROM customer, orders WHERE customer.custid = orders.custid;
```

Q.고객별로 주문한 모든 도서의 총 판매액을 구하고 고객별로 정렬하시오

```sql
SELECT name, SUM(saleprice) FROM customer, orders 
WHERE customer.custid = orders.custid
GROUP BY customer.name
ORDER BY customer.name;
```

Q. 도서를 구매하지 않은 고객을 포함하여 고객의 이름과 고객이 주문한 도서의 판매가격을 구하시오

```sql
SELECT customer.name, orders.saleprice
FROM customer LEFT OUTER JOIN orders
							ON customer.custid = orders.custid; //LEFT, RIGHT, FULL
```

Q.(부속질의)가장 비싼 도서의 이름을 구하시오

```sql
SELECT bookname FROM book WHERE price = (SELECT MAX(price) FROM book);
```

Q.도서를 구매한 적 있는 고객의 이름을 검색하시오

```sql
SELECT name FROM customer
WHERE custid IN (SELECT custid FROM orders);
```

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2015.png)

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2016.png)

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2017.png)

- 합집합 : UNION, 차집합 : MINUS, 교집합 : INTERSECT

![기본키가 2개 이상일 때](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2018.png)

기본키가 2개 이상일 때

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2019.png)

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2020.png)

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2021.png)

![Untitled](Database-mid%2000f2a4bcbdc442d4b693ee7b075f63d4/Untitled%2022.png)