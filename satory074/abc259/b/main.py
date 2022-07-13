import collections as cl
import math
import numpy as np


a, b, d = map(int, input().split())

deg = np.deg2rad(d)

cos = np.cos(deg)
sin = np.sin(deg)

rot_x = (a * cos) - (b * sin)
rot_y = (a * sin) + (b * cos)

print(rot_x, rot_y)
