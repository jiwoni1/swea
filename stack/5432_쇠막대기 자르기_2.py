# 쇠막대기 자르기
import sys
sys.stdin = open('input_5432.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(input())

    cnt = 0
    ans = 0
    laser = True

    for i in range(len(lst)):
        if lst[i] == '(':
            laser = True
            cnt += 1

        else:
            if laser is True:   # 레이저
                laser = False
                cnt -= 1
                ans += cnt     # 자른 갯수를 더해주는 것임

            else:
                laser = False
                cnt -= 1   # 막대기 하나 안녕
                ans += 1   # 마지막 막대기 부분 더해줌

    print(f'#{tc} {ans}')
