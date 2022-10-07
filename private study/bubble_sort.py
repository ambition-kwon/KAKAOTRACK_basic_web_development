#버블 정렬
#구현이 가장 간단하지만 시간복잡도가 최악(O(n^2))인 알고리즘
#best, worst, average 모두 O(n^2)
#인접한 두개의 수를 차례로 비교해서 SWAP시키는 방식

#value = [100, 200, 300, 40, 20, 4, 6, 8, 235, 231] # 10개 원소
value = [200,100,50,40,30,20,10,5,2,1] # 10개 원소(최악일 때)

for i in range(len(value) - 1):
    for j in range(len(value) - 1 - i):
        if value[j] > value[j+1]:
            value[j], value[j+1] = value[j+1], value[j]
            print(value)

print(value)