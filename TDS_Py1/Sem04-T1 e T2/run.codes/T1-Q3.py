def preco_com_aumento(p,perc):
     
     return p + perc
def preco_com_desconto(p,perc):
     
     return p - perc

def main():
     p = float(input("Preço desejado R$"))
     perc = float(input("Percentual desejado R$"))
     aumento = preco_com_aumento(p,perc)
     desconto = preco_com_desconto(p,perc)

     print(f"Preço com aumento R$ {aumento:.2f}")
     print(f"Preço com desconto R$ {desconto:.2f}")

if __name__ == "__main__":
    main()


      