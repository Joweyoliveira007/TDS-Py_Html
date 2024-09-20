try: 
    file = open("dou(c)mento.txt", "x")
    file.write("Só alegria HA! ha! HA!")
    file.close()

except FileExistsError:
    print("O arquivo já existe.")