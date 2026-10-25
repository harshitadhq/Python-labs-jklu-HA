#Write a python program to find out if a positive number is a multiple of another positive number or not.
a=int(input())
b=int(input())
if a<0 and b<0:
    print("Invalid input!")
else:
    if a%b==0:
        print("yes")
    else:
        print("no")
        