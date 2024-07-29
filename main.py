# Calculate the factorial of a number.

def factorial(n):
    # Initialize the factorial variable to 1.
    factorial = 1
    
    # Loop from 1 to n (inclusive) to calculate the factorial.
    for i in range(1, n+1):
        # Multiply the current value of factorial by the loop counter i.
        factorial = factorial * i
    
    # Return the calculated factorial value.
    return factorial

# Prompt the user to enter a non-negative integer.
number = int(input("Enter a non-negative integer for factorial calculation: "))

# Check if the entered number is negative.
if number < 0:
    # If the number is negative, print an error message.
    print("Please enter a non-negative integer.")
else:
    # If the number is non-negative, calculate and print the factorial.
    print(f"The factorial of {number} is: {factorial(number)}")
