from tokenize import Double


numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]

# for num in numbers:
#     doubled.append(num * 2)


friends = ["Rolf", "Sam", "Samantha", "Moses", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
#starts_s = friends
# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)
        
print(starts_s)
print(friends)
print(friends is starts_s)
print("friends: ", id(friends), "starts_s:", id(starts_s))
