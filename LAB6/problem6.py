N=int(input("Enter upper limit N: "))
print("Armstrong numbers between 1 and",N,":")
num=1
while num<=N:
    temp=num
    digits=0
    while temp>0:
        digits+=1
        temp//=10
    temp=num
    total_sum=0
    while temp>0:
        digit=temp%10
        power=1
        count=0
        while count<digits:
            power*=digit
            count+=1
        total_sum+=power
        temp//=10
    if total_sum==num:
        print(num)
    num+=1