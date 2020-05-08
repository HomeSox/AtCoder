S, T = input().split()
A, B = map(int, input().split())
U = input()

nokori = {S:A, T:B}

nokori[U] -= 1

print(str(nokori[S]) + " " + str(nokori[T]))
