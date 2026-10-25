#Enter the coefficients of two straight lines a1x + b1y = c1 and a2x + b2y = c2 and display their point of intersection. Handle all the cases for invalid input as well as the cases where the two lines are parallel or coincident, and display the solution till exactly 2 decimal places.
x1=int(input())
x2=int(input())
y1=int(input())
y2=int(input())
c1=int(input())
c2=int(input())
if x1==0 and y1==0:
    print("invalid")
elif x2==0 and y2==0:
    print("invalid")
else:
    d=x1*y2-x2*y1
    if d!=0:
        a=(c1*y2-c2*y1)/d
        b=(x1*c2-x2*c1)/d
        print(f"Point of intersection:({a:2f},{b:2f})")
    else:
        if x1*c2==x2*c1 and y1*c2==y2*c1:
            print("These lines are coincident and have infinite solutions")
        else:
            print("These lines are parallel and have no solutions.")