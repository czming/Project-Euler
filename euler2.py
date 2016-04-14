parameters = 4000000
number1 = 1
number2 = 2
total_number = 0
new_number = 2
while number2 <= parameters:
    if new_number % 2 == 0:
        total_number += new_number
    new_number = number1 + number2
    number1 = number2
    number2 = new_number
print (total_number)
