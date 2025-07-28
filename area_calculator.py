import math

print('==================')
print('Area Calculator 📐')
print('==================')

print('1) Triangle')
print('2) Rectangle')
print('3) Square')
print('4) Circle')
print('5) Quit')

chosen_shape = int(input("Which shape: "))

if chosen_shape == 1:
    height = int(input("Height: "))
    base = int(input("Base: "))
    area = (height * base) / 2
    print('The area is:', int(area))
if chosen_shape == 2:
    length = int(input("Length: "))
    width = int(input("Width: "))
    area = length * width
    print('The area is:', int(area))
if chosen_shape == 3:
    side = int(input("Side: "))
    area = side * side
    print('The area is:', int(area))
if chosen_shape == 4:
    radius = int(input("Radius: "))
    area = math.pi * (radius * radius)
    print('The area is:', int(area))
if chosen_shape == 5:
    quit