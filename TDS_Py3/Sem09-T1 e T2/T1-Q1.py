#Criando a função valor com três parâmetros n1,n2 e ,n3
def valor(n1,n2,n3):
#SE o n1 for igual a n2 e igual ao n3
    if n1 == n2 and n1 == n3:
#Retorna a mensagem "Todos os valores são iguais" caso seja verdade
        return ("Todos os valores são iguais")
#SE o n1 for diferente do n2,o n1 for diferente do n3 e o n2 diferente do n3
    if n1 != n2 and n1 != n3 and n2 != n3:
#Retorna a mensagem "Todos os valores são diferentes" caso seja a opção verdadeira
        return("Todos os valores são diferentes")
#Caso as outras opções não sejam as corretas, essa é a última opção
    else:
#Retorna a mensagem caso seja correta
        return("Existem dois valores iguais e um diferente")
#Entrada       
def main():
    num2 = int(input("Digite um número: "))
    num3 = int(input("Digite um segundo número:"))
    num1 = int(input("Digite um  terceiro número:"))
    valores = valor(num1,num2,num3)
#Processamneto e a Saída de dados
    print(valores)
#Encerrar o código
if __name__ == "__main__":
    main()