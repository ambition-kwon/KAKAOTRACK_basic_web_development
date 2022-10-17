# C#-mid

- 가장 간단한 C프로그램을 작성해보시오

```cpp
#include<stdio.h>
void main(){
		printf("Hello, World!\n");
}
```

- 조금 복잡한 C프로그램을 작성해보시오

```cpp
#include<stdio.h>
	int iX;
	int iY;
	void Assign(int a, int b){
		iX = a;
		iY = b;
	}
	int add(){
		return iX + iY;
	}
	void main(){
		Assign(2, 3);
		int iResult = add();
		printf("두 값을 합한 결과 = %d\n", iResult);
	}
```

- 지역변수와 전역변수의 차이점에 대해 설명하시오
    - 지역변수(local) : 함수 안에서 만든 변수
        - scope(사용범위) : 변수 정의한 함수 내에서만 접근 가능
        - life time(생명주기) : 함수가 실행될 때 생성되며, 함수가 종료되면 사라짐
    - 전역변수(global) :  함수 밖에서 만든 변수
        - scope(사용범위) : 모든 함수에서 접근 가능
        - life time(생명주기) : 프로그램이 실행될 때 생성되며, 프로그램이 종료되면 사라짐
- 코드를 읽고 분석하기 쉽게 하는 방법 : 코드 추상화
- 코드 추상화(Abstraction): 함수(function)
- 매개변수(파라미터) == 지역변수
- (유일하게⭐)  100개의 `변수`와 1000개의 `함수`로 이루어진 프로그램? : 재사용이 어렵다, 수정이 어렵다 → 소프트웨어 위기가 발생한다 → 변수와 함수를 하나로 묶어야 한다 → 데이터 추상화 → 클래스(Class)
- 데이터 추상화(Abstraction): 클래스(class)
- 클래스 == 자료형
- 자료형 → `변수` 만들라고 있는 것
- 클래스 → `객체` 만들라고 있는 것

---

- 창자이야기 : 클래스로 묶지 않은 데이터들은 마치 창자를 몸 밖에 매달고 다니는 것과 같다!
    - 해결방법 : 클래스로 묶자!(XXX) → `정보은폐(information hiding)`
    - 묶자 == `캡슐화(Encapsulation)`
- SDT(Standard Data Type)(표준자료형): int, double과 같은 자료형
- ADT(Abstract Data Type)(추상자료형) : Class와 같은 자료형
- 멤버변수 : 특성(키, 몸무게, 나이 등…)
- 멤버함수 : 할 줄 아는 일
- ⭐클래스의 존재 이유 : `객체` 만드려고, `재사용` 하려고
- 클래스를 도입한 수업시간에 진행된 가장 간단한 코드

```cpp
#include<stdio.h>
class XXX{
private:	
	int iX;
	int iY;
public:
	void Assign(int a, int b){
		iX = a;
		iY = b;
	}
	int add(){
		return iX + iY;
	}
}; //C++에선 클래스 끝에 세미콜론 필수

XXX gildong;

	void main(){
		gildong.Assign(2, 3);
		int iResult = gildong.add();
		printf("두 값을 합한 결과 = %d\n", iResult);
	}
```

---

- 💯 다음 주어진 C++코드를 C#코드로 변경해보아라(위 : 문제 / 아래 : 정답)

```cpp
 #include <stdio.h>

class XXX 
{
private:
    int iX; 
    int iY; 

public:
    void Assign(int x, int y) {
        iX = x;
        iY = y;
    }

    int Add() {
        return iX + iY;
    }
};

XXX gildong;

void main() 
{
    gildong.Assign(2, 3);

    int iResult = gildong.Add();

    printf("두 개의 값을 더한 결과 : %d\n", iResult);
}
```

```cpp
using System;//헤더파일 제거

class XXX 
{
    private int iX; 
    private int iY; 

    public void Assign(int x, int y) {
        iX = x;
        iY = y;
    }

    public int Add() {
        return iX + iY;
    }
} //세미콜론 제거

Class My{//main을 감싸는 임의의 클래스 추가
		public static void Main() //main->Main 
		{
		    XXX gildong = new XXX(); //XXX gildong과 같은 의미
				gildong.Assign(2, 3);
		    int iResult = gildong.Add();
				Console.WriteLine("두 개의 값을 더한 결과 : " + iResult); //printf 대신		    
		}
}
```

