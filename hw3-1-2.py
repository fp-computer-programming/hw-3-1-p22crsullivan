# Author: CRS 9/28/21
first_card = input("Please enter your first card's value.")
second_card = input("Please enter your second card's value.")
jack = 10
queen = 10
king = 10
total_value = first_card + second_card
if total_value <= 21:
    print("You are safe.")
else:
    print("You busted.")
