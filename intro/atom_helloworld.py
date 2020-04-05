
import os

print(os.name)

#
# print(os.environ)

print("hello world on Atom")

# testing()
#
# def testing():
#     print("inside function")

# first_name = "Dharmesh"
# last_name = "Gangani"

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
print("hello world on Atom--2")
print("Hello - " + first_name.capitalize() + " " + last_name.capitalize())
print("Formatted Hello - {} {}" .format(first_name, last_name))


def this_function():
    print("this_function")


output = f"Py3 Formatted Hello - {first_name} {last_name}"
print(output)
print(f"Py3 Formatted Hello 2 - {first_name} {last_name}")

for num in [1, 2, 3, 4]:
    print(num)
