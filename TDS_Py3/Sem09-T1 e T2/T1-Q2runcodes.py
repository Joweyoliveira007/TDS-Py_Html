def func_num(Adição, Subtração, Multiplicação, Divisão, num):
    
    if num == 1:
        print(Adição)
    elif num == 2:
        print(Subtração)
    elif num == 3:
        print(Multiplicação)
    elif num == 4:
        print(Divisão)

def main():
    num1 = float(input().strip)
    num2 = float(input().strip)
    num = int(input().strip)
    Adição = num1 + num2
    Subtração = num1 - num2
    Multiplicação = num1 * num2
    Divisão = num1 // num2
    print("O resultado é: ")
    func_num(Adição,Subtração,Multiplicação,Divisão,num)
if __name__ == "__main__":
    main()