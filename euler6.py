sum_square = 0
for i in range(101):
    sum_square += i ** 2
integer_sum = 0
for i in range(101):
    integer_sum += i
difference = integer_sum ** 2 - sum_square
print(difference)
