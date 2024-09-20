def hora_e_minuto(tempo):
    hora = tempo // 60
    return hora
def hora_e_minuto01(tempo):
    minuto = tempo % 60
    return minuto
def main():
     tempo = int(input("Quantos minutos são?"))
     minuto = str(hora_e_minuto01(tempo))
     hora = str(hora_e_minuto(tempo))

     print(f"Esses minutos são em horas e minutos:",hora +":"+ minuto)

if __name__ == "__main__":
    main()