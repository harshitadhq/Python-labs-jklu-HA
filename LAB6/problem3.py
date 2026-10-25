N=int(input("Enter number of lines N: "))
print("Pattern A")
i=1
while i<=N:
    j=1
    line=""
    while j<=i:
        line+=str(j)
        j+=1
    print(line)
    i+=1

print("Pattern B")
i=1
while i<=N:
    j=1
    line=""
    while j<=i:
        line+="*"
        j+=1
    print(line)
    i+=1

print("Pattern C")
i=1
current_num=1
while i<=N:
    j=1
    line=""
    while j<=i:
        line+=str(current_num)+" "
        current_num+=1
        j+=1
    print(line)
    i+=1