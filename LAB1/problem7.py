#Write a program to find the area of a circle with radius in the limit 1 to 100 exclusive.
r=int(input("Enter radius of the circle:"))
if r<1 and r>100:
    print("Invalid input!")
else:
    area=3.14*r**2
    print("Area of circle=",area)
    