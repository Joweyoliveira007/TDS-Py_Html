def e_par(n):
    return n % 2 == 0
def e_par_centena(n):
    centena = n // 100
    return e_par(centena)
def main():
    numero = int(input("Digite de 100 a 999: "))
    resultado = e_par_centena(numero)
    if resultado:
        print(f"O dígito das CENTENAS é PAR.")
    else:
        print(f"O dígito das CENTENAS é ÍMPAR")

if __name__=="__main__":
    main()