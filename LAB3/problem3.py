#. Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can,further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases also.
a=int(input("Enter first angle:"))
b=int(input("Enter second angle:"))
c=int(input("Enter third angle:"))
if a<=0 or b<=0 or c<=0:
    print("Invalid angles")
elif a+b+c==180:
    if a<90 and b<90 and c<90:
        print("Acute-angled triangle")
    elif a==90 or b==90 or c==90:
        print("Right-angled triangle")
    else:
        print("Obtuse-angled triangle") 