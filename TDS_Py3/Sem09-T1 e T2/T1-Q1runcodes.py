def inf(num1, num2, num3):
    if (num1 != num2 and num1 != num3 and num2 != num3):
        return "Todos os valores são diferentes"
    else:
        return "Todos os valores são iguais" if (num1 == num2 == num3) else "Existem dois valores iguais e um diferente"
      
def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    
    print(f'{inf(num1, num2, num3)}')
    
if __name__ == '__main__':
    main()