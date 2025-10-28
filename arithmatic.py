A, B = map(int, input().split())

diff = A - B


if A == B:
    print (1)
elif diff % 2 == 0:
    print (3)
elif diff % 2 != 0:
    print (2)
