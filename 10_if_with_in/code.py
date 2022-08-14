movies_watched = {"The Matrix", "Green Book", "Her"}
user_movies = input("Enter a movie you've watched recently:")


if user_movies i movies_watched:
    print(f"I've watched {user_movies} too!")
else:
    print("I haven't watched that yet")



number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:
        print("you're ff by one.")
    else:
        print("Sorry, it's not correct!")