def máximo_num(n1,n2,n3,n4,n5):
    maximo = n1
    if n2 > maximo:
        maximo = n2
    if n3 > maximo:
        maximo = n3
    if n4 > maximo:
        maximo = n4
    if n5 > maximo:
        maximo = n5
    return maximo
def mínimo_num(n1,n2,n3,n4,n5):
    minimo = n2
    if n2 > minimo:
        minimo = n2
    if n3 > minimo:
        minimo = n3
    if n4 > minimo:
        minimo = n4
    if n5 > minimo:
        minimo = n5
    return minimo 
def main():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundon úmero: "))
    n3 = int(input("Digite o terceiro número: "))
    n4 = int(input("Digite o quarto número: "))
    n5 = int(input("Digite o quinto número: "))
    print(f"O máximo: {máximo_num(n1,n2,n3,n4,n5)}\no mínimo: {mínimo_num(n1,n2,n3,n4,n5)}")
if __name__ == "__main__":
    main()