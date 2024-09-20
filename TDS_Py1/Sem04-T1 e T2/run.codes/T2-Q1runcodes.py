def true_false(vogal):

    return vogal.upper()in"AEIOU"
def main():
    
    vogal = input().strip() 
    print (true_false(vogal))
if __name__ == "__main__":
    main()