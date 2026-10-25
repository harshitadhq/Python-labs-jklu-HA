#. Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two digits separately. Also, check if the two sums are equal or not.
n=int(input("Enter a 4 digit number:"))
if n<1000 or n>9999:
    print("Invalid input!")
else:
    first_two_sum=n//1000+n//100%10
    last_two_sum=n//10+n%10
    print("Sum of first two digits:",first_two_sum)
    print("Sum of last two digits:",last_two_sum)
    if first_two_sum==last_two_sum:
        print("The two sums are equal.")
    else:
        print("The two sums are not equal.")
