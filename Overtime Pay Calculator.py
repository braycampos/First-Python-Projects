#Write a program to prompt the user for hours and rate per hour using input 
#to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate 
#for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program 
#(the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.


# Define variables:
hrs = input("Enter Hours: ")
rate = input("Enter rate per hour: ")

# Define the data type entered into the program:
h = float(hrs)
r = float(rate)

# First case:
if h <= 40:
   pay = (h * r)  # Define the payment.
   
# What will be executed if the first case is not met:
else:
    regular_pay = (40 * r)  # Define the payment
    overtime_hours = h - 40  # Define the overtime hours
    overtime_pay = overtime_hours * (r * 1.5)  # Define the overtime calculation
    pay = regular_pay + overtime_pay  # Define the payment with overtime

print(f"{pay:.2f}")  # What we will present (as a function, with .2 decimals)
Let me know if you need any further assistance!










