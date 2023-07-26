A, B = input().split()

c = '1'
r = '2'
p = '3'


if A == c and B == p:
    print('A')
elif A == p and B == c:
    print('B')
elif A == r and B == p:
    print('B')
elif A == p and B == r:
    print('A')
elif A == r and B == c:
    print('A')
elif A == c and B == r:
    print('B')