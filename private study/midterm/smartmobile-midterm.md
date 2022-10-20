# App-mid

## **⭐dart laguage⭐**

---

- 변수형
    - var : 어떤 타입의 변수도 할당 가능, 선언과 동시에 할당한 경우 해당 타입을 고정하게 됨. 따라서 이후에 데이터 추가하게 되면 에러가 발생, 반대로 선언과 동시에 할당하지 않는 경우 어떠한 데이터 타입도 저장 가능한 `dynamic type`이 된다.
        - var = 10;
        - var = “test”;
    - dynamic : var value = 17; value = “hi”; 와 같이 선언 이후 다른 타입으로 자동변경 가능하다.(웬만하면 사용하지 않을 것)
    - int : 정수형, 64bit
    - double : 실수형, 64bit
    - String : 문자형, + 기호를 통해 합칠 수 있다, “”, ‘’ 둘다 가능하다.
    
    ```dart
    String name = """
    my name is
    khw
    hi
    """; //multiline strings
    ```
    
    - bool : 참 / 거짓
        - bool var1 = true;
        - bool var2 = false;
    - List : 리스트 변수
    
    ```dart
    List<String> fruits = [];
    List<String> fruits = ['Apple', 'Banana', 'Kiwi']
    fruits.add("apple");
    fruits.add("banana");
    ```
    
    - enum : 한정된 상수 값 집합을 나타내기 위해 사용된다.
    - final : 상수선언 / `런타임`에 상수가 지정된다. final과 var는 같이 사용 불가
    - const : 상수선언 / `컴파일 시점`에 상수가 지정되어야 한다. const와 var는 같이 사용 불가
    
    ```dart
    void main(List<String> args) {
      final name1 = "dd"; //자동 추론
      print(name1);
      const name2 = "dd"; //자동 추론
      print(name2);
    }
    ```
    
    - nullable : ?를 통해 초기값을 설정하지 않고 변수 선언가능. 즉 null을 갖을 수 있음, 대입도 가능
    - late : late변수를 사용하면 non-nullable변수의 초기화를 나중에 할 수 있다.
    - num : int, double의 상위 클래스로서, 둘다 가능하다.
        - num val1 = 10; num val2 = 10.0;
