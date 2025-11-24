#welcome message
print("Welcome to my Python program!")
# inputs number of hours into formula
hours = input("How many hours did you study today? ")
# converts into float
hours = float(hours)
weekly_hours = hours * 7
#prevents errors from invalid input
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()