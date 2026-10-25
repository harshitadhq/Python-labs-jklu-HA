#Find the largest of 3 numbers using nested if else condition.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if a>b:
    if a>c:
        larger=a
    else:
        larger=c
else:
    if b>c:
        larger=b
    else:
        larger=c
print("Largest number is:",larger)