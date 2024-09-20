def caracteres(teclado):

    if teclado.upper() in "AEIOU" :
        return "vogal"
    elif teclado.upper() in "BCDFGHJKLMNPQRSTVWXYZ" :
        return "consoante"
    elif teclado.upper() in "0123456789" :
        return "número"
    else:
        return "símbolos"
    
def main():
    sinal = input("Anote aleatoriamente: ")
    resposta = caracteres(sinal)
    print(f"{resposta}")

if __name__ == "__main__":
    main()
    