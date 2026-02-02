def format_greeting(name, title="Customer"): 

    name = name.strip() #remove unnecessary whitespace

    if name == "":
        print("Hello, Valued Customer!") #handling empty name

    name = name.title() #uppercase the first letter of the name

    first_name = name.split()[0] #split the name and take the first name

    print(f"Hello, {first_name} ({title})!") #print the first name with the title

full_name = input("What's your full name? ")

greeting = format_greeting(full_name)
print(greeting)