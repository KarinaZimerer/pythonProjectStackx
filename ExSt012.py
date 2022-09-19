#12. tres 3 valores em ordem (IF)
"""
Escreva um programa para ler 3 valores inteiros
(considere que não serão lidos valores iguais)
e escrevê-los em ordem crescente
"""

n1 = int(input("Digite um valor inteiro "))
n2 = int(input("Digite um valor inteiro "))
n3 = int(input("Digite um valor inteiro "))

if (n1 > n2) and (n1 > n3):
    if n2 > n3:
        print(n3)
        print(n2)
        print(n1)
    else:
        print(n2)
        print(n3)
        print(n1)
elif (n2 > n1) and (n2 > n3):
    if n1 > n3:
        print(n3)
        print(n1)
        print(n2)
    else:
        print(n1)
        print(n3)
        print(n2)
elif (n3 > n1) and (n3 > n2):
    if n1 > n2:
        print(n2)
        print(n1)
        print(n3)
    else:
        print(n1)
        print(n2)
        print(n3)
