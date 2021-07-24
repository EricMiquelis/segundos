numero = int(input("Digite um número em segundos para converter: "))

dias = numero // 86400
segundos = numero % 86400
horas = segundos // 3600
segundos = segundos % 3600
minutos = segundos // 60
segundos = segundos % 60

print(dias,"dias,", horas,"horas,", horas,"minutos e", segundos,"segundos.")
