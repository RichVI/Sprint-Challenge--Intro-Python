# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")

# Loop over humans list, if first letter is D, then add it to a
a = [human.name for human in humans if human.name[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")

# Loop over humans list, if last letter(index[-1]) is e, then add it to b
b = [human.name for human in humans if human.name[-1] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")

# create a new list with alphabet from C to G
l = ['C', 'D', 'E', 'F', 'G']

# Loop over humans, if first letter match with(in) the new list, then add it to c
c = [human.name for human in humans if human.name[0] in l]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")

# Loop over humans, add 10 to human.age
d = [human.age + 10 for human in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")

# Loop over humans, concatenate name with cast age to string  with "-" in between 
e = [human.name + "-" + str(human.age) for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")

# Loop over humans, if age is between 27 to 32, turn it into a list of tuple
# and add it to f
f = [(human.name, human.age) for human in humans if human.age >= 27 and human.age <= 32]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")

# Loop over humans, and contruct a new instance called g with names uppercase and
# age + 5
g = [(Human(human.name.upper(), human.age + 5)) for human in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math

# Loop over humans, use math sqrt() method to square root the age and added to h
h = [math.sqrt(human.age) for human in humans]
print(h)
