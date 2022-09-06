# 1주차 학습내용

## MARKDOWN 사용법 정리

- ### 제목 및 글머리

    ~~~
    # 제목1(주제목)
    ## 제목2(부제목)
    ### 제목3
    #### 제목4
    ##### 제목5
    ###### 제목6
    ~~~

- ### CodeBlock

    ~~~java
    public class Test{
      public static void main(String[] args){
        System.out.println("Hello, World!");
      }
    }
    ~~~

    ~~~c
    #include<stdio.h>
    
    int main(void){
      
      printf("Hello, World!\n");
      
      return 0;
    }
    ~~~

    ~~~~Language
    ~~~Language
    Main Code
    ~~~
    ~~~~

- ### 수평선

    ~~~
    --------------------------
    ~~~

- ### Link(1. [Google](http:www.google.com) 2. 구글 : <www.google.com>)

    ~~~
    1. [홈페이지명](연결주소)
    2. 홈페이지명 : <연결주소>
    ~~~

    

- ### Emphasize

    ~~~
    기울기 : *sentence*
    굵게 : **sentence**
    밑줄 : <u>sentence</u>
    ~~~

> 참조 : [마크다운사용법](https://gist.github.com/ihoneymon/652be052a0727ad59601)

--------------------



## Git 설치(MAC OS)

### 1. Homebrew(패키지 관리자) Download

~~~
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
~~~

### 2. 깃 설치

~~~
brew install git
~~~

### 3. 깃 설치완료 확인

~~~
git --version
~~~

> 참조 : [Homebrew](https://brew.sh/index_ko)

---------------------------------------------



## SourceTree 설치(MAC OS)

### 1. Homebrew GUI 확장 프로그램 설치(Cask)

~~~
brew install cask
~~~

### 2. SourceTree 설치

~~~
brew install --cask sourceTree
~~~

> 참조 : [SourceTree](https://www.sourcetreeapp.com)

---------------------------



## Github Repository 생성 & Local Git과 연동

### 1. 깃허브 접속 및 계정생성([Github](https://github.com/))

### 2. Github Repository 생성

- Repositories -> New -> Repository name 기입 -> `public` -> Create repository

### 3. Local Repository 생성 및 Github 연동(Terminal)

- 빈 디렉터리 생성

    ~~~
    mkdir 디렉터리명
    ~~~

- 생성된 디렉터리로 이동

    ~~~
    cd 디렉터리명
    ~~~

- Git 초기화

    ~~~
    git init
    ~~~

- 최초 사용자 정보 입력

    ~~~
    git config --global user.name "유저이름"
    git config --global user.email "Github계정"
    ~~~

- 연동할 Github Repository의 Path 추가

    ~~~
    git remote add origin Repo_HTTPS
    ~~~

- README.md 파일 생성

    ~~~
    echo 본문내용 >> README.md
    ~~~

- 디렉터리 연동

    ~~~
    git add -A
    git commit -m "messages"
    git push origin master
    ~~~

- Github Access Token입력

    `Windows` : 로그인 창에서 Github 계정으로 로그인

    `Mac OS` : Github -> Settings -> Developer settings -> Personal access tokens -> Generate new token

----------------------



## IntelliJ IDEA 설치 & 학생 License 발급받기(목요일)







---------------



## Programmers 계정 생성(목요일)

























