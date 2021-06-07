import re

s = input()

if re.search('^(dream|dreamer|erase|eraser)+$'):
    print('YES')
else:
    print('NO')