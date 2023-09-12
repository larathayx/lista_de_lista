quant = int(input("Digite a quantidade de numeros que voce deseja: "))
list_num = []
for x in range (quant):
    numeros = float(input("Digite o numero: "))
    list_num.append(numeros)

soma = 0
for numero in list_num:
    soma += numero

print("A lista de números é: ", list_num)
print("A soma dos números na lista é: ", soma)