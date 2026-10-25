N=int(input("Enter a positive integer N: "))
count=0
print(f"\nDivisors of {N}:")
for i in range(1,N+1):
    if N%i==0:
        print(i)
        count+=1
print(f"\nTotal count of divisors: {count}")
if count==2:
    print(f"{N} is a prime number.")
else:
    print(f"{N} is NOT a prime number.")