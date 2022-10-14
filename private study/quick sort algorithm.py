def quick_sort(lists, start, end):
    if start >= end: return #종료조건
    pivot = start
    left = start +1
    right = end
    while left <= right:
        while left <= end and lists[left] <= lists[pivot]:
            left += 1
        while right > start and lists[right] >= lists[pivot]:
            right -= 1
        if left > right:
            lists[right], lists[pivot] = lists[pivot], lists[right]
        else:
            lists[right], lists[left] = lists[left], lists[right]
    quick_sort(lists, start, right - 1)
    quick_sort(lists, right + 1, end)
    return lists