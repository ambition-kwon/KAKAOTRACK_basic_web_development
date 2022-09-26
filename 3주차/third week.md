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















