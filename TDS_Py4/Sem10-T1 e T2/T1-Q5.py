def main():
    numeros = 0

    for i in range(100):
        i = int(input())
        if i > numeros:
            numeros = i

    print(f"{numeros}")

if __name__ == "__main__":
    main()