N=int(input())
P=int(input())
if N<=0 or P<=0:
    print("Invalid input!")
else:
    result=1
    count=1
    while count<=P:
        result=result*N
        count+=1
print(result)