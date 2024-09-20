def calculo(n1, n2, n3, media_):
    media_final = (n1 + (n2 * 2) + (n3 * 3) + media_) / 7
    
    #conceito média final 
    if media_final >= 9.0:
        return (f'{media_final:.2f}\nA\nAprovado')
    if  7.5 <= media_final < 9.0:
        return (f'{media_final:.2f}\nB\nAprovado')
    if 6.0 <= media_final < 7.5:
        return (f'{media_final:.2f}\nC\nAprovado')
    if 4.0 <= media_final < 6.0 :
        return (f'{media_final:.2f}\nD\nReprovado')
    if media_final < 4.0:
        return (f'{media_final:.2f}\nE\nReprovado')

def main():
    matricula = (input()).strip()
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media_ = float(input())
    
    print(f'{matricula}\n{calculo(n1, n2, n3, media_)}')
    
if __name__ == '__main__':
    main()
    