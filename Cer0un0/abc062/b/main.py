#!/usr/bin/env python3

H, W = map(int, input().split())

A = []
for i in range(H):
    A.append(input())

print('#'*(W+2))

for a in A:
    print('#'+a+'#')

print('#'*(W+2))
