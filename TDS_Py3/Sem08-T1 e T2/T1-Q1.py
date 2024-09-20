def data(dia1,mes1,ano1): 
    nasci = dia1,mes1,ano1
    return nasci
def idade(dia2,mes2,ano2):
    atual = dia2,mes2,ano2
    return atual
def main():
     dia2 = int(input().strip())
     mes2 = int(input().strip())
     ano2 = int(input().strip())
     dia1 = int(input().strip())
     mes1 = int(input().strip())
     ano1 = int(input().strip())
     resposta1 = dia2 - dia1 
     resposta2 = mes2 - mes1
     resposta3 = ano2 - ano1
     print(f"Você tem {resposta3:.0f} anos,{resposta2:.0f} meses e {resposta1:.0f} dias ")
if __name__ == "__main__":
    main()

