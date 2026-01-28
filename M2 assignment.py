# Assignment 2 – variables and expressions


budget = 2500.50          # Monthly budget (float)
rent = 1200               # Monthly rent (int)
groceries = 450.75        # Grocery expenses (float)

total_expenses = rent + groceries                     # Addition
remaining_budget = budget - total_expenses            # Subtraction
rent_percentage = (rent / budget) * 100               # Division and multiplication
weekly_budget = budget / 4                            # Division

# Define string variables
name = "Wei Zhang"
city = "Clifton Park"
job_title = "Electronics Engineer"

# String concatenation
introduction = f"My name is {name} and I live in {city}."

# String slicing
first_name = name[:3]          # "Wei"
last_name = name[4:]           # "Zhang"

# String methods
job_upper = job_title.upper()                              # Uppercase
city_lower = city.lower()                                  # Lowercase
name_contains_john = "John" in name                        # Check substring
sentence = "I enjoy hiking and soccer."
word_list = sentence.split()                               # Split into words
sentence_length = len(sentence)                            # String length

# Boolean comparisons
can_afford_rent = budget >= rent                          # Comparison 1
is_budget_tight = remaining_budget < 500                  # Comparison 2
same_city = city == "Albany"                              # Comparison 3
is_expensive_rent = rent > 1000                           # Comparison 4
is_name_long = len(name) > 10                             # Comparison 5



print("<FINANCIAL CALCULATIONS>")
print(f"1. My monthly budget is ${budget:.2f}")
print(f"2. Rent costs ${rent:.2f} and groceries cost ${groceries:.2f}")
print(f"3. Total expenses are ${total_expenses:.2f}")
print(f"4. Remaining budget after expenses is ${remaining_budget:.2f}")
print(f"5. Rent represents {rent_percentage:.1f}% of my budget")
print(f"6. My weekly budget allowance is ${weekly_budget:.2f}")


print("<PERSONAL INFORMATION>")
print(f"1. {introduction}")
print(f"2. First name: {first_name}, Last name: {last_name}")
print(f"3. My profession as {job_title} in uppercase: {job_upper}")
print(f"4. City name in lowercase: {city_lower}")
print(f"5. My name contains 'John': {name_contains_john}")
print(f"6. The sentence '{sentence}' has {sentence_length} characters")
print(f"7. Words in the sentence: {word_list}")


print("<BOOLEAN COMPARISONS>")
print(f"1. Can I afford my rent? {can_afford_rent}")
print(f"2. Is my budget tight (less than $500 remaining)? {is_budget_tight}")
print(f"3. Do I live in Albany? {same_city}")
print(f"4. Is my rent expensive (over $1000)? {is_expensive_rent}")
print(f"5. Is my name longer than 10 characters? {is_name_long}")


print("<PROGRAM SUMMARY>")
print("This program demonstrates Python fundamentals:")
print("• Three numeric variables with arithmetic operations (+, -, *, /)")
print("• String manipulation (concatenation, slicing, methods)")
print("• Boolean expressions with comparison operators (>=, <, ==, >)")
print("• Formatted output using f-strings and clear labeling")