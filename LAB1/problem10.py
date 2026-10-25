#Write a python program to check the validity of a 4-digit pin code.
pin=int(input("Enter your pin:"))
if pin<1000 or pin>9999:
    print("Invalid pin code!")
else:
    print("Valid pin code!")