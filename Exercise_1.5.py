# Prompt for product name
name = input("What's the product name? ")

# Clean the input
name = name.strip().lower()

# Categorize using match
match name:
    case "electronics" | "gadget" | _ if name.startswith("tech"):
        category = "High Margin"
    case "clothing" | "apparel":
        category = "Medium Margin"
    case "food" | "grocery":
        category = "Low Margin"
    case _:
        category = "Uncategorized - Review Needed"

# Print result
print(f"Product: {name} | Category: {category}")

#Helper function
def is_profitable(revenue, cost):
    return revenue > cost

def main():
    # Get inputs
    revenue = float(input("Enter revenue: "))
    cost = float(input("Enter cost: "))
    product = input("Enter product category: ").strip().lower()

    # Determine category using match
    match product:
        case "electronics" | "gadget" | _ if product.startswith("tech"):
            category = "High Margin"
        case "clothing" | "apparel":
            category = "Medium Margin"
        case "food" | "grocery":
            category = "Low Margin"
        case _:
            category = "Uncategorized"

    # Check profitability
    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profit: {profit}")

        match category:
            case "High Margin":
                print("Suggestion: Reinvest")
            case "Medium Margin":
                print("Suggestion: Expand cautiously")
            case "Low Margin":
                print("Suggestion: Optimize costs")
            case _:
                print("Suggestion: Review product strategy")
    else:
        print("Not profitable. Do not invest.")