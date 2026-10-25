#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and years of service and print the net bonus amount.
salary=int(input("Enter salary:"))
service=int(input("Enter years of service:"))
if service>=5:
    bonus=salary*0.05
else:
    bonus=0
    print("Bonus:",bonus)
