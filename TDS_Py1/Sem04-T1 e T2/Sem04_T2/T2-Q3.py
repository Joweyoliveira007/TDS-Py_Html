#CRiando uma função chamada true_false com o parâmetro consoante
def true_false(consoante):
#A classe retorna o parâmetro alfabeto com o valor booleano
    return consoante.upper()in"BCDFGHJKLMNPQRSTVWXYZ"
#A classe retorna a função em main
def main():
    consoante = input().strip() 
#Processamento e Saída de dados
    print (true_false(consoante))
#Finalizando o código
if __name__ == "__main__":
    main()