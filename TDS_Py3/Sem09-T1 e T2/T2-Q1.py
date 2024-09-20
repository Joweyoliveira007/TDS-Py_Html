#Criando uma função chamada qual_dia que recebe o parâmetro dia
def dia_semana(Dias):

    if(Dias) == 1:
        return "Domingo"
    if(Dias) == 2:
        return "Segunda-feira"        
    if(Dias) == 3:
        return "Terça-feira"
    if(Dias) == 4:
        return "Quarta-feira"       
    if(Dias) == 5:
        return "Quinta-feira"        
    if(Dias) == 6:
        return "Sexta-feira"      
    if(Dias) == 7:
        return "Sábado"
    else:
        return ValueError("Valor Inválido")
def main():
    Dias = int(input("Digite um número de 1 - 7: "))
    print(f"O Dia da semana referente ao número {Dias} é: {dia_semana(Dias)}!")
if __name__ == "__main__":
    main()