"""
Some examples of code that is considered "Pythonic"
"""

print("Example 1: Loops")
fruits = ["apple", "peach", "fig", "pawpaw"]

# Do this
for fruit in fruits:
    print(fruit)

# Not this
for i in range(len(fruits)):
    print(fruits[i])


print("Example 2: Checking if an element is in a list")
veggies = ["squash", "corn", "peas"]

# Do this
has_corn = "corn" in veggies
print(has_corn)

# Not this
has_corn = False
for veggie in veggies:
    if veggie == "corn":
        has_corn = True
print(has_corn)


print("Example 3: Checking if all items in a list exist")
attendance_count = [25, 60, 0, 18, 54, 2]

# Do this
attendees = all(attendance_count)
print(attendees)

# Not this
attendees = True
for count in attendance_count:
    if count == 0:
        attendees = False
print(attendees)


print("Example 4: Comparisons")
calculation_complete = False

# Do this
if not calculation_complete:
    print('Calculation is not complete')

# Not this
if calculation_complete == False:
    print('Calculation is not complete')


print("Example 5: List comprehensions")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Do this
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Not this
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(even_numbers)


print("Example 6: Reading from a file")
file_name = "README.md"

# Do this
with open(file_name) as readme:
    print(readme.name)

# Not this
readme = open(file_name)
print(readme.name)
readme.close()


print("Example 7: String formatting")
favorite_fruit = "nectarine"

# Do this
print(f'My favorite fruit is the {favorite_fruit}')

# Not this
print('My favorite fruit is the {}'.format(favorite_fruit))
