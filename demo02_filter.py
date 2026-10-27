"""
Filter: similar to map, only the function returns true or false
"""

names = ["isaac", "david", "jace", "zach", "evan"]


def is_not_zach(name):
    return name.lower().strip() != "zach"


print(names)
cleaned_list = filter(is_not_zach, names) # this will return a filter object
print(list(cleaned_list))

even_better = list(
    filter(lambda name: name.lower().strip() != "jace", cleaned_list))
print(even_better)


grades = [
    {"student": "Evan", "score": 12},
    {"student": "Isaac", "score": 83},
    {"student": "Kaine", "score": 90},
    {"student": "Blake", "score": 79},
    {"student": "Micheal", "score": 89},
    {"student": "Zach", "score": 4}
]

# Filter this list down to only passing students:
grades = list(filter(lambda grades: grades["score"] >= 60, grades))
print(grades)