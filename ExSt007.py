# 7.Conjunto de valores (While)
# Dev: Karina Zimerer
# Data: 30.08.2022
"""
Faça um programa que leia um conjunto não determinado de valores
e mostre o valor lido, seu quadrado, seu cubo e sua raiz
quadrada. Finalize a entrada de dados com um valor negativo ou zero.
obs. REFAZER ESSE EXERCICIO
"""
cubo, quadrado, RaizQuadrada = float
numero = int

while True:
    numero = numero >= 0
    print('Digite um numero que seja feito o seu quadrado, o cubo e a raiz quadrada')
    print("O quadrado do número é " + quadrado)
    quadrado = numero * numero
    print("O cubo do número é " + cubo)
    cubo = numero * numero * numero

    print("A raiz quadrada do número é " + RaizQuadrada)
    RaizQuadrada = RaizQuadrada * numero

    print("Digite 0 ou negativo para finalizar")
