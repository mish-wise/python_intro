def area(radius):
    result= 22/7*radius**2
    return result
#area of circle,things in the brackets is the parameter

def say_hi(name):
    print("Good Morning",name)


print(area(10))#called a function
print(area(6.7))
print(area(34.67))

say_hi("Kamau")
say_hi("kim")

a1 = area(10.56)
print(round(a1,2))
