# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calculate the sum
sum = add_numbers(number1, number2)

# Display the result
print(f"The sum of {number1} and {number2} is {sum}")
