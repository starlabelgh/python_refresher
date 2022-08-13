#from unittest import mock


#name = input("enter your name:")
#print(name)

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = size_input / 10.8
print(square_meters)

print(f"{square_feet} square feet is {square_meters:.2f} square metres.")
