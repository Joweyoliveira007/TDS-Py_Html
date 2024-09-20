def _mes(dia_nasci, mes_nasci):
    if mes_nasci == 1 and 20 <= dia_nasci <= 30 or mes_nasci == 2 and 1 <= dia_nasci <= 18: 
        return "Aquário"  
    if mes_nasci == 2 and 19 <= dia_nasci <= 30 or mes_nasci == 3 and 1 <= dia_nasci <= 20: 
        return "Peixes"
    if mes_nasci == 3 and 21 <= dia_nasci <= 30 or mes_nasci == 4 and 1 <= dia_nasci <= 19: 
        return "Áries"
    if mes_nasci == 4 and 20 <= dia_nasci <= 30 or mes_nasci == 5 and 1 <= dia_nasci <= 20:
        return "Touro"
    if mes_nasci == 5 and 21 <= dia_nasci <= 30 or mes_nasci == 6 and 1 <= dia_nasci <= 21: 
        return "Gêmeos"
    if mes_nasci == 6 and 22 <= dia_nasci <= 30 or mes_nasci == 7 and 1 <= dia_nasci <= 22:
        return "Câncer"
    if mes_nasci == 7 and 23 <= dia_nasci <= 30 or mes_nasci == 8 and 1 <= dia_nasci <= 22:
        return "Leão"
    if mes_nasci == 8 and 23 <= dia_nasci <= 30 or mes_nasci == 9 and 1 <= dia_nasci <= 22:
        return "Virgem"
    if mes_nasci == 9 and 23 <= dia_nasci <= 30 or mes_nasci == 10 and 1 <= dia_nasci <= 22: 
        return "Libra"
    if mes_nasci == 10 and 23 <= dia_nasci <= 30 or mes_nasci == 11 and 1 <= dia_nasci <= 21:
        return "Escorpião"
    if mes_nasci == 11 and 22 <= dia_nasci <= 30 or mes_nasci == 12 and 1 <= dia_nasci <= 21:
        return "Sagitário"
    if mes_nasci == 12 and 22 <= dia_nasci <= 30 or mes_nasci == 1 and 1 <= dia_nasci <= 19:
        return "Capricórnio"

def main():
    dia_nasci = int(input("Digite o dia do seu nascimento: "))
    mes_nasci = int(input("Digite o mês do seu nascimento: "))
    print(f"Você é de {_mes(dia_nasci, mes_nasci)}!!")

if __name__ == "__main__":
    main()