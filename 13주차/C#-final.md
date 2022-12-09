# C#-final

## 7장. 델리게이트

- 우리가 중간고사 때 까지 델리게이트를 배우며 복잡한 코드를 작성했던 이유? → 화면을 클릭하면 이벤트가 발생하는 간단한 코드 조차도 백지 상태에서 부터는 작성하기 어려움을 깨닫기 위해 → 이후 `마술사`를 이용하면 얼마나 편리한지를 깨닫기 위해.
- `마술사`를 이용하여 코드를 작성해 보기 전, 중간고사 범위에 포함되었던 델리게이트 코드를 복습할 필요가 있다고 판단. 코드는 아래와 같다.**(단, Base → Form, DelegateClass → EventHandler)**

```csharp
using System;
class Form{
    public delegate void EventHandler();
    public EventHandler Click = null;
    public Form(){

    }
    public virtual void OnClick(){
        if(Click != null){
            Click();
        }
    }
}
class Derived : Form{
    public Derived(){
        Click = new EventHandler(xxx);
    }
    public void xxx(){
        System.Console.WriteLine("Hello, World!");
    }
    public override void OnClick(){
        Form.OnClick();
        System.Console.WriteLine("Click!");
    }
}
class Application{
    public static void Run(Form gildong){
        gildong.OnClick();
    }
}
class My{
    public static void Main(string[] args){
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

- Form과 Application은 우리가 직접 작성할 필요가 없다. 이미 `닷넷 라이브러리`에서 제공한다. 이제는 **참조로 라이브러리를 추가**해 같은 결과를 출력하도록 리팩토링 해보자!
    1. 참조 → System, System.Windows.Forms 2개 추가
    2. using System.Windows.Forms, using System코드 추가
    3. EventHandler 선언 고치기, 핸들러함수(xxx) 고치기, 가상함수(OnClick) 고치기
    4. 완성 코드는 아래와 같다.

```csharp
using System;
using System.Windows.Forms;

class Form{
		//라이브러리 사용하면 명시할 필요없긴 한데, 강의노트에 나와있어서......
    public delegate void EventHandler(**Object sender, EventArgs e**);
}
class Derived : Form{
    public Derived(){
        Click = new EventHandler(xxx);
    }
    public void xxx(**Object sender, EventArgs e**){
        System.Console.WriteLine("Hello, World!");
    }
    **protected** override void OnClick(**EventArgs e**){ //가상함수만 Object sender가 없다.
        Form.OnClick(**e**); //e가 인자로 들어가는 것을 유의할 것.
        System.Console.WriteLine("Click!");
    }
}
class Application{
    public static void Run(Form gildong){
        gildong.OnClick();
    }
}
class My{
    public static void Main(string[] args){
        Application.Run(new Derived());
    }
}
```

- Object `sender`는 어떤 오브젝트가 이 이벤트를 유발시켰는지를 나타낸다.
- EventArgs `e` 는 EventArgs 형으로 이벤트 발생과 관련된 정보를 가지고 있다. (ex. e.X → 이벤트 발생 x좌표, e.Y → 이벤트 발생 y좌표)

---

- 하나의 delegate에 `여러 개의 핸들러 함수 연결`하는 방법은 아래와 같다.(= → +=)
    - 애초에 delegate의 가장 큰 강점 중 하나가 여러 개의 함수를 동시에 발생시킬 수 있다는 것이다.

```csharp
Click += new DelegateClass(xxx);
Click += new DelegateClass(yyy);
Click += new DelegateClass(zzz);
```

- 아래 두 코드는 서로 동일한 결과를 출력하는 코드이다.
- 💯💯💯💯이벤트가 발생했고, 무엇 인가를 하고 싶다면 둘 중에 하나를 해라(중간고사 내용)
    - **핸들러 함수(XXX)를 작성하여 연결**
    - **가상함수(OnClick)를 overriding**

```csharp
class Derived : Form
{
    public Derived()
    {
        Click += newEventHandler(xxx); //디자인 코드
    }
    public void xxx(object sender, EventArgs e)
    {
        System.Console.WriteLine("hello");
    }
}
```

```csharp
class Derived : Form
{
    **protected** override void OnClick(EventArgs e)
    {
        System.Console.WriteLine("hello");
    }
}
```

- ⭐이벤트 처리과정 정리⭐
    - 💯 Run의 역할 : **1. 폼 윈도우 표시, 2. 이벤트 큐 확인하는 무한 루프 발생**

```
*** 프로그램을 실행하면**
1. 닷넷 런타임이 Main함수 호출
2. Main함수에서 Run함수 호출
3. Run함수에서 폼(Form)객체 얼굴 표시
4. 이후 Run함수에서 이벤트 큐를 계속 확인(무한루프)

