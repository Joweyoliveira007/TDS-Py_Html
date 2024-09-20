def true_false(alfabeto):
    return alfabeto.upper()in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def true_falsee(numero):
    return numero.upper()in "0123456789"
def main():
    alfabeto = input().strip() 
    print (true_false(alfabeto))
    numero = input().strip()
    print (true_falsee(numero))

if __name__ == "__main__":
    main()