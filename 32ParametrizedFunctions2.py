def get_initial(name, force_uppercase=True): # Por default ira converter para upper caso nao receba nada como parametro
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(force_uppercase=False, name=first_name) # Passa o nome e um booleano para o upper

print('Your initials are: ' +first_name_initial)
