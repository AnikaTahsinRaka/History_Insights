def peaceful_morning(A, B, C, K):
    if max(A, B, C) - min(A, B, C) > K * 2:
        return "Fight"
    else:
        diff = max(A, B, C) - min(A, B, C)
        if (diff - K * 2) % 3 == 0:
            return "Peaceful"
        else:
            return "Fight"


T = int(input().strip())
for i in range(T):
    A, B, C, K = map(int, input().strip().split())
    result = peaceful_morning(A, B, C, K)
    print("Case %d: %s" % (i + 1, result))