- _ : private
- ${} : 이거 자체가 String으로 return하기 때문에 다음과 같이 할 필요 없다. (var test = "${25.abs()}“) or (var redundant = "${25.toString()}";)
    
    ```dart
    var age = 25;
    var myAge = "my age is $age years old";
    ```
    
- String변수 name을 name[0], name[1]과 같이 하면 슬라이싱 가능함
- toString과 $의 공통점

```dart
String name = 'khw';
var str1 = 'i am' + name + 'years' + (23).toString();
var str2 = 'i am ${name} years ${23};
```

- String변수를 합치는 두가지 방법

```dart
var s = 'i am go to'
          'hello'; //i am go tohello
var s = 'i am go to' +
        'hello'; //i am go tohello
```

- StringBuffer

```dart
void main(List<String> args) {
  var buffer = StringBuffer();
  for(var i = 0; i < 90; i++) 
    buffer.write("$i ");
 
  var value = buffer.toString(); //StringBuffer -> String
  print(buffer); //StringBuffer type
  print(value); //String type
}
```

- enumerated type

```dart
enum Fruits { Apple, Pear, Grapes, Banana, Orange } //not ;
void main() {
  Fruits liked = Fruits.Apple; //type : fruits
  var disliked = Fruits.Banana; //type : fruits
  var index = Fruits.Grapes.index;
  print(liked.toString()); // fruits -> String
  print(disliked.toString()); //fruits -> String
  print(index); //print : 2
}
```

- NaN / isNaN

```dart
  var value = 0 / 0;
  print(value); //NaN으로 출력
  bool check = value.isNaN; // check = true
```

- java에서는 배열이 int[] array = new int[6]; 이지만, dart에서는 List<T>이다.
- fianl, const로 선언한 List

```dart
**void main() {
  final List<int> array1 = [];
  const List<int> array2 = [];
  array1.add(1); //가능
  array2.add(2); //불가능
  array1 = [1,2,3]; //재 초기화 불가능
  array2 = [1,2,3]; //재 초기화 불가능
}**
```

- nullable

```dart
void main() {
  int? value;
  print(value); //print : null
}

```

```dart
void main() {
  String? name;
  String? first = name?[0]; //세군데에 전부 ? 붙여야함. 안붙히면 에러남.
  print(first); //first = null
}
```

- null일경우 runtime error 발생시킴(not compile error)(! = `bang operator`)

```dart
void main() {
  int? value;
  int notvalue = value!; //nullable을 non-nullable에 대입할 때 사용함
}
```

- is : value is int, value is double(true or false return)
- as : type convert(value as int)

```dart
num? value = 5;
int otherValue = value as int; //value와 othervalue는 같은 타입 아니다.
```

- null 조건 연산자 -> ?.
    - null 조건 연산자는 만약 연산자 앞의 변수가 null이라면 연산자 뒤의 작업을 시행하지 않고 null을 반환하는 연산자입니다. null이 아닌 경우는 연산자 뒤의 작업이 정상적으로 실행됩니다.

```dart
String? notString = null;
print(notString?.length); // null 출력
double? pi = 3.14;
final round1 = pi.round();//No, null이 가능할 수도 있으니까 ?꼭 넣어야함, int?형임
final round2 = pi?.round(); // Ok, 만약 null이면 null로 대입시킴, int?형임
```

- null 조건 연산자 → ??
    - null이 아닐경우 값 ?? null일 경우 값

```dart
int? nullable = 10;
int nonNullable = nullable ?? 0; //null아니니까 10이 들어감
```

- ~/ : 몫 나눗셈, % : 나머지
- and : &&, or : ||, not : !

---

- flutter doctor : 플러터 개발 환경 설정 확인 명령어
- models : business logic / widgets : 재사용 가능한 UI 위젯 / test/. : 자동화 테스트 제품군
- yaml : `YAML Ain't markup language`(더 보편적인 것 : .json)
    - 구성 파일 작성에 사용되는 데이터 직렬화 언어이며 데이터 표현 양식
- 번개모양 : Hot reload → 또다시 build를 할 필요없는 refresh 기능
- widget : 화면에 나타나는 모든 것. 모든 것은 widget class의 자식 클래스이다. 이들을 엮어 widget tree계층을 만든다
- if 구문을 이용한 ??구현 및 삼항연산자 구현

```dart
String? status = null;
if (status != null) // equal status = status ?? "RIP";
  isAlive = status;
else
  isAlive = "RIP";
if (correctAns >= 18) // equal status = (correctAns >= 18) "Test ~~" : "RIP"; 
  status = "Test passed!";
else
  isAlive = "RIP";
```

- switch - case문

```dart
switch(){
  case 1:
    ~~~;
    break;
  case 2:
    ~~~;
    break;
  default:
    ~~~;
}
```

- for문, while문, do-while문 : C언어와 동일
- for - in loop

```dart
void main() {
  List<int> array = [1,2,3,4,5];
  for(var i = 0; i < array.length; i++){
    print(array[i]);
  }
  for(var i in array)
    print(i+5);
  for(final i in array)
    print(i+5);
     //셋다 가능하다.
     //final과 var차이는 재 할당 할수 있는지의 여부(var is ok)
}
```

- assert (디버깅 함수) : 릴리스 모드에서 모든 어설션은 컴파일러에서 무시되며 실행 흐름을 방해하지 않습니다. 어설션은 디버그 모드에서만 작동합니다.

```dart
Dart, 디버깅 함수 assert()

assert (조건식, 추가메시지);
 
조건식이 거짓인 경우 오류 메시지를 출력합니다. 
 
// 변수가 null 값인지 검사.
assert(text != null);
 
// 값이 100보다 작은지 검사
assert(number < 100);
 
// https URL 형식인지 검사  
assert(urlString.startsWith('https'));
 
추가 메시지를 넣어주면 오류 발생시 해당 메시지를 출력합니다.
 
assert(urlString.startsWith('https'), 'URL ($urlString) should start with "https".');
```

- dart에서의 함수 사용법

```dart
void main(){
  int add1(int a, int b){
    return a + b;
  }
  //화살표 함수
  int add2(int a, int b) => a + b;
  int add3(int a, int b) => add1(a,b);
  void print1(int val){
    if(val == 1)
      print("hello, world!");
  }
  //불가. 단순 리턴 혹은 함수호출 말고 다음과 같은건 안됨.
  void print2(int val) => if(val == 1){print("hello, world!")};
}
```

- 함수에서 return 자료형 지정 안하면 → dynamic

```dart
void test() {}
test() {} //dynamic
```

- 함수 이름만 바꿔쓰는 3가지 방법(Function type)

```dart
bool checkEven(int value) => (value % 2 == 0); 
void main() {
  //같은 함수를 다른 이름으로 정의하는 3가지 방법
  final check1 = checkEven;
  var check2 = checkEven;
  bool Function(int) check3 = checkEven;
}
```

- anonymous funtions

```dart
void main(List<String> args) {
  //anonymous funtions
  bool Function(int) isEven1 = (int value) => value % 2 == 0; 
  var isEven2 = (int value) => value % 2 == 0;
  final isEven3 = (int value) => value % 2 == 0;

  var hello1 = (String nickname) => "hello" + nickname;
  var hello2 = (String nickname){/*다양한함수들*/};
}
```

```dart
void test(void Function(int) action){
  List<int> array = [1,2,3,4,5];
  //fianl array = [1,2,3,4,5];로 하면 자동으로 array type = List<int>
  for(var i in array)
    action(i);
}
void main() {
  test((int value){print("Number $value");});
}
```

- Dart에서 curly brackets {} 은 optional, named parameter를 지정하는 데 사용한다. {}사용시 ?안하면 오류뜨는게 아마 optional이기 때문에 null이 들어올 가능성이 있어서 그런것 같음.

```dart
void test({int? a, int? b}){//? 중요!!!
  print("$a");
  print("$b");
}
void main(List<String> args) {
  test(a:1); //a=1, b=null
  test(a:2, b:3); //a=2, b=3
  //test(2,3); //error
}
```

```dart
void test({int? a, int b = 0}){
  print(a);
  print(b);
}
void main(List<String> args) {
  test(a: 2); // 2, 0
}
```

```dart
void test({int? a, required int b}){
  print(a);
  print(b);
}
void main(List<String> args) {
  test(a : 2, b : 3); //2, 3 good
  //test(a: 2); // error
}
```

- 한쪽만 { } 사용할 땐 자리지정된 파라미터 이후에 { }사용해야 한다. 아니면 error. 아래는 예시

```dart
void test1(int a, {int? b}){
  print(a);
  print(b);
} // good
void test2({int? a}, int b){
  print(a);
  print(b);
} //doesn't compile
```

- [ ] 대괄호 사용(자리 지정됨) ?빼먹지 말기

```dart
void test1([int? a, int? b]){
  print(a);
  print(b);
} // good
```

- outer function은 호출 가능하지만, inner fucntion은 외부에서 호출 불가능하다.

![Untitled](App-mid%206bece7fa6a77419fb17b4ac120eb73d7/Untitled.png)

- typedef 사용법 : 함수에서만 사용가능

```dart
void printIntegers1(void Function(String) logger) {
  logger("Done."); 
}
typedef Func = void Function(String); //typedef는 함수에서만 사용가능하다.
void printIntegers2(Func logger) {
  logger("Done."); 
}
void main(List<String> args) {
  printIntegers1((String value){ print(value);}); //print : Done.
  printIntegers2((String value) {print(value);}); //print : Done.
}
```

---

- Class 사용 예시

```dart
class Person{
  String? name;
  String? age;
  //생성자
  Person(String name, String age){ //다른 언어와 같이 public으로 안함
    this.name = name;
    this.age = age;
  }
}
```

- dart는 오버로딩 안됨 ex(void test(int a) / void test(int a, int b))
- dart Library 사용법(import 사용법)

```dart
import 'dart:math';
import 'dart:io';
```

- 캡슐화 사용법(정보은닉), dart에서는 기본적으로 모든 멤버가 public임

```dart
String name = "khw";
String _privateName = "www"; //main에서 맘대로 접근할 수 없음
```

- private멤버 접근하는 법

```dart
class Test{
  String name1 = "iii";
  String _name2 = "qqq";
}
void main(List<String> args) {
  var temp = Test();
  print(temp.name1); //ok
  print(temp.name2); //error
  print(temp._name2); //ok
}
```

- 생성자 사용법 및 private변수에 값 넣기

```dart
class Fraction {
  int? _test1; 
  int? _test2;
  Fraction(int test1, int test2){
    _test1 = test1; 
    _test2 = test2;
  } 
}
```

- 생성자를 생성하는 또다른 방법(named constructors)

```dart
class Fraction {
  int? _test1; 
  int? _test2;
  Fraction(int test1, int test2){
    _test1 = test1; 
    _test2 = test2;
  } 
  Fraction.hello(){ //생성자 새로운 방법
    _test1 = 10;
    _test2 = 20;
  }
}
void main(List<String> args) {
  var fraction1 = Fraction(10, 20); //위와
  var fraction2 = Fraction.hello(); //아래는 같다
}
```

- 멤버변수를 nullable설정 안했을 때, 생성자(this.멤버변수); 사용법

```dart
class Test{
  int _a;
  Test(this._a); //실행 가능(파라미터 입력 안하면 객체가 애초에 안만들어 지니까)
  Test(int a){ //실행 불가능(a에 null이 들어올 수 있으니까)
    _a = a;
  }//이걸 가능하게 하려면 최초에 선언을 int? _a;로 하면 됨.
}
void main(List<String> args) {
  var t1 = Test(10);
  print(t1._a);
}
```

- 컴파일 타임에서 오류 안낼라면 final 혹은 static const를 사용해야함(const는 안 됨)

```dart
// OK
final double a = 0.0;
// NO, instance variables can only be 'final' const double b = 0.0;
const doubla b = 0.0;
// OK
static const double PI = 3.14;
// OK
static const PI = 3.14;
```

- 불변 클래스를 만들고 싶으면 내부에 final로만 생성된 변수만 있어야함, 또한 생성자 앞에 const붙여야함. 근데 하나라도 final아닌게 있다면 const붙이면 안되며 당연히 불변 클래스도 만들 수 없음

```dart
class Test{
  final int a;
  final int b;
//int c; 얘가 추가 된다면 불변 클래스 안됨. const도 당연히 붙히면 안됨.
  const Test(this.a, this.b); //불변 클래스 가능
}
void main() {
  var t1 = Test(10,20);
}
```

- dart의 private는 다른 언어와 다르게 _입력하면 접근이 가능함… 근데 이러면 너무 위험하잖아? 그래서 도입한게 getters(get)임. 이를 통해 read-only변수를 새롭게 만들 수 있음(_만 없앤)

```dart
class Test{
  int _a;
  int _b;
  Test(this._a, this._b);

  int get a => _a;
  int get b {return _b;}
}//a랑 b는 read-only변수임
```

- setter(set)도입 시 get으로 만든 멤버들에게 조작 권한 줄 수 있음

```dart
class Test{
  int _a;
  int _b;
  Test(this._a, this._b);

  int get a => _a;
  int get b {return _b;}

  set a(int value){
    _a = value;
  }
}
void main(List<String> args) {
  var t1 = Test(10, 20);
  t1.a = 20; //값 삽입할 땐 정상적인 방법으로 삽입 하면 됨. 만들 때만 함수식으로.
}
```

- operator overload

```dart
class Test{
  Test operator+(Test hi) => 
  Test operator-(Test hi) => 
  Test operator*(Test hi) => 
  Test operator/(Test hi) => 
}
```

- callable class : 클래스를 함수처럼 사용할 수 있게 해줌, 함수 이름을 call로 하면 됨.

```dart
class Example {
  double call(double a, double b) => a + b;
}
void main() {
  final ex = Example();
  final value = ex(1.3, 1.7);
  print("$value"); //print : 3.0
}
```

- 클래스 clone하기, anotherMe는 me를 단지 ‘참조’할 뿐이다.

![Untitled](App-mid%206bece7fa6a77419fb17b4ac120eb73d7/Untitled%201.png)

- 진정으로 클래스를 복사하기 : copyWith()

![Untitled](App-mid%206bece7fa6a77419fb17b4ac120eb73d7/Untitled%202.png)

---

**⭐통신 기출문제⭐**

- 프로토콜 : 정보 전송의 통신 규약
- 프로토콜 구성요소 : 의미(semantic), 구문(syntax), 타이밍(timing)
- 라우팅 : 출발지에서 목적지까지 인용 가능한 전송로 중 가장 효율적인 전송로 선택하는 것
- ITU(International Telecommunication Union) : 정보 통신 기술 분야의 국제 표준화 기구
- OSI 7계층 : physical layer → Data Link Layer → Network Layer → Transport Layer → Session Layer → Presentation Layer → Application Layer
- 홉 단위 수행, 통신망 노드에서 필요한 프로토콜 : 1,2,3계층
- Data Link Layer : PPP, LLC, node-node
- Network Layer : `통신망`을 통하여 목적지 까지 패킷 전달
- Transport Layer : TCP / UDP, 종단간(end-end), 단말기 사이의 오류 수정과 흐름제어, process-process전달
- Session Layer : Process간의 대화제어 및 동기점, 데이터 복구 (process나오면 대부분 이거)
- 대역폭(bandwidth) : 최고 주파수 - 최저 주파수
- 회선의 전송 용량은 대역폭과 비례한다.
- 리피터(Repeater) : 장거리 전송 시 데이터의 감쇠 및 왜곡 현상을 방지하기 위해 사용
- 베이스밴드 전송 : 디지털 신호의 펄스열을 그대로 전송
- 변조 : 채널을 통해 효율적으로 전송되도록 송신 신호를 변환하는 것
- 아날로그-디지털 부호화 방법이 아닌 것 : CDM
- ASK(진폭편이변조) : 반송파로 사용하는 정현파의 전폭에 정보를 싣는 변조 방식
- QAM(직교진폭변조) : 반송파의 진폭과 위상을 상호 변환하는 변조 방식
- PSK : 정보에 따라 위상을 변환시키는 변조 방식
- 파장 짧 → 긴 : 자외선 가시광선 적외선 마이크로파 초단파 단파
- 마이크로파 특징 아닌 것 : 전송 지연이 많이 발생한다
- 다중화 기법(전송효율 good) : 주파수 분할, 시간 분할, 코드 분할(NOT 전류 분할)
- FDM(주파수 분할 다중화) : guard band(보호 주파수대)(상호 간섭 방지)사용, 여러 신호를 서로 다른 주파수 대역을 이용하여 동시에 전송, 변복조 기능 포함, 전송하려는 신호에 필요한 대역폭보다 전송 매체의 유효 대역폭이 클 때 사용, (time slot이용 X, 터미널의 수가 동적으로 변함 X, 동기식과 비동기식 다중화 방식이 있다X, 가변 파장 송신 장치tunable laser, 가변 파장 수신 장치tunable filter를 사용하여 특정 채널을 선택한다X)
- OFDM(Orthogonal Frequency Division Multiplexing) : 하나의 정보를 여러 개의 반송파로 분할하고, 분할된 반 송파 사이의 주파수 간격을 최 소화하기 위해 `직교 다중 화`해서 전송하는 통신 방식, (사용자의 데이터 열에 따라 반송 주파수를 변화한다X), 여러 개의 부반송파에 고속의 데이터를 저속의 병렬 데이터로 변환하여 실어 보내는 기법, 고속의 송신 신호를 다수의 직교하는 협대역 반송파로 다중화시키는 변조 방식은?,
- TDM(시분할 다중화) : time slot과 관련된 대부분 문제 답은 `동기식 시분할 다중화`, 동기식 시분할 다중화는 한 전송 회선의 대역폭을 일정한 시간 단위로 나누어 각 채널에 할당하는 방식, (전송로의 데이터 전송 시간을 일정한 타임 슬롯으로 나누어 각 부채널로 분배하여 비동기 형만 사용하고 있다X)
)
    - 효율 : 동기식 < 통계식
    - 통계적 시분할 : 별도의 주소 정보가 필요
    - 통계적 시분할 : time slot고정할당X → 동기식 시분할, time slot이용하나, 유동적으로 이용함
