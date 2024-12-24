# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
# senha = input('Senha: ')
#print(not True)  # False
#print(not False)  # True

senha = input ('Senha:')
senha_correta = '123456'

if not senha:
    print('Você não digitou nada')
elif senha != senha_correta:
    print('Senha incorreta')
else:
    print('Bem-vindo ao sistema.')