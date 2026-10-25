#Write a program that reads n integers and finds their sum.
n=int(input())
total_sum=0
for _ in range(n):
    number=int(input())
    total_sum+=number
print(total_sum)