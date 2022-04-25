"""
Test 1
1
1 1000000
Case #1: 534358
974.489ms
"""

import time

t = int(input())
for test_case in range(1, t + 1):
    A, B = [int(_) for _ in input().split()]
    interesting = 0
    start = time.time()

    for num in range(A, B + 1):
        s, p = 0, 1
        while num:
            digit = num % 10
            num = num // 10
            s += digit
            p *= digit
        if p % s == 0:
            interesting += 1
    end = time.time()
    print(f"Case #{test_case}: {interesting}")
    print(end - start)
