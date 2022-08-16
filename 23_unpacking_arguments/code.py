from ast import arg


def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    
    return total
    
print(multiply(1, 3, 5))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
    
print(apply(1, 3, 6, 7, operator="+"))


def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

nums = {"x": 15, "y": 25}
print(add(x=nums["x"], y=nums["y"]))