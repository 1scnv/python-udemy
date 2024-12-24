primeiro_valor = input ('digite um valor: ')
segundo_valor = input ('digite outro valor: ')

if segundo_valor > primeiro_valor:
    print(f'O segundo valor({segundo_valor}) é maior que o primeiro valor ({primeiro_valor})')
elif segundo_valor == primeiro_valor:
    print(f'o segundo valor e o primeiro valor são iguais')
elif primeiro_valor > segundo_valor:
    print(f'O primeiro valor({primeiro_valor}) é maior que o segundo valor ({segundo_valor})')
else:
    print('Fora do bloco')