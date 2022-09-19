# 2. Idade e peso (IF)
# Dev: Karina Zimerer
# Data: 23.08.2022

idade = int(input("Digite a sua idade:  "))
peso = float(input("Digite o seu peso:  "))

if idade < 20 and peso <= 60:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 9")
elif:
    idade < 20 and peso > 60 and peso <= 90:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 8")
elif:
    idade < 20 and peso > 90:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 7")
elif:
    idade >= 20 and idade <= 50 and peso <= 60:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 6")
elif:
    idade >= 20 and idade <= 50 and peso > 60 and peso <= 90:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 5")
elif:
    idade >= 20 and idade <= 50 and  peso > 90:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 4")
elif:
    idade > 50 and  peso <= 60:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 3")
elif:
    idade > 50 and  peso > 60 and peso <= 90:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 2")
elif:
    idade > 50 and peso > 90:
    print("Com", idade, "anos e  no peso de", peso, "kilos, você está no grau de risco 1")









