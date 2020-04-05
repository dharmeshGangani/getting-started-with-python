from datetime import datetime


# Function to print current date and time for logging
def print_time(task_name):
    print('Task Completed: ' + task_name)
    print(datetime.now())
    print()


# Function to get initial for a given name
def get_initial(name, force_uppercase=True):
    initial = name[0:1]
    if force_uppercase:
        initial = initial.upper()
    return initial


first_name = input('Enter first name: ')
print('fName initial: '+get_initial(first_name))
print_time('fName')

last_name = input('Enter last name: ')
print('LName initial: '+get_initial(force_uppercase=False, name=last_name))  # named params
print_time('lName')
