number = 0
not_found = True
while not_found:
    number += 2
    for i in range(10,21):
        if number % i != 0:
            break
        if i == 20:
            not_found = False
print(number)
