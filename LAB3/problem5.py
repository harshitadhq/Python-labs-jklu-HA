#Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built functions and do not use loops. Also print the position of that digit counted from the left. If the largest digit occurs more than once, print the position of its first occurrence.
n=int(input("Enter a 5-digit numeber:"))
if n<10000 or n>99999:
    print("Invalid input!")
else:
    d1=n//10000
    d2=n//1000%10
    d3=n//100%10
    d4=n//10%10
    d5=n%10
    largest=d1
    position=1
    if d2>largest:
        largest=d2
        position=2
    elif d3>largest:
        largest=d3
        position=3
    elif d4>largest: 
        largest=d4
        position=4
    elif d5>largest:
        largest=d5
        position=5
        print("Largest digit is :",largest)
        print("Position of the largest digit is:",position)

