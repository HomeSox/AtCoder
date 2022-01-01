A = int(input())
B = int(input())
# print(int(f"{A}0{B * 10 // 2}"))

# 解説
# 実は、この問題の制約下では 500,000,000×B+A は必ず「超ラッキーな数」になります。
print(5 * 10 ** 8 * B + A)