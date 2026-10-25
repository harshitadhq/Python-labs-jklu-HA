#READ THE PROBLEMS FILE
income=int(input("Enter taxable income:"))
if income<=20000:
    tax=income*0.02
elif income<=50000:
    tax=400+(income-20000)*0.025
else:
    tax=1150+(income-50000)*0.035
print("Set tax:",tax)
