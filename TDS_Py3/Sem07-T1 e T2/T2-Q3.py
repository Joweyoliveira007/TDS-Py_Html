def e_par(num, n):
    if (num % 10) % 2 != 0:
        n += 1
    num = num // 10
    if num % 2 != 0:
        n += 1 
    if n == 0:
        return "Não tem número ímpar."
    if n == 1:
        return "Apenas um número é ímpar."
    else:
        return "Os dois números são ímpares."
def main():
    num = int(input("Digite um número de 10 a 99: "))
    n = 0
    print(f"O número {num} tem {e_par(num, n)}")
if __name__ == "__main__":
    main()