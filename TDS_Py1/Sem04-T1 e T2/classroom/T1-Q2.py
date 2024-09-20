#Função da área do quadrado
def area_quadrado(num):
    a = num**2
    return a
#Função do perímetro quadrado
def area_perimetro(num):
    p = num*4
    return p

#Bloco principal de código
def main():

#Entrada
    lado = float(input("Valor do lado do quadrado:"))
#Processamento
    area = area_quadrado(lado)
    perimetro = area_perimetro(lado)
#Saída
    print(f"O valor da área é{area:10.4f}m² e o perímetro do quadrado é{perimetro:10.4f}m")

if __name__== '__main__':
     main()
    
