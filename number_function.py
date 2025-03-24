import math

from conditions import height

x = 568
print(math.sqrt(x))
print(math.pi)
print(math.floor(99.5678)) #cannot round off number when using floor
print(math.ceil(78.94))#can roundoff number when using the ceil


radius = 56
height = 90

volume =22/7 * radius * radius * height
volume = round(volume,0)
print(volume)
sa = 2 * 22/7  *radius**2 +2 *22/7 *radius *height
print(sa)
sa =2 *22/7 * radius *(radius+height)
sa = round(sa,2)
print(sa)


result =10 +20/5 *6-3
print(result)

