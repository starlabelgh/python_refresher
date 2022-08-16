from email.policy import default


def add(x, y=12):
    print(x + y)
    
add(32)

default_y = 12

def add(x,y=default_y):
    sum = x+y
    print(sum)
    
add(5)

