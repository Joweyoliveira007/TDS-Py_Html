def calcular_custo_final(custo_fabrica):
    percentagem_distribuidor = 0.28
    percentagem_impostos = 0.45

    valor_distribuidor = custo_fabrica * percentagem_distribuidor
    valor_impostos = custo_fabrica * percentagem_impostos

    custo_final = custo_fabrica + valor_distribuidor + valor_impostos

    return custo_final
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))
custo_final = calcular_custo_final(custo_fabrica)
print(f"O custo final ao consumidor é: R${custo_final:.2f}")
