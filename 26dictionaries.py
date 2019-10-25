# A diferença entre dicionarios e listas é que:
# No dicionario é possível nomear os itens
erik = {'first': 'Erik', 'last': 'Rocha'} 
vivian = {'first': 'Vivian', 'last': 'Silva'}

people = [erik, vivian]
people.append({'first': 'Maria', 'last': 'Luiza'})
presenters = people[1:3]

# print(people)
# print()
# print(presenters)

print(len(people))
print()


