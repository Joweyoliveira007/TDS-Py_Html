def true_false(simbolos):
    return not simbolos in ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
def main():
    simbolos = input().strip() 
    print (true_false(simbolos))
if __name__ == "__main__":
    main()