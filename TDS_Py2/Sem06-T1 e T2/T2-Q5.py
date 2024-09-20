def Celsius(valor):
    conta = (valor*(9/5))+32
    return conta
def main():
     (valor) = int(input("Quanto Celsius está fazendo?").strip())
     total = Celsius(valor)
     print(f"A temperatura em Fahrenheit é {total:.2f}" )
    
if __name__ == '__main__':
    main()