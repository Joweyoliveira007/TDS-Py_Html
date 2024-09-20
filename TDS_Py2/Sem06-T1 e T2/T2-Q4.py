def anos(Zob):
    return Zob * 0.5
def main():
     Zob = float(input("Quantos anos terrestres deseja anotar?").strip())
     print(f"Em anos espaciais são {anos(Zob):.0f}" )
    
if __name__ == '__main__':
    main()