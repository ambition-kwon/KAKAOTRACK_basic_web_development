#에라토스테네스의 체(소수판별 알고리즘)
#소수 각각의 판별은 쉽지만, 일정 범위에서 '소수만'판별하기에는 시간이 오래걸림
#위의 문제를 해결하기 위한 알고리즘.
#한번 소수가 된 수의 '배수'는 절대 소수가 될 수 없음을 이용한 방식

import sys
def fastinput():
    return sys.stdin.readline()
max = int(fastinput().rstrip())

judge = [True for i in range(max + 1)] #index 0도 포함되기에 +1
judge[0] = judge[1] = False #0과 1은 기본적으로 판별의미가 없음

for i in range(2, int(max**0.5) + 1): #sqrt(max)까지 인 이유는 수학적 심오한 이유...
    if judge[i] == True: #False인 경우엔 이미 check가 완료 되었다는 뜻
        for j in range(2*i, max+1, i):
            judge[j] = False

for sol in range(max + 1): #출력코드(True일 경우에만)
    if judge[sol] == True:
        print(sol, end = " ")