---

- 💯멤버는 멤버를 호출(==접근)할 수 있다.
- C#에서 Main함수가 static인 이유는? : 객체를 만들지 않아도 닷넷(.NET) 프레임워크가 호출할 수 있도록
- C#에서 Main함수를 클래스 안에 넣어버린 이유는? : 전역함수를 클래스 멤버함수로 만듦으로서 모든 함수가 예외없이 클래스 멤버함수가 되도록
- 만약 똑같은 이름의 클래스가 생긴다면?(동료 협업간) : `namespace`도입
- using문 사용 이유 : 반복적으로 네임스페이스를 붙이는 것이 귀찮아서
- 아래 코드는 XXX클래스가 2개임에도 정상적으로 동작하는 코드이다.

```csharp
using System;

namespace A{
	class XXX{
		private int iX;
		private int iY;
		public void Assign(int a, int b){
			iX = a;
			iY = b;
		}
		public int add(){
			return iX + iY;
		}
	}
}

namespace B{
	class XXX{
		public static void Main(){
			A.XXX gildong = new A.XXX(); //제일 중요한 부분
			gildong.Assign(2, 3);
			int iResult = gildong.add();
			Console.WriteLine("두 값의 합은 : " + iResult);
		}
	}
}
```

- WriteLine은 Console이라는 클래스안에 있는 static함수이다.

---

- 레퍼런스 : 변수의 `별명` 혹은 변수의 `또 다른 이름`
- C# 접근제한자 : `public`, `protected`, `private`
    - internal이 있는 것 같긴 한데 신경쓰지 말자

```csharp
using System;
class Point{
	protected int iX;
	protected int iY;
	public void Assign(int a, int b){
		iX = a;
		iY = b;
	}
	public int add(){
		return iX + iY;
	}
}
class Circle : Point{
	protected int iRadius;
	public void SetRadius(int r){
		iRadius = r;
	}
	public double Area(){
		return 3.14 * iRadius * iRadius;
	}
}
class Ellipse : Circle{
	private int iRadius2;
	public void SetRadius2(int r){
		iRadius2 = r;
	}
	public new double Area(){ //💯💯💯💯💯💯💯💯제일 중요
		return 3.14 * iRadius * iRadius2; 
	}
}
class XXX{
	public static void Main(){
		Point gildong = new Point();
		Circle youngja = new Circle();
		Ellipse cheolsu = new Ellipse();

		gildong.Assign(2, 3);
		youngja.SetRadius(10);
		cheolsu.SetRadius(20);
		cheolsu.SetRadius2(30);

		int result = gildong.add();
		double area = youngja.Area();
		double area2 = cheolsu.Area();

		Console.WriteLine("x+y = " + result);
		Console.WriteLine("원 너비 = " + area);
		Console.WriteLine("타원 너비 = " + area2);
	}
}
```

- 💯Circle의 멤버 변수 갯수는? : 3개(iX, iY, iRadius)
- 💯Ellipse의 멤버 변수 갯수는? : 4개(iX, iY, iRadius, iRadius2)
- 💯💯💯💯Area함수를 override(재정의)할 때 사용한 키워드는? : `new`
- 코드를 위와같이 상속(재사용)하는 이유는 : 단지 귀찮아서, 서로 엮인 관계를 만들기 위함이 아니다
- protected를 보면 무슨생각을 해야하는가? : 나중에 재사용 하겠구나

---

- csc명령어 : 컴파일 명령어(`my.cs` → `my.exe`)
- csc /t:library 명령어(Main함수 없을 때) : 컴파일 명령어(`my.cs` → `my.dll`)
- cmd로 csc명령어 안될 때 : C:\WINDOWS\Microsoft.NET\Framwork\4.xx Path 추가

