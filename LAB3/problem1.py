#Write a program that prompts the user to enter the centre of a circle (x1, y1), its radius r, and asecond point (x2, y2), and displays whether the second point lies inside, on the boundary of, oroutside the circle. The formula for computing the distance between two points is distance = √[(x2 – x1)2 + (y2 – y1)2].
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
r=int(input("Enter radius:"))
distance=((x2-x1)**2+(y2-y1)**2)**0.5
if distance<r:
    print("Interior point")
elif distance==r:
    print("Boundary point")
else:
    print("Exterior point")
    