- 129, 130은 문제 통째로 암기
    
    129. 다중화multiplexing에 대한 설명으로 틀린 것은?                                                 4
    1 다중화란 효율적인 전송을 위하여 넓은 대역폭을 가진 하나의 전송 링크를 통해 여러 신호
    를 동시에 실어 보내는 기술을 말한다.
    2 동기식 시분할 다중화는 전송 시간을 일정한 간격의 슬롯time slot으로 나누고, 이를 주기
    적으로 각 채널에 할당한다.
    3 주파수 분할 다중화는 여러 신호를 전송 매체의 서 로 다른 주파수 대역을 이용하여 동시
    에 전송하는 기술을 말한다.
    4 파장 분할 다중화에서는 각 채널별로 특정한 타임 슬롯이 할당되지 않고 전송할 데이터가
    있는 채널 만 타임 슬롯을 이용하여 데이터를 전송한다.
    
    130. 다중화 기술에 대한 설명으로 옳지 않은 것은?                                                        4
    1 하나의 통신로를 여러 가입자가 동시에 이용하여 통신할 수 있도록 하는 것이 다중화 기술
    이다.
    2 아날로그 방식의 주파수 분할 다중화FDM와 디지털 방식의 시분할 다중화TDM 및 코드 분
    할 다중화 CDM 기술이 있다.
    3 주파수 분할 다중화FDM는 채널마다 독립된 주파수 대역으로 분할하여 다중화하는 방식으
    로 시분할 다중화 또는 코드 분할 다중화보다 효율이 낮다.
    4 시분할 다중화TDM는 정해진 시간으로 슬롯을 배정하고 이를 다시 Frame으로 묶어 다중
    화하는 방식으로 코드 분할 다중화CDM보다 다중화 효율이 높다.
    
