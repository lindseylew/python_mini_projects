print("Welcome to the tip calculator!\n")

total_bill = input("What was the total bill? $")

tip_amount = input("How much tip would you like to give? 10, 12, or 15? ")

number_of_people = input("How many people to split the bill? ")

new_total_bill = float(total_bill)
new_tip_amount = int(tip_amount)
new_number_of_people = int(number_of_people)

multiply_percent = (new_total_bill * (new_tip_amount/100))

per_person_amount = round(float((new_total_bill + multiply_percent)/new_number_of_people), 2)

print(f"Each person should pay: ${per_person_amount}")