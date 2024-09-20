def num_imc(m,h):
    imc = m / (h*h)
    if imc <18.5:
        return (f"IMC: {imc:.2f}\nCategoria: Abaixo do peso")
    elif 18.5 <= imc <25:
        return (f"IMC: {imc:.2f}\nCategoria: Peso normal")
    elif 25 <= imc <30:
        return (f"IMC: {imc:.2f}\nCategoria: Sobrepeso")
    elif 30 <= imc <35:
        return (f"IMC: {imc:.2f}\nCategoria: Obeso leve")
    elif 35 <= imc <40:
        return (f"IMC: {imc:.2f}\nCategoria: Obeso moderado")
    elif 40 <= imc <45:
        return (f"IMC: {imc:.2f}\nCategoria: Obeso mórbido")
def main():
    m = float(input("Digite seu peso: "))
    h = float(input("Digite sua altura: ")) 
    print(f"""
Categoria:

< 18,5     Abaixo do peso          
< 25       Peso normal
< 30       Sobrepeso
< 35       Obeso leve
< 40       Obeso moderado
>=40       Obeso mórbido                             
    {num_imc(m,h)}""")
if __name__ == "__main__":
    main()