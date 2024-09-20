def horas_minutos(tempo):
    horas = tempo // 60   
    return horas
def minutos_hora(tempo):
    minutos = tempo % 60
    return minutos
def minutos_segundos(tempo):
    segundos = tempo % 60
    return segundos
def main():
     tempo = float(input("Quantos minutos são?"))
     minutos = str(minutos_hora(tempo))
     horas = str(horas_minutos(tempo))
     segundos = str(minutos_segundos(tempo))
     print(f"Em horas, minutos e segundos são:" ,horas +":"+ minutos+":"+segundos)
if  __name__  ==  "__main__":
    main()