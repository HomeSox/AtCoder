from collections import deque

# 変数
N, M = map(int, input().split())
tsutsulist = [] # 筒リスト
for _ in range(M):
    k = int(input())
    tsutsulist.append(deque(map(int, input().split())))

# color IDごとに筒indexを保持（最初の1つのみ）
popable_tsutsu_index_list = [-1 for _ in range(N+1)]
# 取り出し可能な筒indexの組み合わせ
# (筒index1, 筒index2)
popable_color_id_list = deque()

# 初期処理
for i in range(M):
    n = tsutsulist[i][0] # 一番上にある球の色ID

    if popable_tsutsu_index_list[n] == -1: # まだ同じ色の組み合わせが見つかっていない場合
        popable_tsutsu_index_list[n] = i # index=色IDとなる要素に筒IDを保持
    else: # 既に同じ色の組み合わせが見つかっている場合
        popable_color_id_list.append((popable_tsutsu_index_list[n], i)) # 取り出し可能な組み合わせとして、（筒index1, 筒index2）をappend

# シミュレート
# 取り出し可能な組み合わせがなくなるまで
while popable_color_id_list:
    # 取り出し可能な筒の組み合わせをpop
    i1, i2 = popable_color_id_list.pop()

    # 各筒に対する処理
    for i in [i1, i2]:
        # 一番上の球を取り出す
        tsutsulist[i].popleft()

        if tsutsulist[i]: # 筒に球が残っている場合
            append_n = tsutsulist[i][0] # 一番上球の色ID

            if popable_tsutsu_index_list[append_n] == -1: # まだ同じ色の組み合わせが見つかっていない場合
                popable_tsutsu_index_list[append_n] = i # index=色IDとなる要素に筒IDを保持
            else: # 既に同じ色の組み合わせが見つかっている場合
                popable_color_id_list.append((popable_tsutsu_index_list[append_n], i)) # 取り出し可能な組み合わせとして、（筒index1, 筒index2）をappend

# すべての筒に球が残っているかチェックし、答えを出力
ans = 'No' if any(tsutsulist) else 'Yes'
print(ans)
