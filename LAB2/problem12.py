#. Calculate the gross salary of an employee by taking as input the basic Salary. HRA = 20% of basic salary, TA is 5% of basic salary, and DA is 10% of basic salary. Gross Salary = Basic Salary + HRA + TA + DA.
basic_salary=int(input("Enter basic salary:"))
HRA=basic_salary*0.20
TA=basic_salary*0.05
DA=basic_salary*0.10
gross_salary=basic_salary+HRA+TA+DA
print("Gross Salary:",gross_salary)