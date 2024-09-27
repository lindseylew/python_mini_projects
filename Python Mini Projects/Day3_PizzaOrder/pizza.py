# Based on a user's order, work out their final bill.
# Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): +$2
# Add pepperoni for medium or large pizza (Y or N): +$3
# Add extra cheese for any size pizza (Y or N): +$1


print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")

bill = 0

#add_pepperoni = input() # Do you want pepperoni? Y or N
#extra_cheese = input() # Do you want extra cheese? Y or N

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
   bill += 25

    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni == "Y" and size == "S":
        bill += 2
    elif add_pepperoni == "Y":
        bill += 3

    extra_cheese = input("Do you want extra cheese? Y or N ")
    if extra_cheese == "Y":
        bill += 1

    print(f"Your total bill is ${bill}.")

else:
    print("Please try again!")

