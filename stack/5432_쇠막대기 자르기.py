# 쇠막대기 자르기
# stack에 각 막대기의 갯수를 넣어줌 - 1511ms 겁나 오래걸림
import sys
sys.stdin = open('input_5432.txt')

T = int(input())
for tc in range(1, T+1):
    lst = list(input())

    bar = [0] * 1000
    top = -1
    ans = 0
    laser = True

    for i in range(len(lst)):
        if lst[i] == '(':
            laser = True
            top += 1
            bar[top] = 1   # 막대기 한 개

        else:
            if laser is True:   # 레이저인거
                laser = False
                top -= 1
                for j in range(top+1):  # 가지고 있는 막대기 다 잘라줬으니까 다 갯수 +1
                    bar[j] += 1
            else:          # 막대기 빼기
                laser = False
                ans += bar[top]   # 빠진 막대기의 최종 갯수 더하기
                top -= 1

    print(f'#{tc} {ans}')





