# 1. Estruturas condicionais e de repetição: Preço de produtos (Swich Case)
"""
Faça um programa que receba o preço, a categoria
(1 limpeza; 2alimentação; ou 3vestuário) e
 a situação (R produtos que necessitam de refrigeração;
e N produtos que não necessitam de refrigeração). Calcule e mostre:
O valor do aumento, usando as regras que se seguem na tabela (ver tabela no canva)
"""

#refazer esse programa, fazer alterações.

preco, precoAumento, imposto, novoPreco = float
categoria = int
situacao = str
imposto = 0.08

print("Qual o preço: ")
input(preco)

print("Qual o categoria: ")
input(categoria)

print("Qual a situaçäo: ")
input(situacao)

if  preco <= 25:
    if categoria != 1:
        pass
    else:
        precoAumento = preco * 1.05
        novopreco = precoAumento * (1 - imposto)  #5% do preco acumulado , do 100

    if novoPreco > 50:
        pass
    else:
        print("barato")
    if not:
    print("normal")

    else:
    print("caro")

elif:
    categoria == 2 or situacao == "R":
    precoAumento = preco * 1.05
    novopreco = precoAumento * (1 - 0.05)
    if (novoPreco <= 50):
    print("barato")
    if not:
    print("normal")
    else:
    print("caro")

    else:
    precoAumento = preco * 1.10
    novopreco = precoAumento * (1 - imposto)

    if (novoPreco <= 50):
    print("barato")
    if not:
        print("normal")
    else:
        print("caro")

if preco > 25
    if categoria == 1:
        precoAumento = preco * 1.12
        novopreco = precoAumento * (1 - imposto)

    if novoPreco <= 50:
    print("barato")
    if not (novoPreco > 50 and <= 120):
        print("normal")
    else:
        print("caro")
    elif:
        categoria == 2 or situacao == "R":
        precoAumento = preco * 1.05
        novopreco = precoAumento * (1 - 0.05)
    if novoPreco <= 50):
    print("barato")
    if not:
    print("normal")
    else:
    print("caro")

    else:
    precoAumento = preco * 1.10
    novopreco = precoAumento * (1 - imposto)

    if (novoPreco <= 50):
    print("barato")
    if not:(novoPreco > 50 and <= 120):
         print("normal")
    else:
        print("caro")
