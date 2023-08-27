#!/usr/bin/python3
#This will print tickets for a roller custer rides and charge the price based on age. 
age = int(input("What is your age?"))
print("======Tickets are sold and prices are determined based on buyer's age=====")
if age >= 18 and age < 41:
    print("You are above 18 years so you are considered as an adult and will pay reg amount")
elif age < 18 and age >=6:
        print("You are between 6 and 18 yrs old and will have a discount of 10 dollars")
elif age >= 40:
    print("You are considered a senior hence  your tickets are already paid for. ")
else:
    print("You are not allowed to ride")