*** 폼 객체 얼굴 위에서 마우스 클릭(이벤트 발생)**
1. 운영체제에서 Click이벤트를 만들어 이벤트 큐로 넣음
2. 이벤트 큐를 계속 확인하던 Run함수 루프에서 이벤트를 꺼내 확인
3. Click이벤트 임을 알고 OnClick가상함수 호출
4. OnClick에서 Click이 null이 아니면 연결한 핸들러 함수 xxx를 호출

*** 폼 객체를 닫을 경우**
1. 운영체제에서 Close이벤트를 만들어 이벤트 큐로 넣음
2. Run함수 루프에서 이벤트를 꺼내 확인
3. Close이벤트 임을 알고 OnClose가상함수 호출
4. 프로그램 종료
```

- 💯가장 간단한 Form프로그램을 작성하시오
    - Application → System.Windows.Forms
    - Form → System.Windows.Forms

```csharp
using System;
using System.Windows.Forms;

class My{
	public static void Main(){
		Application.Run(new Form());
	}
}
```

---

---

---

- 기존 코드에서 Base → Form, Derived → MainForm, Derived생성자 내 코드 → InitializeComponent()로 추상화
- Form객체 사이즈 변경하면 자동으로 코드 생성 → `코드 생성기`
- InitializeComponent에 속하는 코드 → `디자인 코드`
- 디자인 코드에 속한 Size함수 사용하기 위해 → System.Drawing.dll 참조 추가
- Click += new EventHandler(xxx)는 디자인 코드에 속함
- `핸들러 함수(xxx)`는 `디자인 코드에 속하지 않음`

---

- 최초 My클래스와 MainForm클래스를 구분해서 2개의 파일로 작성하였는데, MainForm클래스 내의 디자인 코드(InitializeComponent)도 분리해서 총 3개의 파일로 운용해보자! → `partial`
- `partial` 키워드는 MainForm.cs / Designer.cs 양쪽 클래스 모두에 붙여줘야 함.
- partal 키워드는 왜 필요할까 → 디자이너가 따로 코드 작성하고, 다른 사람이 또 다른 코드만들어 나중에 합치려고
- partial 키워드를 사용하면 class가 2개 선언되어도 에러 나지 않으며 나중에 합쳐진다.
- 위의 내용을 반영한 최종 코드는 아래의 3개 파일과 같다.

```csharp
using System;
using System.Windows.Forms;

namespace My1201
{
    class My
    {
        public static void Main(string[] args)
        {
            Application.Run(new MainForm());
        }
    }
}
```

```csharp
using System;
using System.Windows.Forms;
using System.Drawing;

