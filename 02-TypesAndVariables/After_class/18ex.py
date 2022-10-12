import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
heron_base = (a + b + c)/2
area_heron_formula = math.sqrt(heron_base * (heron_base - a)*(heron_base - b)*(heron_base - c))

print(area_heron_formula)