- CSMA/CD : 자유 경쟁 충돌 허용, IEEE 802.3, BUS형, CS Carrier Sense는 데이터 sensing 즉 체크하는 기능이다, 어느 한 기기에 고장이 발생하여도 다른 기기의 통신에 전혀 영향을 미치지 않는다, (p-persistent기법 사용X), 구현 간단, 지연시간 예측 어려움,
- 무선 LAN : CSMA/CA, DCF(경쟁의 의한 채널 접근), 자원은 유한하다,
- bluetooth : 2.4Ghz, 간섭에 강함, 회로 구성 간소화 가능, 코어 규격/프로파일 규격 구분, 저가격, 저전력
- ZigBee : 지능형 홈 네트워크 및 산업용 기기 자동차, 물류, 환경 모니 터링, 휴먼 인터페이스, 텔레매틱스 등 다양한 유 비쿼터스 환경에 응용이 가능하다
- 3세대 : WCDMA
- QDMA : 다중 접속 방식 X
- CDMA : 산악 지형 또는 도심 지역에서 품질 그대로임(그러니까 우리가 썼지!)
- 인터네트워킹 : 리피터(같은 LAN의 두 세그먼트를 연결), 라우터, 게이트웨이, 스위치
- HUB : LAN과 단말장치 연결
- 라우터 : 복수 개의 네트워크를 연결하는 데 사용
- 게이트웨이 : 프로토콜의 변환이나 외부 네트워크와 접속하기 위한 목적, 프로토콜이 전혀 다른 네트워크 결합, 트래픽 혼잡 상태 제어X 때문에 병목현상 발생
- TCP/IP : 아닌 계층(세션계층), TCP(전송 계층 프로토콜로 순서 제어와 에러 제어), IP(네트워크 계층)
    - UDP(트랜스포트 계층) : 오버헤드 적다, 빠른 전달 가능, 신뢰성 없다, 흐름 제어나 순서 제어가 없어 전송 속도가 빠르다, 체크섬 필드가 필요 있다.
    - 연결형 / 비연결형 / 비연결형 (TCP/IP/UDP)
