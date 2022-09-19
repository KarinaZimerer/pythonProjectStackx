# 6.Receber nomes e salários (While)
# Dev: Karina Zimerer
# Data: 30.08.2022

"""
objetivo: fazer um programa para receber o  salario do funcionario Carlos
-salario de Joao é equivalente a 1/3 do salario de Carlos
-Carlos aplicara seu salario na Poupanca == Rendimento da Poupanca de Carlos: 2% ao mes (0.02)
-Joao aplicara seu salario integramente no fundo de renda fixa ==  fundo de renda fixa de Joao rende 5% ao mes (0.05)
-O programa deverá calcular e mostrar a: quantidade de meses necessários para que o valor pertencente
a João IGUALE OU  ultrapasse o valor pertencente a Carlos
- QuantidadeDeMeses do valor do Joao = ou > valor de Carlos
- O salario do Joao ( é 1/3 do salario do Carlos)
"""

Salario = float
ValorPoupanca = float
ValorRenda = float
Nome = str
Meses = 1

RendaPoupanca = 1.02
ValorRendaFixa = 1.05

while True:
    print(" Qual é o nome do funcionário: ")
    input(Nome)
    print("Qual é o salário? ")
    input(Salario)

    if Nome == "Carlos":
        ValorPoupanca = Salario * RendaPoupanca

    else:
        Salario = Salario / 3
        ValorRendaFixa = Salario * ValorRendaFixa

    while True:
        Meses += 1
        if ValorRendaFixa >= ValorPoupanca:
            print("O Valor do funcionario", Nome, "Se igualou ao de Carlos, em", Meses, "Meses")
        else:
            continue
