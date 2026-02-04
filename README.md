## Exercise_1.1


## Exercise_1.2


## Exercise_1.3
Description: This program prompts the user for their full name and prints a formatted greeting.  
It demonstrates basic Python concepts such as functions, string manipulation, default parameters, and user input.

The program ensures the name is cleaned and formatted consistently before generating the greeting.

Features
- Prompts the user for their full name
- Strips leading and trailing whitespace
- Capitalizes the name correctly
- Uses only the first name if multiple names are entered
- Handles empty input gracefully
- Uses a function with a default parameter

How the Program Works
1. The user is asked to enter their full name.
2. The `format_greeting` function:
   - Removes extra whitespace
   - Checks for empty input
   - Converts the name to title case
   - Extracts the first name
   - Returns a formatted greeting
3. The greeting is printed to the console.

Sample Run

Input:

What's your full name?   john doe

Output:

Hello, John (Customer)!

## Exercise_1.4
Description: This program calculates a user's tax bracket and estimated tax based on their income.  
It demonstrates core Python concepts including functions, conditionals, return values, user input, and basic arithmetic.

The program also includes a bonus feature that marks users as deduction-eligible if their income is an even number.

Features
- Prompts the user to enter their income
- Validates income input (rejects negative values)
- Determines tax bracket using conditional logic
- Calculates estimated tax based on the bracket
- Uses a function to encapsulate tax logic
- Demonstrates a ternary conditional expression (bonus)

How the Program Works
1. The user is prompted to enter their income.
2. The `get_tax_bracket` function:
   - Checks for invalid (negative) income
   - Determines the correct tax bracket:
     - Less than 50,000 → Low (10%)
     - 50,000 to less than 100,000 → Medium (20%)
     - 100,000 or more → High (30%)
   - Adds a deduction eligibility note if the income is even
3. The main code:
   - Calls the function
   - Determines the tax rate based on the returned bracket
   - Calculates and prints the estimated tax

Sample Run

Input:

Enter your income: 50000

Output:

Your bracket: Medium (20%) (Deduction Eligible). Estimated tax: 10000.0

## Exercise_1.5
Description: This project categorizes products based on their name and determines business decisions using revenue and cost data.  
It demonstrates Python fundamentals including string manipulation, pattern matching with `match`, functions, conditionals, and basic business logic.

The project is divided into two parts:
1. Product margin categorization
2. Bonus business decision tool

Part 1: Product Margin Categorization

Overview: The program prompts the user for a product name, cleans the input, and categorizes the product into a margin level using Python’s `match` statement.

Features
- Prompts for a product name
- Strips leading and trailing whitespace
- Converts input to lowercase for consistent matching
- Uses `match` with multiple cases and conditions
- Assigns a margin category
- Prints a formatted summary

Categorization Rules
- **High Margin**
  - `"electronics"`
  - `"gadget"`
  - Any product name starting with `"tech"`
- **Medium Margin**
  - `"clothing"`
  - `"apparel"`
- **Low Margin**
  - `"food"`
  - `"grocery"`
- **Uncategorized**
  - Any other product name

Sample Run

Input:

What's the product name?  Tech Phone  

Output:

Product: tech phone | Category: High Margin
