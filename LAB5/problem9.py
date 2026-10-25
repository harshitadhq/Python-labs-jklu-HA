number=1244549
d=4
original_number=number
count=0
if number==0:
    if d==0:
        count=1
else:
    while number>0:
        if number%10==d:
            count+=1
        number//=10
print(f"The digit {d} appears {count} times in {original_number}.")
