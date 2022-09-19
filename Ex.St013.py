#13. Altura e sexo (IF)
"""
entrada: a altura e o sexo
1: feminino 2: masculino)
objetivo: calcular e imprimir o peso ideal.
Fórmulas:
para homens: (72.7 * Altura) – 58
para mulheres: (62.1 * Altura) – 44.7
"""

altura = float(input("Digite a sua altura"))
peso = float(input("Digite o seu peso"))
sexo = str(input("Digite o seu sexo: F ou M"))


if sexo == "M":
    peso_ideal_M = (72.7 * altura) - 58
    print("O seu peso ideal é  ", peso_ideal_M)

elif sexo == "F":
    peso_ideal_F = (62.1 * altura) - 44.7
    print("O seu peso ideal é  ", peso_ideal_F)