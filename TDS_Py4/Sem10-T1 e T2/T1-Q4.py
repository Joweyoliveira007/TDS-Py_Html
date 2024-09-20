# Inicializando uma lista vazia
sequencia = []

# Gerando a sequência
for i in range(10, 1001, 10):
    sequencia.append(str(i))

# Juntando os números com ', ' e adicionando '.' no final
sequencia_formatada = ', '.join(sequencia) + '.'

print(sequencia_formatada)