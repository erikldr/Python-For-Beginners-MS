import json
# Create a dictionary objetc
person_dict = {'first': 'Christopher', 'last': 'Harrison'}
# Add additional key pairs as needed to dictionary
person_dict['City'] = 'Seattle'

# Convert dictionary to JSON object
# person_json = json.dumps(person_dict)
#print(person_dict)

# *********************************************************
#person_dict = {'first': 'Christopher', 'last': 'Harrison'}
# Create staff dictionary wich assigns a person to a role
staff_dict = {}
staff_dict['Program Manager'] = person_dict

# Convert dictionary to JSON object
staff_json = json.dumps(staff_dict)

# Print JSON object
print(staff_json)

# Create a list object of programming languages
languages_list = ['CSharp', 'Python', 'JavaScript']
# Add list to dictionary
person_dict['languages'] = languages_list

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)

# When creating and reading JSON
# Use print statemments to help you debug
# Use a JSON linting tool to make the JSON easier to read
# Have a print out of the full JSON so you can figure out the structure when reading specific elements
