#Take two positive integers as input. Check whether the second number is the exact reverse of the first one. Do not use any inbuilt reverse functions.
a=int(input())
b=int(input())
original=a
reverse=0
while a>0:
    digit=a%10
    reverse=reverse*10+digit
    a=a//10
if reverse==b:
    print("yes")
else:
    print("no")
    
