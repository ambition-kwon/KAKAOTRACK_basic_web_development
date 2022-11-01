# Flutter 그림 파일 및 폰트 적용법

- pubspec.yaml파일내의 assets부분 주석해제 후(cmd+/) 아래와 같은 문법으로 기입

```yaml
assets:
	- assets/images/
fonts:
	- family: nanum-gothic
    fonts:
			- asset: assets/fonts/nanum-gothic/NanumGothic.otf
```

- pubspec.yaml파일 수정 후, terminal에서 다음과 같이 입력한다.

~~~
flutter packages get
~~~

- ttf / otf차이
    - ttf : True Type Font의 약자로 1980년 애플에서 만든 폰트의 저장형식, 가장 보편화된 문서를 작성할 때 사용된다.
    - otf : Open Type Font의 약자로 1990년 마이크로소프트와 어도비가 공동으로 개발한 폰트의 저장형식, 그래픽과 같은 고해상도 출력에 주로 사용된다.



