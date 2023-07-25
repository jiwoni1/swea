import sys
sys.stdin = open('input.txt')             # input 파일 불러오기

T = int(input())                          # 3줄 (3번) 실행
for number in range(T):                   # 한 줄씩 돌아가며
    numbers = list(map(int, input().split()))  # 한 줄에 있는것들을 공백으로 나눠서 int로 다 바꿈
    big = 0                               # 대소 비교를 위한 변수, 큰 수를 저장할 곳

    for i in numbers:                     # 한 줄에서 (여러개의 수가 들어있는 리스트)
        if big < i:                       # 돌아가면서(for) 대수 비교
            big =  i                      # 크면 big에 큰 수 저장 (갱신)

    print(f'#{number+1} {big}')           # number는 0, 1, 2


    