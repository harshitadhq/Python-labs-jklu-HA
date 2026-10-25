#A supermarket sells apples for $2.50 per pound. Write a cashier’s program that requests the number of pounds and the amount of cash tendered as input and displays the change from the transaction. If the cash is not enough, the message “You owe $x.xx more.” should be displayed, where $x.xx is the difference between the total cost and the cash.
pounds=int(input("enter number of pounds:"))
cost=pounds*2.50
cash=float(input("Enter cash tendered:"))
if cash>cost:
    print("Change:",cash-cost)
elif cash<cost:
    print("you owe $",cost-cash,"more.")
    