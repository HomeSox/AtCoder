S = input()
Sr = S[::-1] # 一の位から考える

T = 0 # 部分文字列
mod = [0] * 2019 # mod数え上げ配列
mod[0] += 1 # 「部分文字列T = S」の場合の、 「0 % 2019 = 0」を予めカウント
d = 1 # 桁数
for i, s in enumerate(Sr):
  T += int(s) * d
  T %= 2019
  d = (d * 10) % 2019

  mod[T] += 1

# ペアを合計
# n個から2通り選ぶ（nC2）
mod = [n * (n-1) // 2 for n in mod]
print(sum(mod))