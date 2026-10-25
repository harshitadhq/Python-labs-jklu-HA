#Write a program that asks the user to enter a whole number of months as input and then converts that amount of time to years and months. The program should use both integer division and the modulus operator.
input_months=int(input("Enter number of months:"))
years=input_months//24
months=input_months%24
print("Years:",years)
print("Months:",months)