def hello():
    print("hello!")
    
hello()


def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

print("Welcome to the age in seconds program!")
user_age_in_seconds()

print("Goodbye!")


friends = ["Rolf", "Moses"]

def add_friend():
    friend_name = input("Enter your friend name:")
    friends = friends + [friend_name]
    
add_friend()


def add_friend():
    friends.append("Rolf")
    
friends = []
add_friend()

print(friends) #Rolf