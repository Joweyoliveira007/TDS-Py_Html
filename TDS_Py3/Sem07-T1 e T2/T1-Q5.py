def terceira_nota(media, n3):
    if n3 > 8:
        media += 1
    if media > 10:
        media = 10   
    return media
def main():
    n1 = float(input('Digite o valor da sua primeira nota: '))
    n2 = float(input('Digite o valor da sua segunda nota: '))
    n3 = float(input('Digite o valor da sua terceira nota: '))
    media = (n1 + n2 + n3) / 3 
    print(f'A sua média final é: {terceira_nota(media, n3):.2f}!!')
    
if __name__ == '__main__':
    main()
