quant = int(input("Digite a quantidade de numeros que voce deseja: "))
list_num = []
for x in range (quant):
    numeros = int(input("Digite o numero: "))
    list_num.append(numeros)

lista_num2 = []

for elemento in list_num:
    if elemento not in lista_num2:
        lista_num2.append(elemento)
    else:
        list_num.remove(elemento)

print("Lista sem duplicatas:", lista_num2)