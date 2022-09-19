# Idade de um nadador (IF)
# Dev: Karina Zimerer
# Data: 23.08.2022
"""
Faça um programa que receba a idade de um nadador e mostre sua categoria, usando as regras a seguir.
Para idade inferior a 5, qual mensagem deveríamos mostrar?
CATEGORIA					IDADE
Infantil					5 a 7
Juvenil						8 a 10
Adolescente					11 a 15
Adulto						16 a 30
Sênior						Acima de 30

"""

idade = int(input("Digite a sua idade:  "))


if idade >= 5 and idade <= 7:
    print("A categoria do nadador é Infantil")
if idade >= 8 and idade <= 8:
    print("A categoria do nadador é Juvenil")
if idade >= 11 and idade <= 15:
    print("A categoria do nadador é Adolescente")
if idade >= 16 and idade <= 30:
    print("A categoria do nadador é Adulto")
if idade > 30:
    print("A categoria do nadador é Sênior")
if idade < 5:
    print("Essa categoria é inválida")
if idade < 5:
    print("Essa categoria é inválida")



