revenue = float(input("Please enter the revenue amount: ")) # Input revenue amount
cost = float(input("Please enter the cost amount: ")) # Input cost amount
profit = round(revenue - cost, 2) # Calculate profit and round to 2 decimal places
margin = 0 # Initialize margin variable

# Calculate margin if revenue is greater than 0, otherwise print an error message
if revenue > 0:
    margin = round((profit/revenue) * 100, 2)
    print(f"Profit = ${profit} | Margin = {margin}%")
else:
    print("Invalid revenue")