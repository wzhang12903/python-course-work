"""
Unit Converter Program
This program demonstrates functions, variable scope, and error handling
by converting between different units of measurement.
"""

# ===================== GLOBAL VARIABLES =====================
# Global conversion constants (accessible throughout the program)
CONVERSION_FACTORS = {
    "length": {"miles_to_km": 1.60934, "km_to_miles": 0.621371},
    "temperature": {"freezing_c": 0, "freezing_f": 32},
    "weight": {"lbs_to_kg": 0.453592, "kg_to_lbs": 2.20462}
}
app_name = "Unit Converter Pro"
version = "1.0"

# ===================== FUNCTION 1: TEMPERATURE CONVERSION =====================
def celsius_to_fahrenheit(celsius, round_result=True):
    """
    Convert Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
        round_result (bool): Whether to round the result (default True)
    
    Returns:
        float: Temperature in Fahrenheit, rounded to 2 decimals if round_result=True
    """
    fahrenheit = (celsius * 9/5) + 32
    
    if round_result:
        return round(fahrenheit, 2)
    return fahrenheit

# ===================== FUNCTION 2: DISTANCE CONVERSION =====================
def miles_to_kilometers(miles, decimals=2):
    """
    Convert miles to kilometers.
    
    Args:
        miles (float): Distance in miles
        decimals (int): Number of decimal places for result (default 2)
    
    Returns:
        float: Distance in kilometers, rounded to specified decimals
    """
    km = miles * CONVERSION_FACTORS["length"]["miles_to_km"]
    return round(km, decimals)

def kilometers_to_miles(km, decimals=2):
    """
    Convert kilometers to miles.
    
    Args:
        km (float): Distance in kilometers
        decimals (int): Number of decimal places for result (default 2)
    
    Returns:
        float: Distance in miles, rounded to specified decimals
    """
    miles = km * CONVERSION_FACTORS["length"]["km_to_miles"]
    return round(miles, decimals)

# ===================== FUNCTION 3: WEIGHT CONVERSION =====================
def pounds_to_kilograms(pounds, decimals=2):
    """
    Convert pounds to kilograms.
    
    Args:
        pounds (float): Weight in pounds
        decimals (int): Number of decimal places for result (default 2)
    
    Returns:
        float: Weight in kilograms, rounded to specified decimals
    """
    kg = pounds * CONVERSION_FACTORS["weight"]["lbs_to_kg"]
    return round(kg, decimals)

def kilograms_to_pounds(kg, decimals=2):
    """
    Convert kilograms to pounds.
    
    Args:
        kg (float): Weight in kilograms
        decimals (int): Number of decimal places for result (default 2)
    
    Returns:
        float: Weight in pounds, rounded to specified decimals
    """
    pounds = kg * CONVERSION_FACTORS["weight"]["kg_to_lbs"]
    return round(pounds, decimals)

# ===================== FUNCTION 4: INPUT VALIDATION =====================
def get_valid_number(prompt, allow_negative=True):
    """
    Get a valid number from user input with error handling.
    
    Args:
        prompt (str): Message to display to user
        allow_negative (bool): Whether negative numbers are allowed (default True)
    
    Returns:
        float: Valid number entered by user
    """
    while True:
        try:
            value = float(input(prompt))
            
            # Check if negative numbers are allowed
            if not allow_negative and value < 0:
                print("Please enter a non-negative number.")
                continue
                
            return value
        except ValueError:
            print("Invalid input! Please enter a number (e.g., 10.5).")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            exit()

# ===================== DEMONSTRATING VARIABLE SCOPE =====================
def demonstrate_scope():
    """
    Show the difference between local and global variables.
    """
    local_var = "I'm LOCAL to this function"
    global app_name  # Accessing global variable
    
    print("\n" + "=" * 50)
    print("VARIABLE SCOPE DEMONSTRATION")
    print("=" * 50)
    print(f"Inside function - Local variable: {local_var}")
    print(f"Inside function - Global variable (app_name): {app_name}")
    
    # Trying to modify global variable without 'global' keyword
    # This creates a new local variable instead
    version = "modified locally"
    print(f"Inside function - Attempt to modify global 'version': {version}")
    
    # Accessing the REAL global version
    import sys
    print(f"Inside function - Actual global 'version' is still: {sys.modules[__name__].version}")

