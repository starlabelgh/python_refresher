name = "Bob"
greeting = "Hello, {}"

with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)


longer_phrase = "Hello {}, today is {}."
formatted = longer_phrase.format("Moses", "Saturday")
print(formatted)