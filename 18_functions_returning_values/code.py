from unittest import result


def add(x, y):
    print(x + y)
    
add(6, 9)

result = add(6, 9)

print(result)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "you fool"
    
    
result = divide(21,3) * 5
print(result)

