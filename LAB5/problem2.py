#Take a positive integer as input and display the product of its digits. The number can be of any length.
num=input()
product=1
for digit in num:
    product=product*int(digit)
print(product)
4