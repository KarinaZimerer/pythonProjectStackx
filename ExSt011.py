# 11. Compra de maçâs (IF)
"""As maçãs custam R$ 0,30 cada se compradas
menos do que uma dúzia, e R$ 0,25 se forem compradas
pelo menos doze. Escreva um programa que leia o número de maçãs compradas,
calcule e escreva o valor total da compra"""

valorUnitario = 0.30
TotalCompra = float

QtdMacas = int(input("Digite o número de maçãs que irá comprar?: "))

if QtdMacas >= 12:
    TotalCompra = QtdMacas * valorUnitario
    print("O valor total da compra é: ", TotalCompra)
else:
    TotalCompra = QtdMacas * 0.25
    print("O valor total de compra e: ", TotalCompra)
