#알고리즘 수업 - 모래시계 별찍기
num = int(input(""))
blank = num - 2 
for i in range(2 * num - 1):
    if i < num:
        print(" " * i + "*" * (2 * (num - i) -1))
    else :
        print(" " * blank + "*" * (((2 * num) - 1) - (2 * blank)))
        blank -= 1