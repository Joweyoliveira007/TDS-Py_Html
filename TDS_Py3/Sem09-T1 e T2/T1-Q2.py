#CRiando a função func_num com cinco parâmetros:Adição,Subtração,Multiplicação,Divisão e num
def func_num(Adição, Subtração, Multiplicação, Divisão, num):
#Dentro da função func_num, verifica o valor de num e imprime o resultado com base na operação.
    if num == 1:
        print(Adição)
    elif num == 2:
        print(Subtração)
    elif num == 3:
        print(Multiplicação)
    elif num == 4:
        print(Divisão)
#Entrada
def main():
#Lê dois números de ponto flutuante da entrada do usuário.
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite um número: "))
#Lê um número inteiro representando a operação 1 para adição,2 para subtração,3 para multiplicação,4 para divisão.
    num = int(input("Digite um número: "))
#Calcula os resultados para cada operação.
    Adição = num1 + num2
    Subtração = num1 - num2
    Multiplicação = num1 * num2
    Divisão = num1 // num2
#Processamento e Saída de dados
#Imprime o cabeçalho “O resultado é:”.
    print("O resultado é: ")
#Chama a função func_num para imprimir o resultado apropriado com base na operação selecionada.
    func_num(Adição,Subtração,Multiplicação,Divisão,num)
#Encerrando o código
if __name__ == "__main__":
    main()