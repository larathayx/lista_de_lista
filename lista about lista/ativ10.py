quant = int(input("Digite a quantidade de numeros que voce deseja: "))
list_num = []
for x in range (quant):
    numeros = int(input("Digite o numero: "))

    if numeros % 2 == 0:
        numeros = 0
        list_num.append(numeros)
    else:
        list_num.append(numeros)

print (list_num)
