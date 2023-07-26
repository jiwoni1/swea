import sys
sys.stdin = open('input.txt')

T = int(input())
for number in range(T):
    numbers = list(map(int, input().split()))
    big = 0

    case_number = 1

    for i in numbers:
        if big < i:
            big =  i

    print(f'#{number+1} {big}')


    