- TCP 특징 X : 데이터 그램 서비스 아님, 라우팅(경로설정) 아님
- VoIP : 보안 약하다
- DNS : 도메인 → IP주소

---

## **⭐족보 기출문제⭐**

- 데이터 통신 시스템 최초 분야 : 군사분야
- 현재 사용하는 인터넷의 효시 : 알파넷
- 통신을 위해 개체들은 (  )에 합의해야 한다. (  )은 통신을 제어하는 규칙들의 집합이다. → 프로토콜
- 네트워크 계층 데이터 단위 : frame
- 하나의 프로세스에서 다른 프로세스로 메세지 전송에 대한 책임이 있는 계층은 : 전송계층(transport)
- node-node : data-link layer
- 정현파를 표현하는 데 사용되는 요소 : amplitude, frequency, phase, time
- 채널 용량 구하기

```
C=W*log2(1+S/N)   C:채널용량[bps], W:대역폭{Hz], S:신호전력[Watt], N:잡음전력[Watt]
```

- OSI는 7계층, TCP는 4계층
    
    ![Untitled](App-mid%206bece7fa6a77419fb17b4ac120eb73d7/Untitled%203.png)
    
- 객체지향 언어의 4가지 특성을 영어로 : Inheritance, Encapsulation, Abstraction, Polymorphism
- 무전기의 전송 방식 : 반이중 통신
- LTE 다중화 방식 : OFDM
- 서로 다른 파장을 갖는 신호를 다중화 하는 방식으로 광 통신에서 사용하는 방식 : WDM
- 난수 발생에 따라 반송파의 주파수를 특정 패턴으로 바꾸면서 데이터를 전송 : FHSS

