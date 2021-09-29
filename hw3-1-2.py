# Author: CRS 9/28/21
first_card = int(input("Please enter your first card's value."))
second_card = int(input("Please enter your second card's value."))
total_value = first_card + second_card
if total_value <= 21:
    print("You are safe.")
else:
    print("You busted.")
