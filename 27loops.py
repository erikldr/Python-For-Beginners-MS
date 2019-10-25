# name vai iterar com a lista e assumir os seus valores
for name in ['Erik', 'Vivian', 'Luiza']:
    print(name)
print()

# index vai assumir os valores do intervalo estipulado
for index in range (0, 2):
    print(index)
print()

# Looping with a condition
names = ['Erik', 'Vivian', 'Luiza']
index = 0

# Neste exemplo index assume os valores de 0 ate o tamanho da lista
while index < len(names):
    print(names[index])
    # Change the condition!!
    index = index + 1