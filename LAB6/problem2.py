N=int(input("Enter positive integer N (1-1000): "))
slot=1
result_str=""
while slot<=1000:
    if slot%N==0:
        if slot%4!=0:
            result_str+=str(slot)+" "
    slot+=1
print(result_str.strip())