---

## **⭐수업시간 강조부분⭐**

- AOT(Ahead of time compilation)
- AMPS(Advanced Moblile Phone System)
- **JIT(just in time)**
- AM(Amplitude Modulation)
- FM(Frequency Modulation)
- **relation(관계)** : 1:1 / 1:union / union:1
- **funtion(함수)** : 1:1 / union:1
- 따라서 relation이 더 넓은 개념이다.
- var a = 1.35e2; //10의 2승
- var a = 0xF1A; //16진수
- 신호세기는 파장의 제곱에 비례하고, 거리의 제곱에 반비례한다.
- FDMA(Frequency Division multiple access)
- DS(direct sequence), FH(Frequency hopping)
- CDMA(code division multiple access)
- IEEE 802.11a/b/g/n/ac/ad/ax/be 표준규격
- CSMA/CD(Carrier sense multiple access with collision detection)
- CSMA/CA(Carrier Sense Multiple Access with Collision Avoidance)
- FHSS(Frequency-hopping spread spectrum)
- DSSS(Direct Sequence Spread Spectrum)
- OFDM(Orthogonal Frequency Division Multiplexing)
- LOS(Line of Sight)
- CoAP(constrained application protocol)
- 6LoWPAN(IPv6 LOW POWER WPAN)
- RFID(Radio-Frequency Identification)
- UWB(Ultra Wide Band)
- GMPCS(Global Mobile Personal Communications by Satellite)
- UAV == Drone
- ITS(Intelligent Transport System)
- V2G (Vehicle to Grid), V2H (Vehicle to Home), V2L (Vehicle to Load), V2V (Vehicle to Vehicle), V2P (Vehicle to Pedestrian)
- PSM(power saving mode)
- NB-IoT(NarrowBand-IoT)

---