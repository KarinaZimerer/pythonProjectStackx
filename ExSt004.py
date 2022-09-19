# Salário Bruto (IF)
# Dev: Karina Zimerer
# Data: 24.08.2022

"""
Faça um programa que receba o salário bruto de um funcionário e, usando a tabela a seguir, calcule e mostre o valor a receber. Sabe-se que este é composto pelo salário bruto acrescido de gratificação e descontado o imposto de 7% sobre o salário.

SALÁRIO 			    GRATIFICAÇÃO
Até R$350,00 			    R$100,00
R$351,00 até R$600,00 		R$75.00
R$601,00 até R$900,00 		R$50,00
Acima de R$901,00 		    R$35,00

Imposto 7%: 0.07%

"""

salarioBruto = float(input("Digite o valor do salário bruto: "))
salarioLiquido = float

Imposto = 0.07

if salarioBruto < 350:
    salarioLiquido = salarioBruto - (salarioBruto * Imposto) + 100, 00
    print("O salario liquido é: ", salarioLiquido)

elif salarioBruto > 351 and salarioBruto <= 600:
    salarioLiquido = salarioBruto - (salarioBruto * Imposto) + 75,00
    print("O salario liquido é: ", salarioLiquido)

elif salarioBruto > 600 and salarioBruto <= 900:
    salarioLiquido = salarioBruto - (salarioBruto * Imposto) + 50,00
    print("O salario liquido é: ", salarioLiquido)

else:
    salarioLiquido = salarioBruto - (salarioBruto * Imposto) + 35,00
    print("O salario liquido é: ", salarioLiquido)



