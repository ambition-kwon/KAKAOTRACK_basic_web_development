import math

count = 0
tot = int(input("계산할 행렬의 갯수를 입력하시오: "))
matrix = [[] for i in range(tot+1)] # index를 1부터 사용할 것이기 때문에 tot + 1
memo = [[None] * (tot+1) for _ in range(tot+1)] # 각 부분문제 결과 저장하여 메모이제이션 하기 위한 배열
matrix[0] = [0, 0] # 배열의 1번째 부터 사용할 것이기 때문에
for i in range(tot):
    row = int(input(f"{i+1}번째 행렬의 행(row)값을 입력하시오 : "))
    col = int(input(f"{i+1}번째 행렬의 열(col)값을 입력하시오 : "))
    matrix[i+1].append(row)
    matrix[i+1].append(col)

def Recursive_MatrixChain(i, j):
    global count #재귀가 반복되어도 변수 값을 유지하기 위해
    if memo[i][j] != None:
        return memo[i][j]
    if i == j: 
        memo[i][j] = 0
        return 0 # 재귀 종료조건
    min = math.inf # 가장 큰 수
    for k in range(i, j): # i ~ j-1까지
        count += 1
        temp = Recursive_MatrixChain(i, k) + Recursive_MatrixChain(k+1, j) + (matrix[i][0] * matrix[k][1] * matrix[j][1])
        if temp < min: 
            min = temp
            memo[i][j] = temp
    return min

###### 최소값을 출력 #######
print(Recursive_MatrixChain(1, tot))
###### 최소값을 출력 #######

### 각 부분문제에 대한 결과를 출력 ###
for row in range(1, len(memo)):
    for col in range(1, len(memo[0])):
        print(memo[row][col], end = " ")
    print("\n")
### 각 부분문제에 대한 결과를 출력 ###

### 재귀 호출 횟수를 출력 ###
print(f"함수 재귀 호출 횟수 : {count}번")
### 재귀 호출 횟수를 출력 ###