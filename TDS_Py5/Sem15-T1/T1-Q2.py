def conversor(temp, escalat):
    if escalat.upper() == 'F':
        # Fahrenheit (->) Celsius
        return (temp - 32) * (5/9)
    else:
        # Celsius (->) Fahrenheit
        return (temp * (9/5)) + 32

def somaTemp(temp0, temp1):
    t0, esc0 = temp0
    t1, esc1 = temp1

    if esc0 != esc1:
        t0 = conversor(t0, esc0)

    return round((t0 + t1), 4), esc1

def main():
    temperaturas = []
    escalas = []

    print('Insira duas temperaturas em Celcius(C) ou Fahrenheit(F):')
    while len(temperaturas) < 2:
        temp = float(input('Temperatura: ').strip())
        temperaturas.append(temp)
        escala = str(input('Escala: ').upper()[0])
        escalas.append(escala)

    temp0 = (temperaturas[0], escalas[0])
    temp1 = (temperaturas[1], escalas[1])

    print('A soma entre as duas temperaturas é:', somaTemp(temp0, temp1))

if __name__ == "__main__":
    main()