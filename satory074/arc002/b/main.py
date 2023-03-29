from datetime import datetime, timedelta

S = input()

d = datetime.strptime(S, "%Y/%m/%d")
for i in range(10 ** 8):
    y = d.year
    m = d.month
    dd = d.day

    if y % (m * dd) == 0:
        print(d.strftime("%Y/%m/%d"))
        break

    d += timedelta(days=1)
