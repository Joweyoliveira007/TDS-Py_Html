def main():
# Inicializando contadores
    contagem_pares = 0
    contagem_impares = 0
# Lendo 100 números
    for numero in range(100):
        numero = int(input())
    # Verificando se o número é par ou ímpar
        if numero % 2 == 0:
            contagem_pares += 1
        else:
            contagem_impares += 1
# Imprimindo os resultados
    print(f"{contagem_pares}\n{contagem_impares}")
if __name__ == "__main__":
    main()