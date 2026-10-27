"""
the map() function is used to apply a given function to every item in a collection
(collections: list, tuple, set, dictionary)
"""



celsius_temps = [0,10,20,30,40]

# convert these all to a list of fehrenheit
# (c * 9/5) + 32

def c_to_f(temp):
    return (temp * 9/5) + 32

fehrenheit_temps = map(c_to_f, celsius_temps)
print(fehrenheit_temps) # map object
# convert map objects to a list
print(list(fehrenheit_temps))

# do the same thing but with a lambda
fehrenheit_temps2 = map(lambda temp: (temp * 9/5) + 32, celsius_temps)
print(fehrenheit_temps2)
# convert to list
print(list(fehrenheit_temps2))

"""
why would we use map?
- save time, no need for long for loops
- cleaner code
- works great with lambda
- efficient
"""

names = [
    {"fname": "frank", "lname": "williams", "age": 52},
    {"fname": "david", "lname": "smith", "age": 15},
    {"fname": "jace", "lname": "larkin", "age": 16},
    {"fname": "k", "lname": "luh", "age": 103},
    {"fname": "duane", "lname": "olesnanik", "age": 31}
]

# without list comprehension: Map these names to be lastnameFirstInitial, zero padded age (52: 052)
# if age were 7, 007

names = map(lambda names: f"{names["lname"]}{names["fname"][0]}{str(names["age"]).rjust(3, "0")}",names)
print(names)

for name in names:
    print(name)