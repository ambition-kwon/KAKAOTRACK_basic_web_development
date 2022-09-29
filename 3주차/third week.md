# 3주차 학습내용

## Pull request를 이용한 remote Repository Merge(복습)

- 단순 `Merge`와 `Pull request` 차이점
    - `Merge` : 로컬 저장소에서 병합을 '먼저' 실시하고, 이후에 병합된 내용을 local에서 remote저장소로 push를 통해 원격 저장소와 동기화 시키게 됨
    - `Pull request` : 원격 저장소(Github)에서 병합을 '먼저' 실시하고, 이후에 병합된 내용을 local에서 fetch후 pull을 통해 로컬 저장소로 불러 오게 됨(굳이 원격에서 먼저하는 이유는, 오픈소스 같은 경우 내가 작업한 내용을 다른 개발자들에게 먼저 review받고 ok sign을 받은 후 merge하는 것이 **예의** 이기 때문)


- branch 생성방법

~~~
git branch issue-1
~~~

- branch 변경방법

~~~
git switch issue-1
~~~

- 현재 브랜치 보는방법(2가지)

~~~
git status //최상단에 현재 브랜치가 표기 됨
git branch //현재 Repository에 존재하는 모든 브랜치 표기 후, 현재 위치한 브랜치가 강조되어 표기 됨
~~~

- 원격에서 수정된 내용이 있는지 확인하는 방법(다른 개발자와 협업시)

~~~
git fetch
~~~

- 로컬에서 먼저 merge후 원격 저장소와 동기화 하는 법`(Method-1)`

~~~
git switch master
git merge issue-1
git push origin master
~~~

- `Rebase`를 통해 더 깔끔하게 `merge`하기`(Method-2)`
    - 그룹 단위가 커지면 커질수록 브랜치도 그에 맞게 늘어날 것이고, 각 개발자들이 모두 새로운 브랜치를 생성하여 `merge`를 하면 GUI에서 표시되는 git 분기이미지가 알아볼 수 없을 정도로 복잡해짐. 이를 방지하려면 `Rebase`라는 명령어를 사용해 깔끔한 분기를 만들 수 있음
    - `rebase`는 `branch`를 잘라서 `master`에 그대로 접합시키는 방법이라고 생각하면 편함, 이것도 개발자들 간에 하나의 **예의**라고 함

~~~
git switch issue-1
git rebase master
~~~

----

## git .ignore관련 문법(복습)

- `git ignore` :git을 통해 버전 관리를 하게 되면 항상 모든 파일이 git status상에 존재하게 된다(추가 시켰든 / 아니든). 하지만 특정 파일은 관리하고 싶지 않을 때가 있는데(실행파일류), 이때 사용하게 되는것이 `.gitignore`이다. 한마디로 말해 **project상에 원하지 않는 파일들을 git에서 제외시킬수 있는 설정파일**이다.

- 조건 : `.gitignore`은 항상 최상위 디렉터리에 존재해야한다.

- 문법

    ~~~
    # : 주석(파이썬과 동일)
    *.py : .py확장자를 가진 모든 파일을 제외
    *.java : java확장자를  가진 모든 파일을 제외
    !important.py : .py가 무시되었지만, important.py만큼은 제외 시키지 않음
    test/ : test폴더 안에있는 모든 파일, 디렉터리 무시하기
    test.java : 루트 디렉터리에 있는 test.java파일 '만'무시
    test/test.java : test디렉터리에 있는 test.java파일 '만'무시
    /test.java : 현재 디렉토리에 있는 /test.java파일은 무시되지만, subDir/test.js 같이 특정 디렉토리 하위에 있는 test.java는 무시되지 않음
    src/*.js : src/ 하위의 .js파일만 무시
    src/**/*.txt : src/ 하위에 존재하는 모든 디렉토리의 .txt 파일을 무시
    /**/*.js : 현재 디렉토리와 그 하위 디렉토리 내에 존재하는 모든 .js 파일을 무시
    ~~~

    >  [.gitignore 자동생성 홈페이지](https://www.toptal.com/developers/gitignore)

- ~~.java파일을 gitignore하고 싶은데, 이미 다른 자바 파일이 commit되어 있으면 제대로 적용되지 않는다. 이때 해결방법은 아래와 같다.

~~~
git rm -r --cached .
git add -A
git commit -m "fixed untracked files"
~~~

-----

## git revert, reset, cherry-pick(복습)

- 협업시 : `reset` <<<<< `revert`
- `reset` : **과거로 되돌리겠다는 내용의 기입 X**, 아예 과거로 회귀가능하며 이력을 남기지 않고 원하는 시점으로 되돌아갈 수 있다.
- `revert` : **과거로 되돌리겠다는 내용의 기입 O**, 이력을 남겨두고 원하는 시점으로 돌아가기때문에 과거로 되돌리는 이유 등을 기입할 수 있다.
- `reset 사용법`**(ID를 기준 저장된 내용으로 되돌린다)**

~~~
git reset --soft [ID] // 커밋이후 변경된 내용들은 존재하되(staging area), commit기록만 말소
git reset --mixed [ID] // 커밋이후 변경된 내용들은 존재하되(working directory), commit기록만 말소
git reset --hard [ID] // 커밋이후 변경된 내용들 기록 자체 말소
~~~

- `revert 사용법`**(ID를 기준으로 -1번째 저장된 내용으로 되돌린다)**
    - 예를들어 현재 "3-2"이고, "3-1" commit으로 revert하려면, 3-2를 기준으로 revert시키면 된다.(revert는 해당 커밋의 영향으로 +,- 된 변화량을 -,+로 변화시키기 때문)
    - 무조건 가장 최신의 커밋부터 revert해줘야 충돌이 나지 않는다. reset과 달리 하나하나 차근차근 내려가야 한다.


~~~
git revert HEAD
git revert HEAD^
git revert HEAD^^
~~~



