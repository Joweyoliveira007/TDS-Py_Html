def valores(v1,v2,v3):
    if v1 == v2 in v1 != v2:
        print("O primeiro é o maior ou igual ")
    elif v1 == v3 in v1 != v3:
        print("O segundo é o maior ou igual ")
    elif v3 == v2 in v3 != v2: 
        print("O terceiro é o maior ou igual ")
    else:
        print("São todos diferentes")
def main():
    v1 = int(input("Digite um número de sua escolha:")) 
    v2 = int(input("Digite um número de sua escolha:")) 
    v3 = int(input("Digite um número de sua escolha:"))
    conta = v1,v2,v3
    print(f"{valores(conta).0f}")
if __name__ == "__main__":
    main()