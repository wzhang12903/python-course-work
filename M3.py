# PART 1: CONDITIONAL STRUCTURE 
print("=" * 60)
print("GRADING SYSTEM")
print("=" * 60)

try:
    score = float(input("Enter your exam score (0-100): "))
    
    if score >= 90:
        grade = "A"
        message = "Excellent work!"
    elif score >= 80:
        grade = "B"
        message = "Good job!"
    elif score >= 70:
        grade = "C"
        message = "Satisfactory"
    elif score >= 60:
        grade = "D"
        message = "Needs improvement"
    else:
        grade = "F"
        message = "Please seek help from instructor"
    
    print(f"\nYour score: {score}")
    print(f"Your grade: {grade}")
    print(f"Feedback: {message}")
    
except ValueError:
    print("Please enter a valid number.")

# PART 2: FOR LOOP PROCESSING 
print("\n" + "=" * 60)
print("STUDENT ROSTER")
print("=" * 60)

students = ["Wei", "John", "Jinglu", "Lily", "Lucy", "William"]
print("Class roster:")

for i, student in enumerate(students, 1):
    name_length = len(student)
    if name_length <= 4:
        length_description = "short name"
    elif name_length <= 6:
        length_description = "medium name"
    else:
        length_description = "long name"
    
    print(f"  {i}. {student} ({name_length} letters - {length_description})")

total_students = len(students)
print(f"\nTotal students: {total_students}")

# PART 3: WHILE LOOP WITH BREAK/CONTINUE 
print("\n" + "=" * 60)
print("GUESS THE NUMBER GAME")
print("=" * 60)
print("I'm thinking of a number between 1 and 10.")
print("Try to guess it!")

import random
secret_number = random.randint(1, 10)
attempts = 0
max_attempts = 5

while True:
    try:
        guess = int(input("\nEnter your guess (1-10): "))
        attempts += 1
        
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            attempts -= 1  
            continue 
        
        if guess == secret_number:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break  
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        
        if attempts >= max_attempts:
            print(f"\nSorry, you've used {max_attempts} attempts.")
            print(f"The secret number was {secret_number}.")
            break
            
    except ValueError:
        print("Please enter a valid number.")
   

print("\nThanks for playing!")

# PART 4: ADDITIONAL WHILE LOOP EXAMPLE
print("\n" + "=" * 60)
print("PASSWORD VALIDATION")
print("=" * 60)

correct_password = "youaregreat"
attempt = 0
max_attempts_password = 3

while attempt < max_attempts_password:
    password = input("Enter password: ")
    attempt += 1
    
    if password == correct_password:
        print("Access granted! Welcome to the system.")
        break
    else:
        remaining = max_attempts_password - attempt
        if remaining > 0:
            print(f"Incorrect password. You have {remaining} attempt(s) left.")
        else:
            print("Too many failed attempts. Access locked.")
            