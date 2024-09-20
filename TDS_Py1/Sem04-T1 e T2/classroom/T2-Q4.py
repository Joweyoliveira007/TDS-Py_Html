#CRiando uma função chamada true_false com o parâmetro alfabeto
def true_false(alfabeto):
#A classe retorna o parâmetro alfabeto com o valor booleano
    return alfabeto.upper()in"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#CRiando uma função chamada true_false com o parâmetro numero
def true_falsee(numero):
#A classe retorna o parâmetro numero com o valor booleano
    return numero.upper()in"0123456789"
#A classe retorna a função em main
def main():
    alfabeto = input().strip() 
    numero = input().strip()
#Processamento e Saída de dados
    print (true_false(alfabeto))
    print (true_falsee(numero))
#Finalizando o código
if __name__ == "__main__":
    main()