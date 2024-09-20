#Criando uma função eh_quadrado que recebe dois parâmetros:base e altura.
def eh_quadrado(base, altura):
#Esta linha verifica se a base é igual à altura.
    if base == altura:
#Se a base for igual à altura,a função retorna a string "QUADRADO".
        return "QUADRADO"
#Caso contrário se a base não for igual à altura, o fluxo de controle vai para o bloco.
    else:
#Calculamos o perímetro do quadrado ou retângulo somando duas vezes a base com duas vezes a altura.
        perimetro = (base * 2) + (altura * 2)
#Calculamos a área multiplicando a base pela altura.
        area = base * altura
#A função retorna uma string formatada com os valores do perímetro e da área,arredondados para zero casas decimais
        return (f'{perimetro:.0f} - {area:.0f}') 
#Entrada
def main():
#Solicitamos ao usuário que insira o valor da base do triângulo 
    base = int(input("Digite o valor da base do triângulo: "))
#Solicitamos ao usuário que insira o valor da altura do triângulo.
    altura = int(input("Digite o valor da altura do triângulo: "))
#Chamamos a função eh_quadrado com os valores inseridos pelo usuário e imprimimos o resultado.   
    print(f"{eh_quadrado(base, altura)}")
#Encerrando o código
if __name__ == "__main__":
    main()