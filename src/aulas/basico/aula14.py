##formatacao de string

a = 'A'
b = 'B'
c = 1.111

string = 'a={nome1} b={nome2} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)
print(formato)