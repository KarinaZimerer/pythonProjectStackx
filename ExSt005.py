# 5. Empresa com 10 funcionários (While)
# Dev: Karina Zimerer
# Data: 25.08.2022

"""
Uma empresa possui dez funcionários com as seguintes características:
código, número de horas trabalhadas no mês, turno de trabalho
(M – matutino; V – vespertino; N – noturno),
categoria (O – operário; ou G – gerente),
valor da hora trabalhada.
objetivo da empresa: informatizar a folha de pagamento
Fazer um  programa que atenda os seguintes requisitos:
a) Leia as informações dos funcionários, exceto o valor da hora trabalhada,
não permitindo que sejam informações dos turnos e nem categorias inexistentes.
Trabalhe sempre com a digitação de letras maiúsculas;

b) Calcule o valor da hora trabalhada, conforme a tabela 1.
Adote o valor de R$450,00 para o salário mínimo;

c) Calcule o salário inicial dos funcionários com base no valor
da hora trabalhada e no número de horas trabalhadas;

d) Calcule o valor do auxílio alimentação recebido pelo funcionário de acordo com seu salário inicial,
conforme a tabela 2;

e) Mostre o código, número de horas trabalhadas, valor da hora trabalhada, salário inicial,
 auxílio alimentação e salário final (salário inicial + auxílio alimentação).
"""

Codigo = int
HorasTrabalhadasMensais = int
TurnoDeTrabalho = str
Categoria = str
ValorDaHoraTrabalhada = float
SalarioInicial = float
SalarioMinimo = float = 450
SalarioFinal = float
AuxilioAlimentacao = int

laco1: int = 10
laco2: bool = True
laco3: bool = True

while laco1 <= 10:
    print(input(" Digite o Codigo do funcionário:  "))
    print("Digite as horas trabalhadas no mês:  ")
    input(HorasTrabalhadasMensais)
breakpoint(laco1)

while laco2:
    print(input("Digite a Categoria do funcionário "))
    if Categoria == "O" or Categoria == "G":
        laco2 = False
    else:
        print("As categorias possíveis que são O e G, digite novamente...")
        continue
breakpoint(laco2)

while laco3:
    print(input("turno de trabalho"))
    if TurnoDeTrabalho == "M" or TurnoDeTrabalho == "V" or TurnoDeTrabalho == "N":
        laco3 = False
    else:
        print("Os turnos possíveis são M, V, N, digite novamente...")
        continue
breakpoint(laco3)

if Categoria == "G" and  TurnoDeTrabalho == "N":
    ValorDaHoraTrabalhada = SalarioMinimo * 0.18
    SalarioInicial = HorasTrabalhadasMensais * ValorDaHoraTrabalhada
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        if not SalarioInicial >300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        if not
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
breakpoint(Categoria)


if not Categoria == "G" and TurnoDeTrabalho =="M" or TurnoDeTrabalho == "V":
    ValorDaHoraTrabalhada = SalarioMinimo * 0.15
    SalarioInicial = HorasTrabalhadasMensais * ValorDaHoraTrabalhada

    if SalarioInicial <= 300:
        AuxilioAlimentacao = SalarioInicial * 0.20
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
    if not SalarioInicial > 300 and SalarioInicial <= 600:
        AuxilioAlimentacao = SalarioInicial * 0.15
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
    if not
        AuxilioAlimentacao = SalarioInicial * 0.05
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
breakpoint(Categoria == "G" and TurnoDeTrabalho =="M" or TurnoDeTrabalho == "V")

if not Categoria == "O" and TurnoDeTrabalho =="N":
    ValorDaHoraTrabalhada = SalarioMinimo * 0.13
    SalarioInicial = HorasTrabalhadasMensais * ValorDaHoraTrabalhada
    if SalarioInicial <= 300:
        AuxilioAlimentacao = SalarioInicial * 0.20
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
    if not SalarioInicial > 300 and SalarioInicial <= 600:
        AuxilioAlimentacao = SalarioInicial * 0.15
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
    if not
        AuxilioAlimentacao = SalarioInicial * 0.05
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
breakpoint(Categoria == "O" and TurnoDeTrabalho =="N")

if not Categoria == "O" and TurnoDeTrabalho =="M" or TurnoDeTrabalho =="M":
    ValorDaHoraTrabalhada = SalarioMinimo * 0.10
    SalarioInicial = HorasTrabalhadasMensais * ValorDaHoraTrabalhada
    if SalarioInicial <= 300:
        AuxilioAlimentacao = SalarioInicial * 0.20
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
    if not SalarioInicial > 300 and SalarioInicial <= 600:
        AuxilioAlimentacao = SalarioInicial * 0.15
        SalarioFinal = SalarioInicial + AuxilioAlimentacao
    if not
        AuxilioAlimentacao = SalarioInicial * 0.05
        SalarioFinal = SalarioInicial + AuxilioAlimentacao

breakpoint(Categoria == "O" and TurnoDeTrabalho =="M" or TurnoDeTrabalho =="V")

# quadro resumo
print("Codigo: ", Codigo, "Horas trabalhadas: ", HorasTrabalhadasMensais, "Salario Inicial", SalarioInicial)
print( "Auxilio Alimentacao: ", AuxilioAlimentacao, "Salario Final: ", SalarioFinal)

print("Laço Principal", laco1)
laco1 = laco1 + 1
laco2 = True
laco3 = True

print("Fim do programa")

















