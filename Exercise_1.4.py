def get_tax_bracket(income):
    
    # Handle invalid income
    if income < 0:
        return "Invalid income."

    # Determine tax bracket
    if income < 50000:
        bracket = "Low (10%)"
    elif income < 100000:
        bracket = "Medium (20%)"
    else:
        bracket = "High (30%)"

    # Bonus: ternary check for deduction eligibility
    if income % 2 == 0:
        bracket = bracket + " (Deduction Eligible)"  
    
    else: bracket

    return bracket


# Main code
income = float(input("Enter your income: "))

bracket = get_tax_bracket(income)

if bracket == "Invalid income.":
    print(bracket)
else:
    # Determine tax rate based on bracket
    if "10%" in bracket:
        rate = 0.10
    elif "20%" in bracket:
        rate = 0.20
    else:
        rate = 0.30

    estimated_tax = income * rate
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}")