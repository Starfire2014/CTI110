# CTI-110
# P2HW2 - Lists and Sets
# Briana Jackson
# 06/19/2022
#

num1 = float(input('Enter num 1:'))
num2 = float(input('Enter num 2:'))
num3 = float(input('Enter num 3:'))
num4 = float(input('Enter num 4:'))
num5 = float(input('Enter num 5:'))
num6 = float(input('Enter num 6:'))
chosen_numbers = [num1, num2, num3, num4, num5, num6]
avg_list = sum(chosen_numbers) / len(chosen_numbers)

print('Created List:')
print(chosen_numbers)

print('Smallest number in list:', min(chosen_numbers))
print('Largest number in list:', max(chosen_numbers))
print('Sum of numbers in list', sum(chosen_numbers))
print('Average of numbers in list:', avg_list)

chosen_numbers_set = set([num1, num2, num3, num4, num5, num6])
print('Created set:', chosen_numbers_set)
