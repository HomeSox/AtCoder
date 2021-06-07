import re

s = input()

if re.search('^(dream|dreamer|erase|eraser)+$', s):
    print('YES')
else:
    print('NO')