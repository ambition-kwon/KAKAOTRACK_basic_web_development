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

```dart
String name = 'khw';
var str1 = 'i am' + khw + 'years' + (23).toString();
var str2 = 'i am (23) 
```