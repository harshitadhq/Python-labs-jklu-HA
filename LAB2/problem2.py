#If the lengths of the two parallel sides of a trapezoid are X meters and Y meters, respectively, and the height is H meters, what is the area of the trapezoid? Write Python code to output the area by taking X, Y and H as input from the user.
a=int(input("First side of trapezoid:"))
b=int(input("Second side of trapezoid:"))
h=int(input("height of trapezoid:"))
area=((a+b)/2)*h
print("Area of trapezoid is:",area)
