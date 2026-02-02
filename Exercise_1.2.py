credit_score = int(input("Please enter your credit score: "))
if credit_score < 300 or credit_score > 850:
    print(f"Your credit score of {credit_score} is invalid.")
elif credit_score < 600:
    print (f"Your credit score of {credit_score} is poor. Hence, your loan is denied. Please seek credit improvement.")
elif credit_score >= 600 and credit_score < 700:
    print (f"Your credit score of {credit_score} is fair. Hence, your loan can be approved conditionally. Please seek credit improvement.")
elif credit_score >= 700 and credit_score < 750:
    print (f"Your credit score of {credit_score} is good. Hence, your loan is approved with review. Interest Rate - Low")
else:
    print (f"Your credit score of {credit_score} is excellent. Hence, your loan is approved. Interest Rate - Low")