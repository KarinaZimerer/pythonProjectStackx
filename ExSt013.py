# 16. Três valores e o maior deles (IF)
"""
Escreva um programa para ler 3 valores inteiros e escrever o maior deles.
Considere que o usuário não informará valores iguais.
"""
n1 = int(input("Digite um valor inteiro "))
n2 = int(input("Digite um valor inteiro "))
n3 = int(input("Digite um valor inteiro "))

if (n1 > n2) and (n1 > n3):
    print(" O número 1  é o maior", n1)
else:
    var = (n2 > n1) and (n1 < n2)
    print("O numero 2 é maior", n2)
if (n1 == n2) and (n2 == n1):
    print("Erro, valores Iguais")