```csharp
public class Point{ //💯💯💯💯💯public이라고 명시 안하면 후에 컴파일 에러남!!!!
	public int iX;
	public int iY;
	public void Assign(int a, int b){
		iX = a;
		iY = b;
	}
	public int add(){
		return iX + iY;
	}
}//Point.cs라고 하자
```

```csharp
class XXX{
    static void Main(string[] args){
        Point gildong = new Point();
        gildong.Assign(2,3);
        int iResult = gildong.add();
        System.Console.WriteLine("결과 = " + iResult);
    }
}//XXX.cs라고 하자
```

- 위 두 코드를 동작시켜 결과를 출력시키는 방법(순서대로 3단계)
    - `csc /t:library Point.cs`
    - `csc XXX.cs /reference:Point.dll`
    - `XXX.exe`
- 가장 중요한 것 : Point.cs의 class앞에 public키워드 안붙이면 동작 안한다.
- `.exe` / `.dll` → 어셈블리(Assembly)라고 한다
- 어셈블리(Assembly)라고 하는 이유는? : 우리가 그동안 다뤄왔던 실행파일(hwp.exe)과 다르기 때문 / 관련된 내용을 한 파일에 모아서 어셈블리라고 한다.
- 기존의 실행파일, 라이브러리 파일 문제점 :
    - 다른 OS에서 실행불가
    - dll사용하는 프로그램 작성하려면 이를 설명하는 헤더파일이 따로 준비되어 있어야 함
- 어셈블리는 dll안에 헤더파일이 모여있다.
- 닷넷(.NET) : JVM(자바가상머신)처럼 어셈블리를 실행하는 가상환경을 제공해준다 / 즉 어떤 OS던 간에 닷넷 환경만 구축되어 있다면 실행 가능하다.
- 어셈블리(Assembly) : `메`타데이터(관련정보) + `실`행코드
- 실행코드 : 기계어가 아닌 중간 형태의 코드(Intermediate Language)이다.
- CPU = CU + PU(==ALU)
- dll → 동적 / lib → 정적
- 닷넷 플랫폼 == 닷넷 런타임 == 닷넷 가상머신
- 💯메타데이터 = 메니페스트 + 클래스 정보
    - 메니페스트 : 어셈블리 이름, 버전, 정보, 검증 키 등 어셈블리에 대한 정보를 명확하게 보여주는 것
    
    > 메니페스토(manifesto) : 자신의 주장과 견해를 분명히 밝히는 연설
    > 
- 메타 : ~를 위한 또 다른 ~(ex. 메타버스 : 지구를 위한 또 다른 지구)
- 어셈블리 분석도구(`ildasm`) → my.exe / my.dll분석 → 메타데이터 + 실행코드 볼 수 있음
- 돋보기에 비유한 프로그램이 무엇인가? : ildasm💯

---

```csharp
public class MY{
	static void Main(){
	
	}
}
```

- 위의 코드를 컴파일 하여(MY.exe) ildasm으로 분석시 다음과 같이 나온다.

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled.png)

- MANIFEST → 메니페스트
- MY → 클래스 정보
- MANIFEST + MY → 메타데이터
- 실행코드(IL)를 보고 싶으면 : Main : void(string[])을 클릭하면 된다.

---

![MANIFEST 클릭 하여 자세히 보면 아래 그림과 같다.](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%201.png)

MANIFEST 클릭 하여 자세히 보면 아래 그림과 같다.

- My → 어셈블리 이름
- ver → 어셈블리 버전
- 💯publickeytoken : mscorlib 어셈블리 인증하는 키로 엉뚱한 mscorlib가 사용되는 것을 방지한다.

---

- Main()함수 안에 System.Console.WriteLine(”Hello, World!”); 추가 후 `ildasm`으로 실행코드 부분 살펴보자

![Main : void(string[])을 클릭하여 실행코드(IL)부분 살펴보기](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%202.png)

Main : void(string[])을 클릭하여 실행코드(IL)부분 살펴보기

- `ldstr` : “Hello, World!” 문자열을 스택에 push한다.
- `call` : 스택 top(최상단)에 있는 문자열을 pop한 후, WriteLine함수를 이용하여 화면에 출력한다.
- `ret` : return
- 💯 ldstr, call에 대해 각각 설명해보시오

