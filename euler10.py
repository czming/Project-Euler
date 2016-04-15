def is_prime(number):
    for k in range(2, int(number ** (1/2))+1):
        if number % k == 0:
            return False
    return True
number_sum = 0
for i in range(2, 2000000):
    if is_prime(i):
        number_sum += i
print (number_sum)
