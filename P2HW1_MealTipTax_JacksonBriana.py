# Tip Calculator Project
# 06/19/2022
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Briana Jackson
#
food_charge = float(input('Enter Charge For Food:'))
tip_percent = float(input('Enter tip percent:'))
tax_percent = float(input('Enter Tax percent:'))
total_tip = food_charge * tip_percent
added_tax = food_charge * tax_percent
print('Calculated Tip:', total_tip)
print('Calculated Tax:', added_tax)
print('Total cost including tip and tax:', food_charge + total_tip +added_tax)
