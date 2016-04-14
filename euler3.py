parameter = 600851475143
largest_prime_factor = 0
def is_prime(number):
    for k in range(2, int(number ** (1/2))):
        if number % k == 0:
            return False
    return True
for i in range(1, int(parameter ** (1/2))):
    if parameter % i == 0:
        print (i)
        if is_prime(i):
            largest_prime_factor = i
print (largest_prime_factor)
