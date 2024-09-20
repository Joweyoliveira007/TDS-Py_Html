def valor(produto,cliente):
        return cliente - produto
def main():
    produto = float(input())
    cliente = float(input())
    troco = valor(produto, cliente)
    if cliente - produto >= 0:
        print(f"{troco:.2f}")
    else:
        print("Pagamento Insuficiente")
if __name__== "__main__":
    main()