namespace My1201
{
    **//사용자 정의 코드**
    partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }
        **//핸들러 함수 -> 디자인 코드 아니다.**
				private void MainForm_Click(object sender, System.EventArgs e)
        {
            Close();
        }
    }
}
```

```csharp
namespace My1201
{
    **//디자인 코드**
    partial class MainForm
    {
        **private** void InitializeComponent()
        {
            this.SuspendLayout();
            this.ClientSize = new System.Drawing.Size(367, 224);
            this.Name = "MainForm";
            this.Click += new System.EventHandler(this.MainForm_Click);
            this.ResumeLayout(false);

        }
    }
}
```

---

### ⭐지금부턴 마술사를 이용한 코딩

- `Text` → 화면상에 표시됨, `Name` → 코드 상에서 객체 식별
- `핸들러` 함수 : **사용자 정의 코드**
- `델리게이트 초기화` 함수 : **디자인 코드**
- 화면에 글자 표기 하는 코드
    - **Click만 사용했을 때 문제점 : 화면 밖으로 나가면 초기화 됨**
    - 해결방법 : **Paint 이벤트 도입**(폼 윈도가 다시 그려져야 할 때마다 자동으로 발생하는 이벤트)

```csharp
namespace My1202
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }
				//얘가 중요 Display는 내가 정의한 함수. 내부 코드를 암기하자
        public void Display(String val, int x, int y)
        {
            **Graphics gildong = this.CreateGraphics();
            gildong.DrawString(val, Font, new SolidBrush(Color.Blue), x, y);**
        }
        private void MainForm_Click(object sender, EventArgs e)
        {
            Display("Hello korea!", 100, 100);
        }

        private void MainForm_Paint(object sender, PaintEventArgs e)
        {
            Display("Hello korea!", 50, 50);
        }
				//얘는 마우스 클릭한 좌표에다가 글자 표기하는 함수. (e.X / e.Y 집중할 것)
				private void MainForm_MouseDown(object sender, MouseEventArgs e)
        {
            Display("Mouse Click!", e.X, e.Y);
        }
    }
}
```

- 글자 표기하는 함수

```csharp
private void MainForm_MouseDown(object sender, MouseEventArgs e)
{
    **Graphics gildong = this.CreateGraphics();
		gildong.DrawString(val, Font, new SolidBrush(Color.Blue), e.X, e.Y);**
}
```

- 사각형 그리는 함수

```csharp
private void MainForm_MouseDown(object sender, MouseEventArgs e)
{
    Graphics gildong = this.CreateGraphics();
    gildong.DrawRectangle(new Pen(Color.Red), e.X, e.Y, 100, 100);
}
```

- 핸들러 함수 제거하는 법 : 속성 창에서 번개모양 클릭 후 핸들러 함수 이름 지우고 ctrl + s눌러 저장
    - 이때 EventHandler 선언 코드(디자인 코드)는 알아서 삭제되지만 MainForm밑에 우리가 직접 내용을 입력한 함수(사용자 정의 코드)는 지워지지 않음 → 혹여나 실수로 힘들게 작성한 코드가 삭제될 수도 있으므로. **즉 핸들러 함수를 확인하고 직접 본인이 삭제하라는 의미**
- 아까도 언급했지만, 이벤트 발생했을 때 무엇인가를 하고 싶으면 2가지 중 하나를 고르면 됨. 지금까지는 핸들러 함수 연결하는 방법으로 했고, 가상함수를 override하는 방법을 사용하려면 여태까지 핸들러함수 정의했던 부분에 override키워드 입력하면 알아서 자동 완성 됨.(아래 그림처럼)
    - 이때 base.OnClick()안에 e를 인자로 줘야함 → base.OnClick(e);

---

- ⭐ 직접 코딩하여 버튼을 추가해 보자 + xxx핸들러 함수도 연결
    - 3개(System, System.Drawing, System.Windows.Forms)는 항상 using하자.

```csharp
public partial class MainForm : Form
{
    Button btn;
    public MainForm()
    {
        InitializeComponent();
    }
		public void xxx(){
			//~~~~~
		}
}
```

```csharp
partial class MainForm
{
    private void InitializeComponent()
    {
        btn = new Button();
        btn.Text = "Close";
        btn.Location = new Point(100, 100);
        btn.Size = new Size(100, 30);
				btn.Click += new EventHandler(this.xxx);
        Controls.Add(btn);
    }
}
```

- ⭐ 마술사 이용하여 버튼을 추가해 보자 + xxx핸들러 함수도 연결
    - Button btn;이 Designer.cs에 선언 된 것을 알 수 있다. 그렇다고 InitializeComponent에 속해 있지는 않다. 근데 InitializeComponent에 Button btn = new Button()과 같이 코딩해도 정상동작하긴한다.

```csharp
public partial class MainForm : Form
{
    public MainForm()
    {
        InitializeComponent();
    }

    private void btn_Click(object sender, EventArgs e)
    {
        Close();
    }
}
```

```csharp
partial class MainForm
{
    private void InitializeComponent()
    {
        this.btn = new System.Windows.Forms.Button();
        this.SuspendLayout();
        // 
        // btn
        // 
        this.btn.Location = new System.Drawing.Point(27, 28);
        this.btn.Name = "btn";
        this.btn.Size = new System.Drawing.Size(225, 77);
        this.btn.TabIndex = 0;
        this.btn.Text = "button1";
        this.btn.UseVisualStyleBackColor = true;
        this.btn.Click += new System.EventHandler(this.btn_Click);
    }
    private Button btn;
}
```

---

## 8장. 모듈과 라이브러리

- Know How→ `Know Where`
- 어떻게 동작하는지 → `어떻게 사용하는지`
    - 💯**모듈은 블랙박스** 이기 때문(내부는 몰라도 사용만 할 수 있으면 됨)
- 마음에 드는 코드 → `코드(클래스) 모듈화`→ `라이브러리`

```csharp
//Phone.cs는 모듈화 된 라이브러리
class Phone{
	public void Say(){
		System.Console.WriteLine("hello, world!");
	}
}
//-------------위는 아예 다른파일-------------//
class My{
	public static void Main(){
		Phone gildong = new Phone();
		gildong.Say();
	}
}
```

- 💯 Phone.cs를 `링크로 추가`
- My `has-a` Phone
    - has-a relation

---

- **Main함수 밖에서 객체 만들었을 경우** 사용방법1(정석)

```csharp
class My{ //Hello.cs를 링크로 추가했다고 가정
	Hello gildong = new Hello();
	public static void Main(){
		My sajang = new My();
		sajang.gildong.Say();
	}
}
```

- **Main함수 밖에서 객체 만들었을 경우** 사용방법2(Static)

```csharp
class My{ //Hello.cs를 링크로 추가했다고 가정
	static Hello gildong;
	public static void Main(){
		gildong = new Hello();
		gildong.Say();
	}
}
```

---

### 💯모듈화 실전예제(Is-A / Has-A)

- MainForm is-a Form(자식클래스는 부모클래스이다 / 남자는 사람이다 / 지구는 행성이다)

```csharp
class Form{
	public int Font;
	public void CreateGraphics(){

	}
}

