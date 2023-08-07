N = int(input())

# 27 = aa
# 123456789 = jjddja

# Nを26進数でprint
# 26進数の桁数はlog26(N)で求められる
# 26進数の各桁はNを26で割った余りで求められる
# 26進数の各桁は文字に変換できる
# 26進数の各桁を逆順にprint
# 26進数の各桁を逆順にprintしたものを文字列に変換する
# 26進数の各桁を逆順にprintしたものを文字列に変換したものをprint
print(''.join([chr(ord('a') + (N % 26)) for N in range(N)]))