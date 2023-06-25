import collections as cl
import math

N = int(input())
S = input()

stack = []
n_stack_in_kakko = 0
for s in S:
    if s == ')':
        if n_stack_in_kakko == 0:
            stack.append(s)
            continue

        while stack and stack[-1] != '(':
            stack.pop()

        if stack:
            stack.pop()

        n_stack_in_kakko -= 1
    else:
        if s == '(':
            n_stack_in_kakko += 1

        stack.append(s)

print(''.join(stack))