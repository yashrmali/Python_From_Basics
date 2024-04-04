#Write a Python program to swap two variables


#Input from the user
a = float(input("Enter the first variable: "))
b = float(input("Enter the second variable: "))
#Print the original variables values
print(f"Original Values: a = {a}, b = {b}")
#Swap using temp varaible
temp = a
a = b
b = temp
#Print the swapped values
print(f"Swapped Values: a = {a}, b = {b}")
