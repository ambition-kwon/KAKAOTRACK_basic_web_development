import random as r
import time as t
question1 = [r.randint(1,20000) for i in range(20000)]
question2 = question1.copy()

def insertion_sort1(lists): # 해답을 보지 않은 코드
	for i in range(1, len(lists)):
		target = lists[i]
		j = i
		while(j != 0):
			if (target >= lists[j-1]):
				break
			else:
				lists[j] = lists[j-1]
				j -= 1
		if j != i: lists[j] = target
	return lists

def insertion_sort2(arr): # 구글 복사본
    for end in range(1, len(arr)):
        to_insert = arr[end]
        i = end
        while i > 0 and arr[i - 1] > to_insert:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = to_insert
    return arr
		
start1 = t.time()
print(insertion_sort1(question1))
end1 = t.time()
start2 = t.time()
print(insertion_sort2(question2))
end2 = t.time()
print(end1 - start1)
print(end2 - start2)
