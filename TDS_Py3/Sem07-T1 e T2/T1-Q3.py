def cores(sinal_transito):

    if sinal_transito.upper() == "V" :
        return "Siga"
    elif sinal_transito.upper() == "A" :
        return "Atenção"
    else:
        return "Pare"
    
def main():

    sinal = input("")
    resposta = cores(sinal)
    
    print(f"A sua mensagem é: {resposta}")

if __name__ == "__main__":
    main()
    