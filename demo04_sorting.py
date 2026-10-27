names = ["Evan", "Jace", "Zach", "Mykyta", "Allyn"]
# we can sort the list with the .sort method.
#note: changes the actual order of your list
print(names)
names.sort()  # defaults to alphabetical (all capitals first)
print(names)

# sort in reverse order:
names.sort(reverse=True)
print(names)

other_names = ("blake", "michael", "abigale", "josie",
               "ryan", "josh", "duane", "john")

# other_names.sort()
# print(other_names)
# but we can sort a tuple if we use sorted:
sorted_other_names = sorted(other_names)
# sorted returns a new list, instead of sorting in place
print(sorted_other_names)
print(dict(enumerate(sorted_other_names)))
print(dict(zip(["A", "B", "C", "D", "E", "F", "G", "H"], other_names)))

# sort by length of string:
len_of_names_sorted = sorted(other_names, key=len)
print(len_of_names_sorted)

from functools import reduce

most_vowels = sorted(len(lambda s: len(list(filter(lambda c: c.lower() in 'aeiou', s)))), reverse=True)
print(most_vowels)

def get_last_letter(word):
    return word[-1]

sorted_by_last_letter = sorted(other_names, key=get_last_letter)
print(sorted_by_last_letter)