def maçã(valor01):
    return valor01 * 3
def banana(valor02):
    return valor02 * 2
def main():
     (valor01) = int(input("Quanto custa a maçã?").strip())
     (valor02) = int(input("Quanto custa a banana?").strip())
     total = maçã(valor01) + banana(valor02)
     print(f"O preço da maçã e da banana no total é:R${total:.2f}" )
    
if __name__ == '__main__':
    main()