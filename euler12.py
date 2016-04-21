number = 0
current_term = 1
divisors = 0
while divisors < 250: #below the square root of the number, if there are 250 factors, there will be 500 factors in total since the number of factors below the square root is equal to the number of factors above it (if the number's square root is a factor of it, it leads to an odd number, so still need 250
    number += current_term
    current_term += 1
    divisors = 0
    for i in range(1, int(number ** (1/2)) + 1):
        if number % i == 0:
            divisors += 1
    print (number)
print (number)
