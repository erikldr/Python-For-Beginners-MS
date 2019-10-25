# This function will return the first initial of a name
def get_initial(name):
    initial = name[0:1].upper() # Pega a primeira inicial e a converte para grande
    return initial

first_name = input('Enter your first name: ')
last_name = input('Enter your first name: ')

print('Your initials are: ' \
     + get_initial(first_name) \
     + get_initial(last_name))
