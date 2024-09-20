def horas_minutos(tempo):
    horas = (tempo // 60) //60  
    return horas
def minutos_hora(tempo):
    minutos = (tempo // 60) % 60
    return minutos
def minutos_segundos(tempo):
    segundos = tempo % 60
    return segundos
def main():
     tempo = int(input().strip())
     minutos = (minutos_hora(tempo))
     horas = (horas_minutos(tempo))
     segundos = (minutos_segundos(tempo))
     print(f"{horas:0.2f}"+":"+f"{minutos:0.2f}"+":"+f"{segundos:0.2f}")
if  __name__  ==  "__main__":
    main()