---

- 지금까지는 `.exe`에 대해 살펴보았으니, 또다른 어셈블리인 `.dll`에 대해 살펴보자.

```csharp
public class Point{
	public Point(){//생성자
	
	}
}
```

- 위 코드를 .dll화 하여 `ildasm`으로 살펴보자

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%203.png)

- 💯 `.ctor` 이란? : 생성자 함수(constructor)이다.
- 💯 생성자 함수란? : 객체가 생성될 때 자동으로 실행되는 함수이다.

---

```csharp
public class Point{
    private int iNumber = 0;
    public Point(){

    }
    public void set(){
        System.Console.WriteLine("Hello, world!");
    }
}
```

- 위 코드를 .dll화 하여 ildasm으로 살펴보면 아래와 같다.

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%204.png)

- 먼저 Set()부분을 자세히 보자

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%205.png)

- ldstr, call, ret은 아까 Main()에서와 같이 stack을 중점으로 동작한다.
- .ctor(생성자 함수) 부분을 자세히 보자

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%206.png)

- `ldarg.0` : 현재 객체의 주소값(this)를 스택에 push
- `ldc.i4.0` : 0값을 스택에 push
- `stfld` : 스택에 있는 두 값(this, 0)을 pop하여 this.iNumber 멤버변수에 0값을 저장 후 초기화
- `ldarg.0` : 현재 객체의 주소값(this)를 스택에 push
- `call` : 스택에서 pop하여 this객체를 가져와서 .ctor생성자 함수를 호출한다.

---

```csharp
public class Point{
    private int iNumber = 0;
    public Point(){

    }
    public void set(int r){
        iNumber = r;
    }
}
```

- 위 코드를 .dll화 하여 ildasm으로 set(int r)부분을 살펴보면 아래와 같다.

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%207.png)

- `ldarg.0` : 0번째 인자(숨겨진 포인터 this)를 스택에 push
- `ldarg.1` : 1번째 인자인 r에 있는 값을 스택에 push
- `stfld` : 스택에 있는 두 값(this, r)을 pop하여 this.iNumber 멤버변수에 r값을 저장
- 위의 과정을 원래 하던대로 하려면 다음의 과정을 거침
    - Point gildong = new Point();
    - gildong.set(10);
- 그러나, ildasm으로 살펴보면 다음과 같은 과정을 거침
    - set(gildong, 10);

---

- namespace선언 시 아래와 같이 분석됨

