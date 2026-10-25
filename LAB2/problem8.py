#Write a program that requests the costs and revenue for a company and displays the message “Break even” if the costs and revenue are equal; otherwise, it displays the profit or loss.
costs=float(input("Enter costs:"))
revenue=float(input("Enter revenue:"))
if costs==revenue:
    print("Break even")
elif costs<revenue:
    print("Profit:",revenue-costs)
elif costs>revenue:
    print("Loss:",costs-revenue)
    