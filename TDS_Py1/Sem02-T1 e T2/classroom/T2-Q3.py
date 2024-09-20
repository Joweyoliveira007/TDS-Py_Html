#Imprime na tela uma frase 
print("Digite seu volume atual e depois seu volume desejado para saber a diferença de volume, para regular o volume do seu dispositivo de som:")
volumeatual=input()
volumeatual=int(volumeatual)
#Imprime na tela o volume desejado
print("Agora digite o volume desejado:")
volumedesejado=input()
volumedesejado=int(volumedesejado)
#Imprime na tela a diferenca de volume
print("A diferença de volume é:",volumedesejado-volumeatual)