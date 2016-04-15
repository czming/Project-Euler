found = False
for a in range(1,1000):
    for b in range(1,1000):
        c_square = a ** 2 + b ** 2
        c = c_square ** (1/2)
        if a + b + c == 1000:
            print (int(a * b * c))
            found = True
            break
    if found:
        break
