#Criando uma função chamada menor_diferenca que recebe três argumentos:n1,n2 e n3.
def menor_diferenca(n1, n2, n3):
#Esta linha calcula a diferença absoluta entre n1 e n2, e a diferença absoluta entre n1 e n3. Em seguida, verifica se a primeira diferença é menor do que a segunda.  
    if abs(n1 - n2) < abs(n1 - n3):
#Se a diferença entre n1 e n2 for menor do que a diferença entre n1 e n3, a função retorna a primeira diferença absoluta.
        return abs(n1 - n2)
#Caso contrário (se a segunda diferença for menor ou igual à primeira), o fluxo de controle vai para o bloco else.
    else:
#A função retorna a segunda diferença absoluta.
        return abs(n1 - n3)
#Entrada
def main():
#Solicitamos ao usuário que insira o valor do primeiro número.
    n1 = int(input("Digite o primeiro número: "))
#Solicitamos ao usuário que insira o valor do segundo número.
    n2 = int(input("Digite o segundo número: "))
#Solicitamos ao usuário que insira o valor do terceiro número.
    n3 = int(input("Digite o terceiro número: "))
#Chamamos a função menor_diferenca com os valores inseridos pelo usuário e imprimimos o resultado.
    print(f"A menor diferença é a de {menor_diferenca(n1, n2, n3)}.")
#Encerrando o código    
if __name__ == "__main__":
    main()