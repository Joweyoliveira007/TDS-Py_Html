def dinheiro(valor):
    return round(valor)
def main():
     (valor) = float(input("Quanto dinheiro você tem?").strip())
     print(f"Você tem {dinheiro(valor):.2f} em dinheiro")
    
if __name__ == '__main__':
    main()