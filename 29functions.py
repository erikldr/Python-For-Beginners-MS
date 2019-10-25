# Import the datetime class from datetime library
from datetime import datetime
#print timestamps to see how long sections of code
#take to run

# Print the current time and task name
def print_time(task_name): # Define a function called print_time
    print(task_name)
    #print(datetime.datetime.now())
    print(datetime.now()) # Now I don't need the extra datetime prefix
    print()

first_name = 'Erik'
print_time('first name assigned') # passa uma string como parametro

for x in range(0,5):
    print(x)

print_time('loop completed') # passa uma string como parametro

#*****************************************************************

first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial,last_name_initial)