import sys
sys.stdin = open("input.txt")

N = input()
answer = 0

for i in N:
   answer += int(i)
print(answer)