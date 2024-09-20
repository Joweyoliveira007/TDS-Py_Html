#Criando uma função chamada condicoes que recebe dois parâmetros: num e resto.
def condicoes(num, resto):
#Esta linha verifica se o valor de resto é igual a 0.    
    if resto == 0:
#Se resto for igual a 0, a função retorna o resultado da expressão (9 * num) + 7.         
        return (9 * num) + 7
#Caso contrário (se resto não for igual a 0), verificamos se resto é igual a 1.    
    elif resto == 1:
#Se resto for igual a 1, a função retorna a string 'par' se num for par, caso contrário, retorna a string 'ímpar'.        
        return "par" if num % 2 == 0 else "ímpar"
#Se resto não for igual a 1, verificamos se resto é igual a 2.
    elif resto == 2:
#Se resto for igual a 2, a função retorna o resultado da expressão (5 * num**2) - (3*num) + 42.        
        return (5 * num**2) - (3*num) + 42
#Se resto não for igual a 2, verificamos se resto é igual a 3.    
    elif resto == 3:
#Se resto for igual a 3, a função retorna o resultado da divisão inteira de num por 10.        
        return num // 10
#Se resto não for igual a 3, verificamos se resto é igual a 4.    
    elif resto == 4:
#Se resto for igual a 4, a função retorna o quadrado de num.        
        return num**2
#Entrada
def main():
#Solicitamos ao usuário que insira um número e armazenamos o valor em num.    
    num = int(input("Digite um número: "))
#Calculamos o resto da divisão de num por 5 e armazenamos o resultado em resto.    
    resto = num % 5
#Chamamos a função condicoes com os valores inseridos pelo usuário e imprimimos o resultado.   
    print(f"O total da ação executada: {condicoes(num, resto)}.")
#Verificamos se o script está sendo executado diretamente (não importado como um módulo).    
if __name__ == "__main__":
    main()