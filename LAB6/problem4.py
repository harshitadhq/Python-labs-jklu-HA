num=int(input("Enter a positive integer: "))
octal_str=""
if num==0:
    octal_str="0"
else:
    while num>0:
        remainder=num%8
        octal_str=str(remainder)+octal_str
        num//=8
print("Calculated Octal Equivalent:",octal_str)