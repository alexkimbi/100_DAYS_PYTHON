print("Welcome to the tip calculator")
bill = float(input("What was your your total bill?  $ " ""))
tip_percentage = int(input("What percentage of your bill do you want to pay as tip? 10, 12, or 15? " ""))
number_of_people = int(input("How many people do you want to split the bill? " ""))
tip_to_be_paid = tip_percentage * tip_percentage
bill_per_person = tip_to_be_paid / number_of_people
total_bill = tip_percentage / 100 * bill + bill
final_bill = round(bill_per_person, 2)
print(f"The total bill to be paid including tips is : {total_bill}")
print(f"The total bill per person {final_bill}")
