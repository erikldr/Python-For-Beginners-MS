# This function will return the first initial of a name
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper() # Pega a primeira inicial e a converte para grande
    else:
        initial = name[0:1]    
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(force_uppercase=True, \
                                 name = first_name)
last_name = input('Enter your first name: ')
last_name_initial = get_initial(force_uppercase=True, \
                                 name = last_name)

print('Your initials are: ' + first_name_initial, last_name_initial)
#**************************************************************************************

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)

    # Imagine code here that logs our errors to a database or file

first_number = 10
second_number = 5

if first_number > second_number:
    error_logger(error_code = 45,
                 error_severity = 1,
                 log_to_db = True,
                 error_message = 'Second number greater than first',
                 source_module = 'my_math_method')