import numpy as np
from math import *
# Importing necessary methods from pyautocad library to draw a polygon:
from pyautocad import Autocad, APoint, aDouble

acad = Autocad(create_if_not_exists=True)

pgonc=[]

k = int(input("Введите число точек синусоиды: "))
ms = float(input("Введите длину периода: "))
cc = input("Введите x, y координаты начала синусоиды, например, x, y: ")
Amp = float(input("Введите амплитуду синусоиды: "))
f = float(input("Введите частоту синусоиды: "))
ccc = (map(float, cc.split(", ")))
ccct = tuple(ccc)
for i in range(k+1):
    x=round(ccct[0]+ms*i/k,2)
    y=round(ccct[1]+Amp*sin(2*pi*x/f/ms),2)
    z=0
    crd = [x, y, z]
    print(crd)
    pgonc.extend(crd)
    i += 1
fp = [pgonc[0], pgonc[1], pgonc[2]]
pgonc.extend(fp)
pgont=tuple(pgonc)
polygon = aDouble(pgont)
polygond = acad.model.AddPolyline(polygon)