side1=float(input("First side of triangle"))
side2=float(input("First side of triangle"))
side3=float(input("First side of triangle"))

if side1 == side2 and side2 == side3:
    print("Triangle is equilateral")
elif side1 != side2 and side2 != side3:
    print("Triangle is Scalene")
else:
    print("Triangle is isoceles")
