def e_par(n):  
    if n % 2 == 0: 
        return True  
    else:
        return False 
def e_par_dezena(n):
    if n // 10:
        return True
    else:
        return False
    

def main():
    numero = int(input()) 
    resultado = e_par_dezena(numero)
if __name__ == "__main__":
    main()
