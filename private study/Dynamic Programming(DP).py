#동적 프로그래밍 / 메모이제이션
#한 문제를 여러개의 작은 문제로 나누어 큰 문제를 해결하는 방법
#이때, 결과로 나온 값을 캐싱(메모이제이션)하여 시간속도 단축
#분할정복과의 차이 : 부분 문제 간 중복 여부
#Top-Down(재귀) / Bottom-Up(반복) 2가지로 구현 가능

#Top-Down(재귀)
number = 100
memo = [0] * (number+1)
def top_down_fibo(num, memo):
	if num == 1 or num == 2:
		return 1
	if memo[num] != 0: #혹시 작은 문제에 대한 결과가 이미 도출되었다면,
		return memo[num] #그 값을 그대로 써라~
	memo[num] = top_down_fibo(num-1, memo) + top_down_fibo(num-2, memo)
	return memo[num]

print(top_down_fibo(number, memo))

#Bottom-Up(반복)
memo = [0] * (number+1)
def bottom_up_fibo(num, memo):
	memo[1] = memo[2] = 1
	for i in range(3, num+1):
		memo[i] = memo[i-1] + memo[i-2]
	return memo[num]

print(bottom_up_fibo(number, memo))