class MainForm : Form{
	public void MainForm_Click(){
		this.CreateGraphics();
		this.Font = 1;
		System.Console.WriteLine("Hello");
	}
}
```

- MainForm_Click()내부를 추상화 해보자 → Display() → 새로운 클래스로 만들어보자 → MyUtil

```csharp
class Form{
	public int Font;
	public void CreateGraphics(){

	}
}

class MyUtil{
	public void Display(){
		this.CreateGraphics();
		this.Font = 1;
		System.Console.WriteLine("Hello");
	}
}

class MainForm : Form{
	MyUtil util = new MyUtil();
	public void MainForm_Click(){
		util.Display();
	}
}
```

- MyUtil내부에 this들은 어떻게 처리할래? → 클래스를 인자로 넘겨주자

```csharp
class Form{
	public int Font;
	public void CreateGraphics(){

	}
}

class MyUtil{
	public void Display(Form f){
		f.CreateGraphics();
		f.Font = 1;
		System.Console.WriteLine("Hello");
	}
}

class MainForm : Form{
	MyUtil util = new MyUtil();
	public void MainForm_Click(){
		util.Display(this);
	}
}
```

- `Is-A` relation : `부모 클래스`를 만든 후 코드 이동과 상속
- `Has-A` relation : `별도의 클래스`를 만든 후 코드 이동
- 모듈화의 장점(3가지)
    - 내가 만든 모듈을 **재사용** 할 수 있다.
    - 블랙 박스로서의 클래스 모듈을 **이해**할 수 있다.
    - 마음에 드는 코드 일부를 **부품(모듈)으로 만들 수 있다.**

---

## 9장. 메모 프로그램 만들기

- 사용자 정의 코드 : MainForm.cs
- 디자인 코드 : MainForm.Designer.cs
- Form Windows 타이틀 변경 : Text 속성(Name속성이 아닌것에 유의할 것)
- & + 문자 : 바로 실행 단축키 설정
- 메모장 제작시 사용하는 `객체(4개)` → `이벤트는 5개`
    - `Form`
        - **FormClosing함수 사용**
        - **Load함수 사용**
    - `MonthCalendar`
        - **DateChanged함수 사용**
    - `Button`
        - **Click함수 사용**
    - `TextBox`(Multiline : True)
        - **TextChanged함수 사용**

---

- String.Remove(삭제 시작 인덱스(0부터 시작), 삭제할 개수) → 혹시나 시험 대비
    - 안녕하세요.Remove(0,2) → 하세요
    - 안녕하세요.Remove(2,1) → 안녕세요
- Hashtable → using System.Collections
- 데이터 저장시 확장자 : `.dat`
- 아래는 모듈화 이전 메모 프로그램 최종 코드이다(`캐스팅(String, Hashtable) 부분 유의`해서 볼 것)
- **Hashtable과 Array의 차이 :** Key값으로 정수가 아닌 다른 자료형이 올 수 있다는 것!

```csharp
namespace My1205
{
    public partial class MainForm : Form
    {
        Hashtable memoDB = new Hashtable();
        public MainForm()
        {
            InitializeComponent(); //디자인 코드
            //실행시 파일 불러와야 하니 생성자에 만들자(LoadFromFile)
            if (!File.Exists("database.dat"))
            {//이것만으로 예외처리가 된다!
                MessageBox.Show("기존에 저장된 데이터가 없습니다. 새로 시작합니다.");
            }
            else
            {
                FileStream fs = File.Open("database.dat", FileMode.Open, FileAccess.Read);
                BinaryFormatter gildong = new BinaryFormatter();
                **memoDB = (Hashtable)gildong.Deserialize(fs); //Hashtable로 Casting**
                fs.Close();
            }
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void monthCalendar_DateChanged(object sender, DateRangeEventArgs e)
        {
            String temp = monthCalendar.SelectionStart.ToString();
            temp = temp.Remove(10, temp.Length - 10);
            **tbMemo.Text = (String)memoDB[temp]; //String으로 Casting**
        }

        private void tbMemo_TextChanged(object sender, EventArgs e)
        {
            String temp = monthCalendar.SelectionStart.ToString();
            temp = temp.Remove(10, temp.Length - 10);
            memoDB[temp] = tbMemo.Text;
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {//실행 종료시 저장하는 함수(SaveToFile)
            FileStream fs = File.Create("database.dat");
            BinaryFormatter gildong = new BinaryFormatter();
            gildong.Serialize(fs, memoDB);
            fs.Close();
        }

        private void MainForm_Load(object sender, EventArgs e)
        {//최초 실행시 로딩 안되는 현상 해결
            String temp = monthCalendar.SelectionStart.ToString();
            temp = temp.Remove(10, 12);
            **tbMemo.Text = (String)memoDB[temp];**
        }
    }
}
```

---

```csharp
class FileUtil
{
    public void SaveToFile(String path, Hashtable ht)
    {
        FileStream fs = File.Create(path);
        BinaryFormatter gildong = new BinaryFormatter();
        gildong.Serialize(fs, ht);
        fs.Close();
    }
    public Hashtable LoadFromFile(String path)
    {
        if (!File.Exists(path))
        {//이것만으로 예외처리가 된다!, 본 코드가 없다면 런타임 에러 발생한다(최초 실행시엔 파일이 없기 때문)
            MessageBox.Show("기존에 저장된 데이터가 없습니다. 새로 시작합니다.");
            return new Hashtable();
        }
        else
        {
            FileStream fs = File.Open(path, FileMode.Open, FileAccess.Read);
            BinaryFormatter gildong = new BinaryFormatter();
            Hashtable ht = (Hashtable)gildong.Deserialize(fs); //Hashtable로 Casting
            fs.Close();
            return ht;
        }
    }
}
```

```csharp
class HashtableUtil
{
    public void ShowToTextBox(TextBox tb, Hashtable ht, MonthCalendar cal)
    {
        String temp = cal.SelectionStart.ToString();
        temp = temp.Remove(10, temp.Length - 10);
        tb.Text = (String)ht[temp]; //String으로 Casting
    }
    public void SaveToHashtable(TextBox tb, Hashtable ht, MonthCalendar cal)
    {
        String temp = cal.SelectionStart.ToString();
        temp = temp.Remove(10, temp.Length - 10);
        ht[temp] = tb.Text;
    }
}
```

```csharp
namespace My1205
{
    public partial class MainForm : Form
    {
        Hashtable memoDB;
        FileUtil futil = new FileUtil();
        HashtableUtil hutil = new HashtableUtil();
        //Hashtable과 Array의 차이는 Key값으로 정수가 아닌 자료형이 올 수 있다는 것!

