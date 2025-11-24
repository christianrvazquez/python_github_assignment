#welcome message
print("Welcome to my Python program!")
#collect input
hours = input("How many hours did you study today? ")
#convert hours to float and give weekly study pace
hours = float(hours)
weekly_hours = hours * 7
#clean output
print(f"You are on track to study {weekly_hours} hours this week.")
#prevent error from invalid input
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
