def qual_dia(dia):
    if dia == 1:
        return 'Domingo'
    if dia == 2:
        return 'Segunda-feira'        
    if dia == 3:
        return 'Terça-feira'
    if dia == 4:
        return 'Quarta-feira'       
    if dia == 5:
        return 'Quinta-feira'        
    if dia == 6:
        return 'Sexta-feira'       
    if dia == 7:
        return 'Sábado'
    else:
        return ValueError('valor inválido')

def main():
    dia = int(input('Digite um número de 1 - 7: '))
    
    print(f'O dia da semana referente ao número {dia} é: {qual_dia(dia)}!')
    
if __name__ == '__main__':
    main()