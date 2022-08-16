from ast import arg
from traceback import print_tb


def named(**kwargs):
    print(kwargs)
    
named(name="Moses", age="28")



def named(name, age):
    print(name, age)
    
details = {"name": "Moses", "age": 28}

named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")
        
print_nicely(name="Moses", age=28)


def both(*args, **kwargs):
    print(arg)
    print(kwargs)
    
both(1, 3, 5, name="Moses", age=28)