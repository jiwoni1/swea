# 백만 장자 프로젝트
import sys
sys.stdin = open('input_1859.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    adv = 0
    max_p = 0

# 앞에서부터 하면 뒤에 계속 더 큰 수가 나와서 너무 복잡해짐, 뒤에서부터 하면 지금보다 큰 수가 나오기 전까지 빼면 돼
    for i in range(N-1, -1, -1):
        if max_p < price[i]:    # 큰 값을 따로 변수로 지정해서 저장해줌
            max_p = price[i]
        else:    # 작은 값이 나오면 저장된 값에서 가격 빼서 더해주기
            adv += max_p - price[i]  # 매입값 더해주기!

    print(f'#{tc} {adv}')


