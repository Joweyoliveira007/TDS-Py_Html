#Criando uma função nomeada true_false como o parâmetro vogal
def true_false(vogal):
#A classe retorna o parâmetro vogal com o valor booleano
    return vogal.upper()in"AEIOU"
#Entrada
def main():
    vogal = input().strip() 
#Processamebto e a Saída de dados
    print (true_false(vogal))
#Encerrar o código
if __name__ == "__main__":
    main()