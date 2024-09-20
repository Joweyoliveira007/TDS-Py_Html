def dono_da_loja00(valor):
    a_vista = 9 * 100 - valor
    return a_vista
def dono_da_loja01(valor):
    em_5_vezes = valor
    return em_5_vezes
def dono_da_loja02(valor):
    juros_em_10 = 17 * 100 + valor
    return juros_em_10
def main():
     valor = float(input("Qual o valor do produto?"))
     a_vista = str(dono_da_loja00(valor)) 
     em_5_vezes = str(dono_da_loja01(valor)) 
     juros_em_10 = str(dono_da_loja02(valor))

     print (f"Valor para pagamento à vista é: ",valor + "Valor da prestação para pagamento em 5 vezes é: ", + valor +"Valor da prestação para pagamento em 10 vezes é: ", + valor)
if  __name__  ==  "__main__" :
    main()