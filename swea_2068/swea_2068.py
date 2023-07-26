import sys
sys.stdin = open('input.txt')

T = int(input)
for line in range(T):
    line = map(int, input().split())

    max = line[0]

    for i in line:
        if i > max: