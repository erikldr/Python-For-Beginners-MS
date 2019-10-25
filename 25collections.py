names = ['Christopher', 'Susan']
names.append('Erik') # Inserir no fim
names.insert(0, 'Vivian') # Inserir na posição
names.insert(2, 'Luiza') # Inserir na posição
print(names)
print(len(names)) # Get the number of items
print()

names.sort() # Embaralha a lista de nomes
print(names)
presenters = names[0:2] # Get the first two items
#starting index and numbers of items to retrieve
print(presenters)
print()

from array import array
scores = array('d')
scores.append(98) # Add new item to the end
scores.append(99)
print(scores)
print(scores[0]) # Collections are zero-indexed
print(type(scores[0]))
print(type(scores))

# A diferença entre Lista e Array é o que cada um armazena
# A lista armazena qualquer tipo de item
# Já o Array somente itens de mestmo tipo


