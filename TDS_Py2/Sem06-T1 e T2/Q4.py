def numero(n1,n2,n3,n4,n5):
    media = n1 + n2 + n3 + n4 + n5 // 5
    return media
def main():
     n1 = int(input().strip())
     n2 = int(input().strip())
     n3 = int(input().strip())
     n4 = int(input().strip())
     n5 = int(input().strip())
     minimo = min(n1,n2,n3,n4,n5) 
     maximo = max(n1,n2,n3,n4,n5)
     print(f"A média, o máximo, e mínimo são:",numero(n1,n2,n3,n4,n5),maximo, minimo)
if __name__ == "__main__":
    main()
