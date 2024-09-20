def e_par(num, n):
    if (num % 10) % 2 == 0:
        n = 1
    num = num // 10 
    if (num % 10) % 2 == 0:
        n = n + 1
    num = num // 10
    if num > 0:    
        if num % 2 == 0: 
            n = n + 1 
    return n
def main():
    num = int(input("Digite um número entre 100 e 999: "))
    n = 0
    print(f"O número {num} tem {e_par(num, n)} dígito(s) par(es).")
    
if __name__ == "__main__":
    main()