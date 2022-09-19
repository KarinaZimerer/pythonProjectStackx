# Gratificaçao de Natal(IF)
# Dev: Karina Zimerer
# Data: 23.08.2022

horasExtras = float(input("Digite o número de horas extras: "))
horasFalta = float(input("Digite o número de horas faltantes: "))

totalMinutos = (horasExtras - (2 / 3 * horasFalta)) * 60

if totalMinutos >= 2401:
    print("Minutos totais: ", totalMinutos, "A gratificação será de 500,00")
elif totalMinutos >= 1801 and totalMinutos <= 2401:
    print("Minutos totais: ", totalMinutos, "A gratificação será de 400,00")
elif totalMinutos >= 1201 and totalMinutos <= 1800:
    print("Minutos totais: ", totalMinutos, "A gratificação será de 300,00")
elif totalMinutos >= 600 and totalMinutos <= 1200:
    print("Minutos totais: ", totalMinutos, "A gratificação será de 200,00")
elif totalMinutos < 600:
    print("Minutos totais: ", totalMinutos, "A gratificação será de 100,00")
