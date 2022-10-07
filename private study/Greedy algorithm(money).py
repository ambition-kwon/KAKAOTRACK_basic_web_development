#그리디 알고리즘(거스름돈 문제)
#매순간 최선의 선택이 최선의 결과를 가져오는 알고리즘
#동전의 종류 / 총 금액 / 지불 못하는 돈(나머지)
#######가장중요한 것########
#정당성 검토 : 본 거스름돈 문제가 그리디인 이유는
#큰 단위의 동전은 항상 작은 단위 동전의 배수이기 때문이다.

money = [500, 100, 50, 10]
count = list()
money.sort(reverse = True) #내림차순 정렬
tot = 1492 #지불해야 하는 돈
for coin in money:
   if tot // coin > 0:
      count.append(tot//coin)
      tot -= coin * (tot//coin)
   else: pass

print(count) #금액 별 사용 갯수
print(sum(count)) #총 동전 사용 갯수
print(tot) #나머지 돈