![Untitled](C#-mid%20266facf4b88943108510bf0985b3c258/Untitled%208.png)

---

- Base Class Library(`Console`과 같이 기본적으로 존재하는 클래스 들)
    - mscorlib.dll파일 내, System네임스페이스에 작성되어 있음
- 비주얼 베이직 컴파일 방법 : `vbc`

```visual-basic
Module My7
	Sub Main()
		System.Console.WriteLine("Hello, World!")
	End Sub
End Module
```

- My7.vb → My7.exe로 바꾸고 ildasm으로 살펴보면, C#과 거의 동일함을 알 수 있다.
    - 즉, C# / VB 어떤 언어로 작성하든 `어셈블리는 거의 동일`하다.**(JAVA와 가장 다른 점 중 하나)**
- 중간언어(IL)을 도입한 이유
    - 닷넷이 설치되어 있다면 운영체제에 관계없이 실행할 수 있다.
    - 본인이 좋아하는 언어로 프로그래밍 할 수 있다.
- CLR = Common Language Runtime → 런타임, `가상머신`
- 런타임 : 동적 할당된 객체를 자동으로 제거(garbage collection)
- managed code(관리코드) : 닷넷에 의해 객체가 제거되고 관리되는 코드
- JIT(Just - In - Time) 컴파일러
    - CLR구성요소 중 하나
    - (실행될)때 맞춰, 시간에 맞춰, 실행될 때 바로 동작한다.
    - 속도가 빠르다
    - my.exe파일(어셈블리)을 해당 OS에 맞춰진 .exe파일로 JIT(실행될 때) 변환환 후 실행한다.
- 닷넷(.NET) 자료형 구분 2가지
    - 첫 번째 구분 방법
        - `기본` 자료형 : int, double
        - `사용자 정의` 자료형 : class
    - 두 번째 구분 방법
        - `value` 자료형 : int, double 과 같이 new없이 생성되는 것들
        - `reference` 자료형 : new 명령어로 생성되는 것(사용자 정의 클래스, 객체, String)

---

- 델리게이트(delegate) : `함수` `대신` 사용하는 것
    - 델리게이트 존재 이유 : 닷넷(.NET) 응용 프레임워크에서 아직은 만들지 않은 핸들러 함수 xxx를 호출할 수 있도록 하기 위해
    - 닷넷(.NET) 프레임워크에서는 이미 OnClick(), OnDoubleClick()과 같이 핸들러 함수를 연결할 수 있는 코드를 이미 만들어 놓았음
- gildong.XXX() → gildong.Click()으로 바꿔도 아무 이상이 없다면, Click이 바로 XXX의 delegate라고 할 수 있다.
- C++에서의 함수 포인터(delegate) 사용법

```cpp
#include<stdio.h>
void xxx(){
	printf("hello, world!");
}
void main(){
	void (*Click)(); //문법 중요!(맨 왼쪽 : 반환형, 맨 오른쪽 : 매개변수)
	Click = xxx;
	Click();
}
```

- C#에서의 delegate 사용법

```csharp
using System;

class Base
{
    public delegate void DelegateClass();
    public DelegateClass Click = null;
    public Base()
    {
        Click = new DelegateClass(xxx);
    }

    public void xxx()
    {
        Console.WriteLine("클릭!");
    }
}
class Delegate
{
    static void Main()
    {
        Base gildong = new Base();
        gildong.Click();
    }
}
```

- 💯return 값이 double이고, 파라미터가 int형 두 개인 함수를 대신 실행할 수 있는 델리게이트 객체를 만들어보아라!

```csharp
class Base{
	public delegate double DelegateClass(int a, int b);
	public DelegateClass Click = null;
	public Base(){
		Click = new DelegateClass(xxx);
	}
	public double xxx(int a, int b){ ... }
}
```

- 위와 같은 코드로 Click과 xxx를 연결하고, Click()을 실행했을 때, 만약 연결되지 않았을 시 버그가 발생함 → 해결 방법 : OnClick()함수 도입

```csharp
using System;

class Base
{
    public delegate void DelegateClass();
    public DelegateClass Click = null;
    public Base()
    {
        Click = new DelegateClass(xxx);
    }
    public void OnClick()
    {
        if (Click != null) //연결 되었을 경우 Click()함수를 실행하라!
            Click();
    }
    public void xxx()
    {
        Console.WriteLine("클릭!");
    }
}
class Delegate
{
    static void Main()
    {
        Base gildong = new Base();
        gildong.OnClick();
    }
}
```

| Click | 델리게이트, 델리게이트 객체, 델리게이트 인스턴스, 이벤트 |
| --- | --- |
| DelegateClass | 델리게이트 형(type) |
| xxx | 핸들러 함수 |
| OnClick | Click이 null이 아니면 이벤트 Click을 fire하는 함수 |
| OnXxx | xxx가 null이 아니면 이벤트 xxx를 fire하는 함수 |
- Windows OS : 응용프로그램들 형태가 서로 비슷하다(GUI), 모든 프로그램이 멀티태스킹, 이벤트 처리 기능을 기본적으로 가지고 있다.
    - 개발자가 프로그램을 만들 때, 중복 해서 작성해야 하는 코드가 많지 않을까? → 라이브러리로 만들어 놓고 사용하면 좋겠다!
- 위 코드에서 Base클래스를 항상 작성해야 한다고 가정 → Base클래스를 라이브러리로 만들자! → 근데 xxx함수는 프로그래머로 하여금 작성되어야 해서 먼저 작성되어 있으면 안되는 것 인데? → Base클래스에서 xxx와 같은 것 빼서 만든 후, 이를 상속받아 사용하자!(Derived)
    - Base : 비하인드 클래스 / Derived : 프론트 클래스 (Is-a Relation만족)

```csharp
using System;

class Base
{
    public delegate void DelegateClass();
    public DelegateClass Click = null;
    public Base()
    {
        
    }
    public void OnClick()
    {
        if (Click != null)
            Click();
    }
}
class Derived : Base
{
    public Derived()
    {
        Click = new DelegateClass(xxx);
    }
    public void xxx()
    {
        Console.WriteLine("클릭!");
    }
}
class Delegate
{
    static void Main()
    {
        Derived gildong = new Derived();
        gildong.OnClick();
    }
}
```

- Main()함수 안에 있는 내용조차도 작성하기 귀찮다 → 라이브러리화 하자

```csharp
using System;

class Base
{
    public delegate void DelegateClass();
    public DelegateClass Click = null;
    public Base()
    {
        
    }
    public void OnClick()
    {
        if (Click != null)
            Click();
    }
}
class Derived : Base
{
    public Derived()
    {
        Click = new DelegateClass(xxx);
    }
    public void xxx()
    {
        Console.WriteLine("클릭!");
    }
}
class Application //아직은 라이브러리화 못함
{
    public static void Run()
    {
        Derived gildong = new Derived();
        gildong.OnClick();
    }
}

class Delegate
{
    static void Main()
    {
        Application.Run();
    }
}
```

- 위의 코드는 돌아가긴 하는데… Application클래스를 라이브러리화 할 수 있는게 맞나? → 안된다 → 왜? : Base파생 클래스가 Derived가 될지 누가 아느냐! → 이를 해결해보자

```csharp
using System;

class Base
{
    public delegate void DelegateClass();
    public DelegateClass Click = null;
    public Base()
    {
        
    }
    public void OnClick()
    {
        if (Click != null)
            Click();
    }
}
class Derived : Base
{
    public Derived()
    {
        Click = new DelegateClass(xxx);
    }
    public void xxx()
    {
        Console.WriteLine("클릭!");
    }
}
class Application
{
    public static void Run(Base gildong)
    {
        gildong.OnClick();
    }
}

class Delegate
{
    static void Main()
    {
        Application.Run(new Derived());
    }
}
```

- 이젠 Application 클래스도 라이브러리화가 가능하겠다!(Base도 이미 있을 것이며, OnClick도 이미 있을거니까!)
- 마지막으로 이미 라이브러리화가 된 OnClick()함수를 바꿔 쓰고 싶다면? → 가상함수로 만들자

```csharp
//사용 전엔
public virtual void OnClick(){ //virtual도입
	if(Click != null)
		Click();
}
//사용하려면?
public override void OnClick(){
	base.OnClick(); //완전 바꾸는게 아니라 기존것도 사용하고 싶을 때
	Console.WriteLine("이거 하나 추가하려고 멀리 돌아왔다~");
}
```

- 💯💯💯💯따라서 이벤트가 발생했고, 무엇 인가를 하고 싶다면 둘 중에 하나를 해라
    - 핸들러 함수(XXX)를 작성하여 연결
    - 가상함수(OnClick)를 overriding
- 아래는 이 모든 내용을 적용한 포함한 최종 코드이다.

```csharp
using System;

class Base
{
    public delegate void DelegateClass();
    public DelegateClass Click = null;
    public Base()
    {
        
    }
    public virtual void OnClick()
    {
        if (Click != null)
            Click();
    }
}
class Application
{
    public static void Run(Base gildong)
    {
        gildong.OnClick();
    }
}
class Derived : Base
{
    public Derived()
    {
        Click = new DelegateClass(xxx);
    }
    public void xxx()
    {
        Console.WriteLine("클릭!");
    }
    public override void OnClick()
    {
        base.OnClick();
        Console.WriteLine("이거 하나 추가 하려고 멀리 돌아왔다~");
    }
}
class Delegate
{
    static void Main()
    {
        Application.Run(new Derived());
    }
}
```

```csharp
public class Form{}
public class Application{}
//위는 라이브러리로 제공되는 코드들
//아래는 우리가 작성하는 코드들
using System;
public class Derived{}
public class Delegate{Main(){...}}
```

---

- 응용 프레임워크 : 이미 만들어져 있는 거대한 코드 덩어리