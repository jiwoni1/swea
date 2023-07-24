import sys 
sys.stdin = open('input_file')

number = 0

t = int(input())
for line in range(t):
    line = map(int, input().split())

    case = 0

    for i in line:
        if i % 2 == 1:
            case += i
    number += 1
    print(f'#{number}, {case}')