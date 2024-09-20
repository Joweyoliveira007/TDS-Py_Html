def true_false(alfabeto):
    return alfabeto.upper()in"ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    alfabeto = input().strip() 

    print (true_false(alfabeto))

if __name__ == "__main__":
    main()