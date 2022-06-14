# Basic programming practice
# 06/14/2022
# CTI-110 - Basic Math
# Briana Jackson
#


expense_name= input('Enter name of expense:')
monthly_cost= float(input('Enter monthly charge:'))
tax= monthly_cost * 0.06
monthly_charge= monthly_cost+tax

print('Bill:', expense_name, end=' ')
print('--------- Before Tax:', monthly_cost)
print('Monthly Tax:', tax)
print('Monthly charge', monthly_charge)
print('Annual Charge:', monthly_charge*12)
