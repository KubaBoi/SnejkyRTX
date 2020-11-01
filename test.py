"""
rucni testovani ruznych funkcinalit
neni funkcni prvek aplikace
"""

import math

for index in range(1280*720):
    x = index % 1280
    y = math.floor(index / 1280)
    print(round(x - 1280 / 2), round(y - 720 / 2))