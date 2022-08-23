from operator import itemgetter

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Moses", "age": 28},
    {"name": "Akua", "age": 21},
    {"name": "Efya", "age": 23}
]

def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Moses", get_friend_name))

#alternative lambda function

print(search(friends, "Efya", lambda friend: friend["name"]))

#using itemgetter function
print(search(friends, "Moses", itemgetter("name")))