        public MainForm()
        {
            InitializeComponent(); //디자인 코드
            //폼 윈도우 실행시 database.dat파일 유무에 따라 없다면 새로운 객체 생성하고
						//파일 존재한다면 기존파일 불러오는 함수
            memoDB = futil.LoadFromFile("database");

        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void monthCalendar_DateChanged(object sender, DateRangeEventArgs e)
        {//database에 저장된 text정보 불러오는 함수
            hutil.ShowToTextBox(tbMemo, memoDB, monthCalendar);
        }

        private void tbMemo_TextChanged(object sender, EventArgs e)
        {//database(Hashtable)로 변경된 텍스트 저장하는 함수
            hutil.SaveToHashtable(tbMemo, memoDB, monthCalendar);
        }

        private void MainForm_FormClosing(object sender, FormClosingEventArgs e)
        {//폼 윈도우 종료시 .dat파일로 데이터 저장하는 함수
            futil.SaveToFile("database", memoDB);
        }

        private void MainForm_Load(object sender, EventArgs e)
        {//database에 저장된 text정보 불러오는 함수
            hutil.ShowToTextBox(tbMemo, memoDB, monthCalendar);
        }
    }
}
```

### 💯FileUtil, HashtableUtil은 모두 MainForm입장에서 Has-A relation을 만족한다.