#2. Estruturas condicionais e de repetição: Compra de produto (Switch Case)
"""
Faça um programa que receba:
O código do produto comprado; e
A quantidade comprada do produto.
Calcule e mostre:
O preço unitário do produto comprado, seguindo a Tabela abaixo;
O preço total da nota;
O valor do desconto, seguindo a Tabela (no conteudo do canva) e aplicado sobre o preço total da nota; e
O preço final da nota depois do desconto.
CODIGO      PREÇO       PRECO TOTAL DA NOTA              % DE DESCONTO
1 a 10      R$10.00     Até R$250,00                     5%
11 a 20     R$15,00     Entre R$250,00 e R$500,00        10%
21 a 30     R$20.00     Acima de R$50,00                 15%
31 a 40     R$30.00     -----------------------------------------------
"""

codigo = int(input("código do produto: "))
qnt = int(input("Quantidade: "))
precoUnit, precoTotal = float

#no python nao tem swtch case, usar condicionais, if, elif, else if os permitem selecionar certos blocos de código


#sintaxe:

condicao_1 = False
condicao_2 = False

if condicao_1:
    print("A condicao_1 é verdadeira.")
elif condicao_2:
    print("A condicao_2 é verdadeira.")
else:
    print("As condições: condicao_1 e condicao_2 são falsas.")




