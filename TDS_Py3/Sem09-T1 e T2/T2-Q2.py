def organ_num(num):
    if 0 < num < 1000:
        unid = num % 10
        num //= 10
        dez = num % 10
        num //= 10
        cem = num % 10
    return cem, dez, unid
def cem_(cem):
    if cem == 1:
        qntd = "Uma centena"
    elif cem == 2:
        qntd = "Duas centenas"
    elif cem == 3:
        qntd = "Três centenas"
    elif cem == 4:
        qntd = "Quatro centenas"
    elif cem == 5:
        qntd = "Cinco centenas"
    elif cem == 6:
        qntd = "Seis centenas"
    elif cem == 7:
        qntd = "Sete centenas"
    elif cem == 8:
        qntd = "Oito centenas"
    else:
        qntd = "Nove centenas"
    return qntd
def dezenas(dez):
    if dez == 1:
        qntd = "Uma dez"
    elif dez == 2:
        qntd = "Duas dezenas"
    elif dez == 3:
        qntd = "Três dezenas"
    elif dez == 4:
        qntd= "Quatro dezenas"
    elif dez == 5:
        qntd = "Cinco dezenas"
    elif dez == 6:
        qntd = "Seis dezenas"
    elif dez == 7:
        qntd = "Sete dezenas"
    elif dez == 8:
        qntd = "Oito dezenas"
    else:
        qntd = "Nove dezenas"
    return qntd
def unidades(unid):
    if unid == 1:
        qntd = "Uma unid"
    elif unid == 2:
        qntd = "Duas unidades"
    elif unid == 3:
        qntd = "Três unidades"
    elif unid == 4:
        qntd = "Quatro unidades"
    elif unid == 5:
        qntd = "Cinco unidades"
    elif unid == 6:
        qntd = "Seis unidades"
    elif unid == 7:
        qntd = "Sete unidades"
    elif unid == 8:
        qntd = "Oito unidades"
    else:
        qntd = "Nove unidades"
    return qntd
def main():
    num = int(input("Digite um número menor que 1000(Mil): "))
    cen, dez, un = organ_num(num)
    print(f"A quantidade de centenas, dezenas e unidades do número lido, por extenso é: ")
    if cen > 0 and dez > 0 and un > 0:
        print(f"{cem_(cen)}, {dezenas(dez)} e {unidades(un)}.")
    elif cen == 0 and dez == 0 and un > 0:
        print(f"{unidades(un)}.")
    elif cen == 0 and dez > 0 and un == 0:
        print(f"{dezenas(dez)}.")
    elif cen > 0 and dez == 0 and un == 0:
        print(f"{cem_(cen)}.")
    elif cen == 0 and dez > 0 and un > 0:
        print(f"{dezenas(dez)} e {unidades(un)}.")
    elif cen > 0 and dez > 0 and un == 0:
        print(f"{cem_(cen)} e {dezenas(dez)}.")
    elif cen > 0 and dez == 0 and un > 0:
        print(f"{cem_(cen)} e {unidades(un)}.")
if __name__ == "__main__":
    main()