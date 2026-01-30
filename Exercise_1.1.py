revenue = float(input("Please enter the revenue amount: "))
cost = float(input("Please enter the cost amount: "))
profit = revenue - cost
margin = 0
if revenue > 0:
    margin = (profit/revenue) * 100
    print
else:
    print("Invalid revenue")