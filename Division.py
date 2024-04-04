#DIVISION
num1 = float(input("Enter the dividend for division: "))
num2 = float(input("Enter the divisor for the division: "))
if num2 == 0:
    print("Error: Division by zero is not allowed")
else:
    div_result= num1/num2
    print("Division:", div_result)