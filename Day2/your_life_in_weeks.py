import time
age = input("What is your current age? "  "")
years_remaining = 90 
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
results = (f"Your total age in weeks is:{age} your remaining age is {years_remaining} and the total number of days is {days_remaining}" )
time.sleep(5.5)    # Pause 5.5 seconds
print(results)
