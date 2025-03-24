def volume_cylinder(radius, height):
    volume = 22/7*radius**2*height
    return volume

print(volume_cylinder(56,18))
print(volume_cylinder(48,10))

v1 = volume_cylinder(height=5,radius=67)#key value argument

def volume_cone(radius, height,decimal=2):#the word decimal is used as an optional
    volume=1/3*22/7*radius**2*height
    volume = round(volume,decimal)
    return volume

print( volume_cone(56,26 ))
print( volume_cone(48,10))