import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
answer = sorted(numbers) # numbers.sort()해서 print(numbers)해도됨 - 원본이 바뀜
print(answer[N//2])      # 파이썬 리스트 인덱싱이 0부터 시작해서 N//2가 맞음

