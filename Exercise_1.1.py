revenue = float(input("Please enter the revenue amount: "))
cost = float(input("Please enter the cost amount: "))
profit = round(revenue - cost, 2)
margin = 0
if revenue > 0:
    margin = round((profit/revenue) * 100, 2)
    print(f"Profit = ${profit} | Margin = {margin}%")
else:
    print("Invalid revenue")