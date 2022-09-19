
"""
Faça um programa para calcular a tabuada de qualquer número digitado pelo usuário.
2. Estruturas condicionais e de repetição Tabuada com entrada do usuário (FOR)
"""

mult = int(input("Digite um número "))
tab = int(input("Qual a Tabuada você prefere? "))

mult = mult * 1

for laco in range(10):
    print(tab, "X", mult, "=", tab * mult)
    mult = + 1
