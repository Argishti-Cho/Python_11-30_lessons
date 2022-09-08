
def roundTheNumber(n):
    # n = int(n-0.5)+1
    # n = int((10*n-0.5)+1) / 10.0
    # n = int((100*n-0.5)+1) / 100.0
    n = int((1000*n-0.5)+1) / 1000.0
    return n

print(roundTheNumber(float(input('Enter any floating number:  '))))


