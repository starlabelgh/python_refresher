from unittest import result


#function with parameter
def add(x, y):
    result = x + y
    print(result)

add(5, 7)

#function without parameter
def say_hello(name, surname):
    print(f"hello!, {name} {surname}")
    
say_hello(surname="Moses", name="starlabel")

#divide function
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("you fool!")
        
divide(dividend=15, divisor=0)
