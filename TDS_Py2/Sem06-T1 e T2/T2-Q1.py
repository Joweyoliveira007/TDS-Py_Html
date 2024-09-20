def escrever(frase):
    return len(frase)

def main():
     frase = input("Digite uma frase:")
     print(f"Essa frase tem: {escrever(frase):.0f}")
    
if __name__ == '__main__':
    main()