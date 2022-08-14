#create a list, called my_list with three numbers. The total of the numbers added together shoud be 100
my_list = [1, 2, 97]

#create a tuple, called my_tuple with a single value in it
my_tuple = int(5,)


#modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5}

set2.add(77)
set2.add(9)
set2.add(12)

intersection = set1.intersection(set2)
print(intersection)