# ===================== MAIN PROGRAM =====================
def main():
    """Main program loop with menu interface."""
    
    # Local variable (only exists in main())
    conversion_count = 0
    
    print(f"\n{'=' * 60}")
    print(f"Welcome to {app_name} (v{version})")
    print(f"{'=' * 60}")
    
    while True:
        print("\nSelect conversion type:")
        print("1. Temperature (Celsius ↔ Fahrenheit)")
        print("2. Distance (Miles ↔ Kilometers)")
        print("3. Weight (Pounds ↔ Kilograms)")
        print("4. Demonstrate variable scope")
        print("5. Exit")
        
        choice = get_valid_number("Enter your choice (1-5): ", allow_negative=False)
        
        # ==================== TEMPERATURE CONVERSION ====================
        if choice == 1:
            print("\n--- Temperature Conversion ---")
            try:
                celsius = get_valid_number("Enter temperature in Celsius: ", allow_negative=True)
                
                # Demonstrate default parameter (round_result=True)
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C = {fahrenheit}°F")
                
                # Demonstrate optional rounding
                precise = celsius_to_fahrenheit(celsius, round_result=False)
                print(f"Precise value (no rounding): {precise}°F")
                
                conversion_count += 1
                
            except Exception as e:
                print(f"Unexpected error during temperature conversion: {e}")
        
        # ==================== DISTANCE CONVERSION ====================
        elif choice == 2:
            print("\n--- Distance Conversion ---")
            print("a) Miles to Kilometers")
            print("b) Kilometers to Miles")
            
            sub_choice = input("Choose option (a/b): ").lower()
            
            try:
                if sub_choice == 'a':
                    miles = get_valid_number("Enter miles: ", allow_negative=False)
                    km = miles_to_kilometers(miles)
                    print(f"{miles} miles = {km} kilometers")
                    
                elif sub_choice == 'b':
                    km = get_valid_number("Enter kilometers: ", allow_negative=False)
                    miles = kilometers_to_miles(km)
                    print(f"{km} kilometers = {miles} miles")
                    
                else:
                    print("Invalid option. Please enter 'a' or 'b'.")
                    continue
                    
                conversion_count += 1
                
            except Exception as e:
                print(f"Error during distance conversion: {e}")
        
        # ==================== WEIGHT CONVERSION ====================
        elif choice == 3:
            print("\n--- Weight Conversion ---")
            print("a) Pounds to Kilograms")
            print("b) Kilograms to Pounds")
            
            sub_choice = input("Choose option (a/b): ").lower()
            
            try:
                if sub_choice == 'a':
                    pounds = get_valid_number("Enter pounds: ", allow_negative=False)
                    kg = pounds_to_kilograms(pounds)
                    print(f"{pounds} lbs = {kg} kg")
                    
                elif sub_choice == 'b':
                    kg = get_valid_number("Enter kilograms: ", allow_negative=False)
                    pounds = kilograms_to_pounds(kg)
                    print(f"{kg} kg = {pounds} lbs")
                    
                else:
                    print("Invalid option. Please enter 'a' or 'b'.")
                    continue
                    
                conversion_count += 1
                
            except Exception as e:
                print(f"Error during weight conversion: {e}")
        
        # ==================== DEMONSTRATE SCOPE ====================
        elif choice == 4:
            demonstrate_scope()
            
            # Show local variable in main()
            print(f"\nOutside function - Local variable (conversion_count): {conversion_count}")
            print(f"Outside function - Global variable (app_name): {app_name}")
        
        # ==================== EXIT ====================
        elif choice == 5:
            print(f"\nYou performed {conversion_count} conversions today.")
            print("Thank you for using Unit Converter Pro. Goodbye!")
            break
        
        # ==================== INVALID CHOICE ====================
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# ===================== PROGRAM ENTRY POINT =====================
if __name__ == "__main__":
    # This demonstrates another try-except block for different error type
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting gracefully...")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        print("Please report this issue.")
        
        