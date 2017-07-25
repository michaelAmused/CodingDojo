def multiply(numbers,mult):
    b = []
    for i in range(len(numbers)):
        b.append(numbers[i] * mult)
    return b

a = [2,4,10,16]
total = multiply(a,5)
print total
