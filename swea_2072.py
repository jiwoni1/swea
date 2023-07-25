import sys 
sys.stdin = open('input_file')     # input파일 불러오기

number = 0                         # '#1'을 위한 숫자 정의

t = int(input())                   # 맨 처음 몇 줄인지 입력
for line in range(t):              # 반복문을 사용해서 여러 줄을 입력하게 함
    line = map(int, input().split())  # 공백을 기준으로 input()된 것을 모두 int함수 적용

    case = 0                       # 값을 저장할 곳

    for i in line:                 # 한 줄에서 순회하며 홀수 판단
        if i % 2 == 1:
            case += i
    number += 1                    # 첫번째 for의 마지막에 더해주기 3번!
    print(f'#{number}, {case}')