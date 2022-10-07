#선택 정렬
#구현이 버블정렬보다도 간단하지만 시간복잡도가 최악(O(n^2))인 알고리즘
#그래도 버블정렬보단 빠르다
#best, worst, average 모두 O(n^2)
#i = 0자리 부터시작해 끝까지 min값 찾은 후, i위치에 fix시키는 방식
#즉, index기준 0~끝의 min 찾고 기존 0자리와 swap,
#index기준 1~끝의 min 찾고 기존 1자리와 swap,
##index기준 2~끝의 min 찾고 기존 2자리와 swap 반복하는 방법임

import sys
def finput():
   return sys.stdin.readline()

array = [9, 6, 7, 3, 5, 10, 23]

for i in range(len(array) -1): #맨 마지막은 신경안써도 돼서 - 1회차
   min = 99999
   min_index = 99999
   for j in range(i, len(array)): #fix된 인덱스는 범위에 포함X
      if array[j] < min:
         min = array[j]
         min_index = j
   if i != min_index: #min자리와 기존 자리가 같지 않을 경우만 swap
      array[i], array[min_index] = array[min_index], array[i]

print(array)