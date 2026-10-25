#READ PROBLEM IN PDF.
s=input("Enter Shape:")
if s=="Square":
    side=int(input("Enter side"))
    area=side**2
elif s=="Rectangle":
    side1=int(input("Enter Length:"))
    side2=int(input("Enter Width:"))
    area=side1*side2
elif s=="Circle":
    r=int(input("Enter Radius of circle:"))
    area=3.14*r**2
elif s=="Triangle":
    base=int(input("Enter Base of triangle:"))
    height=int(input("Enter Height of the triangle"))
    area=0.5*base*height
else:
    area=None
    print("Invalid input!")
if area is not None:
    print(f"{area:.3f}")






