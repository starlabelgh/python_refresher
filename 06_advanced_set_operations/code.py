from threading import local


friends = {"Anne", "Moses", "Dada"}
abroad = {"Moses", "Anne"}

local_friends = friends.difference(abroad)

total_friends = friends.union(abroad)
print(total_friends)
print(local_friends)


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

study_art_only = art.difference(science)
study_science_only = science.difference(art)

total_students = art.union(science)
study_both_subject = art.intersection(science)

print(study_art_only, "study only art")
print(study_both_subject, "study both subject")
print(study_science_only, "study only science")
print(total_students, "are the total number of students")