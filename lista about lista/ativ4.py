lista_compras = []
while True:
    compras = input("Digite o iten que voce deseja comprar ou stop (para parar): ")

    if compras == "stop":
        break

    lista_compras.append(compras)
    
print("Lista de compras: ")
for item in lista_compras:
    print(item)