# 9. Idade para voto(IF)
# Dev: Karina Zimerer
# Data: 30.08.2022
"""
Escreva um programa para ler o ano de nascimento de uma pesso e
escrever uma mensagem que diga se ela poderá ou não votar este ano
(não é necessário considerar o mês em que ela nasceu).
Jovens de 16 e 17 anos e Idosos com idade acima de 70 anos podem votar
"""

#continuar teste (reformular o programa)

AnoNascimento = int
idade = int(input("Digite a sua idade:  "))
AnoAtual = int(input("Digite o ano atual:  "))
voto = str


def voto (ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return "Com", idade "anos": "Não pode votar."
    elif 16 <= idade < 18 or idade > 65:
        return "Com", idade "anos": "O voto é opcional."
    else:
        return "com", idade "anos": "O voto é obrigatório."

# Programa principal
nasc = int(input("Em que ano você nasceu?"))
print(voto(nasc))

if idade = Anoatual - AnoNascimento:


print(" (Idade = AnoAtual - AnoDeNascimento")
input(" A idade do usuário é: ")


if Idade >= 16:
    print("O usuario tem idade para votar")
    if idade <16:
else:
    print("O usuário não tem idade para votar")

