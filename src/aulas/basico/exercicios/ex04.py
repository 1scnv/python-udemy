"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
# numero = input('digite um número inteiro:')

# if numero.isdigit():
#     numero = int(numero)
#     if numero % 2 == 0:
#         print('Número par')
#     else:
#         print('Número ímpar')


horario = input('Digite um horário (0-23)')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horário inválido')
    else:
        if horario <= 11:
            print(f'Bom dia. Agora são {horario} horas da Manhã')
        elif horario <= 17:
            print(f'Boa Tarde. Agora são {horario} horas da Tarde')
        else:
            print(f'Boa Noite. Agora são {horario} horas da Noite')