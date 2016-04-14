def is_palindrome(number):
    number = str(number)
    for i in range(len(number)//2):
        if number[i] != number[-i-1]:
            return False
    return True
largest_number = 0
for i in range(1,999):
    for j in range(1,999):
        number = i * j
        if is_palindrome(number) and number >= largest_number:
            largest_number = number
print (largest_number)
