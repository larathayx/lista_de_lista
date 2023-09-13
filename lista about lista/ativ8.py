quant = int(input("Digite a quantidade de numeros que voce deseja: "))
list_num = []
for x in range (0, quant):
    num = input("Digite o numero: ")
    list_num.append(num)

maior_numero = list_num[0]
menor_numero = list_num[0]

for numero in list_num:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print("O maior número na lista é:", maior_numero)
print("O menor número na lista é:", menor_numero)
