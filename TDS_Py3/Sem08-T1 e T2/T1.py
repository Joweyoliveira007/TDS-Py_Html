print("Primeira data")
dia_1 = int((input("Digite o dia:")))
mes_1 = int((input("Digite o mes:")))
ano_1 = int((input("Digite o ano:")))
print("Segunda data")
dia_2 = int((input("Digite o dia:")))
mes_2 = int((input("Digite o mes:")))
ano_2 = int((input("Digite o ano:")))
if ((ano_2 > ano_1) or ((ano_2 == ano_1) and (mes_2 > mes_1)) or ((ano_2 == ano_1) and (mes_2 == mes_1)) and (dia_2 > dia_1)):
    print(f"A segunda data {dia_2:.2f}-{mes_2:.2f}-{ano_2:.0f} é mais recente que a primeira: {dia_1:.2f}-{mes_1:.2f}-{ano_1:.0f}")
else:
    print(f"A primeira data {dia_1}-{mes_1}-{ano_1} é mais recente que a segunda: {dia_2}-{mes_2}-{ano_2}")