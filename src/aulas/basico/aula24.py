# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5 6 7
#  V i n í c i u s
# -8-7-6-5-4-3-2-1

nome = input ('Digite o seu nome: ')
encontrar = input ('Digite o texto que deseja encontrar:')
# print(nome[1])
# print(nome[-7])

# print('us' in nome) #true
# print('us' not in nome) #false

if encontrar in nome:
    print(f'{encontrar} está no nome: {nome}')
else:
    print(f'{encontrar} não está no nome: {nome}')