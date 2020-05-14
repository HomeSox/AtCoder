s = input()
t = input()

def is_ok(s1, s2):
  if s1 == '@' and s2 == '@':
    return True
  
  if s1 == '@' and s2 != '@':
    return (s2 in 'atcoder')
  
  if s1 != '@' and s2 == '@':
    return s1 in 'atcoder'
  
  if s1 != '@' and s2 != '@':
    return s1 == s2
  
  return False

for s_, t_ in zip(s, t):
  if not is_ok(s_, t_):
    print('You will lose')
    break
else:
  print('You can win')
