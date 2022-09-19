# 8.Número maior (IF)
# Dev: Karina Zimerer
# Data: 30.08.2022
"""
Escreva um programa para ler 2 valores
não serão informados valores iguais
escrever o maior deles
"""
n1 = int(input("Digite o primeiro valor"))
n2 = int(input("Digite o segundo valor"))

if n1 > n2 and n2 < n1:
    print("valor do número 1 é maior: ", n1)
if n1 == n2:
    print("Cogigo de Erro, Os valores são Iguais")
