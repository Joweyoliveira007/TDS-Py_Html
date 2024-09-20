#CRiando uma função chamada true_false com o parâmetro alfabeto
def true_false(alfabeto):
#A classe retorna o parâmetro alfabeto com o valor booleano
    return alfabeto.upper()in"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#A classe retorna a função em main
def main():
    alfabeto = input().strip() 
#Processamento e Saída de dados
    print (true_false(alfabeto))
#Finalizando o código
if __name__ == "__main__":
    main()