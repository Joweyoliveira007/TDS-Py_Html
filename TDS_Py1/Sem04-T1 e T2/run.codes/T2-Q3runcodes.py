def true_false(consoante):
    return consoante.upper()in"BCDFGHJKLMNPQRSTVWXYZ"
def main():
    consoante = input().strip() 
    print (true_false(consoante))
if __name__ == "__main__":
    main()