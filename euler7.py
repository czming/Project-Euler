def is_prime(number):
    for i in range(2, int(number ** (1/2))+1):
        if number % i == 0:
            return False
    return True
number = 0
current_number = 2
while number < 10001:
    if is_prime(current_number):
        number += 1
    current_number += 1
print (current_number-1)
