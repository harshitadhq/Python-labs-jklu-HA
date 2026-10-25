#READ IN THE PROBLEMS' FILE.
basic_salary=int(input("Enter basic salary:"))
HRA=basic_salary*0.20
TA=basic_salary*0.05
DA=basic_salary*0.10
gross_salary=basic_salary+HRA+TA+DA
print("Gross Salary:",gross_salary)
if gross_salary<300000:
    tax=0
elif gross_salary<1000000:
    tax=gross_salary*0.10
elif gross_salary<2500000:
    tax=gross_salary*0.20
else:
    tax=gross_salary*0.30
print("Income tax:",tax)
