#Write a program that prompts the user to enter the side of a regular pentagon and displays its area.The formula for computing the area of a pentagon is Area = (5 * s^2) / (4 * tan(π / 5)), where s is the length of a side.
s=int(input("Enter side:"))
a=(5*s**2)/(4*0.72)
print("Area of pentagon:",a)
