numbers = [1, 2, 3]

new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Johnny"

new_list = [letter for letter in name]
print(new_list)

double_numbers = [number * 2 for number in range(1, 5)]
print(double_numbers)

surname = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in surname if len(name) < 5]
print(short_names)
