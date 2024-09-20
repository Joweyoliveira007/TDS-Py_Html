def true_false(vogal):
    return vogal.upper()in"AEIOU"
def true_false(consoante):
    return consoante.upper()in "BCDFGHJKLMNPQRSTVWXYZ"
def true_falsee(numero):
    return numero.upper()in "0123456789"
def true_false(simbolos):
    return simbolos.upper()in "`^^:;.,_-'!@#$%¨&*()|\=+§ªº¬¢£³²¹?°~"
def main():
    vogal = input().strip() 
    print (true_false(vogal))
    consoante = input().strip() 
    print (true_false(consoante))
    numero = input().strip()
    print (true_falsee(numero))
    simbolos = input().strip()
    print (true_false(simbolos))
    
if __name__ == "__main__":
    main()