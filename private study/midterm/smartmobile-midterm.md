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
void main(List<String> args) {
  test((int value){print("Number $value");});
}
```

- Optional Named Parameters : Dart에서 curly brackets {} 은 optional, named parameter를 지정하는 데 사용한다. {}사용시 ?안하면 오류뜨는게 아마 optional이기 때문에 null이 들어올 가능성이 있어서 그런것 같음.

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
```xxxxxxxxxx String name = 'khw';var str1 = 'i am' + khw + 'years' + (23).toString();var str2 = 'i am (23) dart
````