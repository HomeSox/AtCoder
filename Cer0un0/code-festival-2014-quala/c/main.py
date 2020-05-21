#!/usr/bin/env python3

A, B = map(int, input().split())

before_4 = (A-1) // 4
before_100 = (A-1) // 100
before_400 = (A-1) // 400
after_4 = B // 4
after_100 = B // 100
after_400 = B // 400

before = before_4 - before_100 + before_400
after = after_4 - after_100 + after_400
print(after-before)
