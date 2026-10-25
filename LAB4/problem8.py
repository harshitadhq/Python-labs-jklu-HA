# Find all numbers from 1 through 1000 that end in 6.
num=int(input("Enter number:"))
for num in range(1,1001):
    if num%10==6:
        print(num)