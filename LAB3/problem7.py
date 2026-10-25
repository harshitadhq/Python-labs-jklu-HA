#Take a 3 digit number as input. Check if it is a Harshad number or not, i.e. whether the number is exactly divisible by the sum of its digits. E.g. 1 + 5 + 3 = 9 and 153 / 9 = 17, so 153 is a Harshad number.
n=int(input("Enter a 3-digit number:"))
if n<100 or n>999:
    print("Invalid input!")
d1=n//100
d2=n//10%10
d3=n%10
sum=d1+d2+d3
if n%sum==0:
    print("Number is a Harshad number.")
else:
    print("Number is not a Harshad number.")
          