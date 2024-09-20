def valor(numero):
    return numero  
def main():
    numero = float(input("Digite um número: "))
    numero = round(numero, 2) 
    print(f"Arredondado: {numero}")
if __name__ == "__main__":
    main()