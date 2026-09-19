import math
# Collects the radius value inputted by user
radius = float(input("Enter radius: "))
# This uses the different formulas required by each value
area = math.pi*radius**2
circ = 2*math.pi*radius
sqrt = math.sqrt(area)
rounded_down= math.floor(area)
rounded_up= math.ceil(area)
# Outputs the calculated outputs
print(f"Area of the garden: {area:.2f} square meters")
print(f"Circumference of the garden: {circ:.2f} meters")
print(f"Square root of the area {sqrt:.2f}")
print(f"Area rounded down: {rounded_down:.2f} square meters")
print(f"Area rounded up: {rounded_up:.2f} square meters")