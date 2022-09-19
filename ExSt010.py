# 10. Validar senha (IF)
# Dev: Karina Zimerer
# Data: 31.08.2022
"""
Escreva um programa que verifique a validade de uma senha fornecida pelo usuário.
A senha válida é o número 1234.
Devem ser impressas as seguintes mensagens:
ACESSO PERMITIDO caso a senha seja válida e
ACESSO NEGADO caso a senha seja inválida.
"""

senha = int

print("Digite a sua senha de 4 digitos")
input(senha)

if senha == 1234:
    print("ACESSO PERMITIDO")
else:
    print(" ACESSO NEGADO")
