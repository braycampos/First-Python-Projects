'''Program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error.
If the score is between 0.0 and 1.0,
print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a
suitable error message and exit.'''

# Define the variable for the obtained score
score = input("Enter Score: ")
# Define the data type:
sc = float(score)
# The first condition to filter out incorrect inputs:
if sc < 0.0 or sc > 1.0:
        print("Error")
# If the first condition is not met; we start with our grading criteria:
else:
   if sc >= 0.9:
      grade = 'A'
   elif sc >= 0.8:  # We use elif to ensure that only one condition is applied, not all.
      grade = 'B'
   elif sc >= 0.7:
      grade = 'C'
   elif sc >= 0.6:
      grade = 'D'
   else:
      grade = 'F'
   print(f"{grade}")  # We instruct the program to display the desired output.