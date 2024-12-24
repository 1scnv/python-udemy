nome = input ('Digite o seu nome: ')
idade = input ('Digite a sua idade: ')

if not (nome and idade):
    print('Você não digitou nada')
else:
    print(f'Seu nome é:{nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if '' in nome:
        print('Seu nome contém espaços')
    else: 
        print('Seu nome não contem espaços')
    print(f'{nome}, seu nome tem {len(nome)} caracteres')
    print(f'A primeira letra do seu nome é: {nome[0:1]}')
    print(f'A última letra do seu nome é: {nome[-1::]}')
