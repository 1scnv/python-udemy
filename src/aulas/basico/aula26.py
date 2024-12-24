"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #preencher a esquerda
print(f'{variavel: <10}') #preencher a direita
print(f'{variavel: ^10}') #preencher no centro
print(f'{-1000.498172984714:+,.1f}') #preencher sinal do número e formatar para 1 casa decimal
print(f'O hexadecimal de 1500 é {1500:08x}') #Número decimal de um número
print(f'{variavel!r}')