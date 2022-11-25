import math

count = 0
tot = int(input("계산할 행렬의 갯수를 입력하시오: "))
matrix = [[] for i in range(tot+1)] # index를 1부터 사용할 것이기 때문에 tot + 1
dp = [[None] * (tot+1) for _ in range(tot+1)] # 각 부분문제 결과 저장하여 메모이제이션 하기 위한 배열
matrix[0] = [0, 0] # 배열의 1번째 부터 사용할 것이기 때문에
for i in range(tot):
    row = int(input(f"{i+1}번째 행렬의 행(row)값을 입력하시오 : "))
    col = int(input(f"{i+1}번째 행렬의 열(col)값을 입력하시오 : "))
    matrix[i+1].append(row)
    matrix[i+1].append(col)

def Repetition_MatrixChain(n):
    global count
    for i in range(1, n+1):
        count += 1
        dp[i][i] = 0
    for size in range(1, n):
        for i in range(1, n-size+1):
            min = math.inf
            for k in range(size):
                count += 1
                temp = dp[i][i+k] + dp[i+k+1][i+size] + (matrix[i][0] * matrix[i+k][1] * matrix[i+size][1])
                if temp < min: min = temp
            dp[i][i+size] = min
    return dp[1][n]


###### 최소값을 출력 #######
print(Repetition_MatrixChain(tot))
###### 최소값을 출력 #######

### 각 부분문제에 대한 결과를 출력 ###
for row in range(1, len(dp)):
    for col in range(1, len(dp[0])):
        print(dp[row][col], end = " ")
    print("\n")
### 각 부분문제에 대한 결과를 출력 ###

### 재귀 호출 횟수를 출력 ###
print(f"반복 호출 횟수 : {count}번")
### 재귀 호출 횟수를 출력 ###