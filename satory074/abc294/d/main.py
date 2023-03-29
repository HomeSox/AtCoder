import collections as cl
import math
from collections import defaultdict, deque

N, Q = map(int, input().split())


called = deque()
not_called = deque(range(1, N+1))
comed = defaultdict(bool)

for _ in range(Q):
    inp = list(map(int, input().split()))

    event = inp[0]

    if event == 1:
        while not_called and comed[not_called[0]]:
            not_called.popleft()

        if not_called:
            person = not_called.popleft()
            called.append(person)

        continue

    if event  == 2:
        x = inp[1]

        comed[x] = True

        continue

    if event == 3:
        while called and comed[called[0]]:
            called.popleft()
        if called:
            print(called[0])