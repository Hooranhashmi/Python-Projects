MIN_SALARY = 30000.0 # The minimum annual salary
MIN_YEARS = 2 # The minimum years on the job
# Get the customer's annual salary.
salary = float(input('Enter your annual salary: '))

 # Get the number of years on the current job.
years_on_job = int(input('Enter the number of ' +
 'years employed: '))

 # Determine whether the customer qualifies.
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
 print('You qualify for the loan.')
else:
 print('You do not qualify for this loan.')






 def change_counting_game():
    print("Welcome to the Change Counting Game!")
    print("Enter the number of coins needed to make exactly one dollar.")
    
    # Get user input
    pennies = int(input("Enter the number of pennies: "))
    nickels = int(input("Enter the number of nickels: "))
    dimes = int(input("Enter the number of dimes: "))
    quarters = int(input("Enter the number of quarters: "))
    
    # Calculate total value in cents
    total_value = (pennies * 1) + (nickels * 5) + (dimes * 10) + (quarters * 25)
    
    # Check if total is equal to one dollar (100 cents)
    if total_value == 100:
        print("Congratulations! You've made exactly one dollar. You win!")
    elif total_value < 100:
        print("The total amount is less than one dollar. Try again!")
    else:
        print("The total amount is more than one dollar. Try again!")

# Run the game
change_counting_game()



def calculate_bmi():
    print("Welcome to the BMI Calculator!")
    
    # Get user input for weight and height
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    
    # Calculate BMI using the given formula
    bmi = (weight * 703) / (height ** 2)
    
    # Display the BMI
    print(f"Your BMI is: {bmi:.2f}")
    
    # Determine weight category
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi <= 25:
        print("You have an optimal weight.")
    else:
        print("You are overweight.")

# Run the BMI calculator
calculate_bmi()



