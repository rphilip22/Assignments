credit_score = int(input("Please enter your credit score: "))
if credit_score < 300 or credit_score > 850:
    print(f"Your credit score of {credit_score} is invalid.")
elif credit_score < 600:
    print (f"Your credit score of {credit_score} is poor. Hence, your loan is denied.")
elif credit_score >= 600 and credit_score < 700:
    print (f"Your credit score of {credit_score} is fair. Hence, your loan can be approved conditionally.")
elif credit_score >= 700 and credit_score < 750:
    print (f"Your credit score of {credit_score} is good. Hence, your loan is approved with review.")
else:
    print (f"Your credit score of {credit_score} is excellent. Hence, your loan is approved.")