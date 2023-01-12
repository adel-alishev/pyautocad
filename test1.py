# Importing necessary methods from pyautocad library to draw a polygon:
from pyautocad import Autocad, APoint, aDouble

# os.X_OK: Checks if path can be executed:
from os import X_OK

# Importing math library to compute coordinates for a polygon:
from math import *

acad = Autocad(create_if_not_exists=True)
# 1. Number of vertices for polygon
na = int(input("Введите число точек синусоиды: "))
ms = int(input("Введите масштаб периода 2pi синусоиды: "))
# 2. Center & Radius of Circle
# Center
cc = input("Введите x, y координаты начала синусоиды, например, x, y: ")
ccc = (map(float, cc.split(", ")))
# Converting list to tuple as pyautocad accepts tuple as input
ccct = tuple(ccc)
print('Координаты центра описывающей окружности : ',ccct)
# Radius
rc = float(input("Введите радиус описывающей окружности: "))

# 3. Calculate coordinates
i=0
# Creating an empty list for coordinates
pgonc=[]
for i in range(na):
    x=round(ccct[0]+2*pi*i/na,2)
    y=round(ccct[1]+rc*sin(x),2)
    z=0
    crd = [x, y, z]
    pgonc.extend(crd)
    i += 1
# Addind first point again to complete the loop of polygon
fp = [pgonc[0], pgonc[1], pgonc[2]]
pgonc.extend(fp)
# Converting list to tuple as pyautocad accepts tuple as input
pgont=tuple(pgonc)
print("Координаты полигона: ")
print(pgont)
polygon = aDouble(pgont)
polygond = acad.model.AddPolyline(polygon)
