#Criando uma função nomeada true_false como o parâmetro simbolos
def true_false(simbolos):
#A classe retorna o parâmetro simbolos com o valor booleano
    return not simbolos in ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
#A classe retorna a função em main 
def main():
    simbolos = input().strip() 
#Processamento e Saída de dados
    print (true_false(simbolos))
#Finalizando o código
if __name__ == "__main__":
    main()