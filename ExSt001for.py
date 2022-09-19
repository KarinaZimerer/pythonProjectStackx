#1. Estruturas condicionais e de repetição: Aumento salarial (FOR)
"""
Um funcionário de uma empresa recebe, anualmente, aumento salarial. Sabe-se que:
a) esse funcionário foi contratado em 2000, com salário inicial de R$1.000,00;
b) Em 2001, ele recebeu aumento de 1,5%, sobre o seu salário inicial;
c) A partir de 2002 (inclusive), os aumentos salariais sempre corresponderam
ao *dobro* do percentual do ano anterior.
Faça um programa que determine o salário desse funcionário dos anos de 2000 à 2017.
Apresente todos os valores.
"""
SalarioInicial = PercentualAumento = ReajusteSalarialAnual = SalarioAcumulado = 0
AnoInicial = 2000
AnoFinal = 2018

for i in range(AnoInicial, AnoFinal, 1):
    if i == 2000:
        SalarioInicial = 1000.00
        print(i, "SI: ", SalarioInicial, "%:", PercentualAumento, "RS (R$):", ReajusteSalarialAnual, "SA:",SalarioAcumulado)
    elif i == 2001:
        PercentualAumento = 0.0015
        ReajusteSalarialAnual = SalarioInicial * PercentualAumento
        SalarioAcumulado = SalarioInicial + ReajusteSalarialAnual
        print(i, "SI: ", SalarioInicial, "%:", round(PercentualAumento, 6), "RS (R$):", round(ReajusteSalarialAnual, 2), "SA:",SalarioAcumulado)
    else:
       # print(i, "SA: ", round(SalarioAcumulado, 2))
        ReajusteSalarialAnual = SalarioAcumulado * PercentualAumento
        SalarioAcumulado = SalarioAcumulado + ReajusteSalarialAnual
        print(i, "PA: ",round(PercentualAumento, 5), f"\tRS: {ReajusteSalarialAnual:,.2f}", f"\t\t\tSA: {SalarioAcumulado:,.2f}")
    PercentualAumento *=2