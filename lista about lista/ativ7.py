quant = int(input("Digite a quantidade de nomes você quer na lista: "))
lista_nomes = []
nomes_ordenados=[]

for x in range(quant):
    nome = (input("Digite o nome: "))
    lista_nomes.append(nome)

while lista_nomes:
    menor_nome = lista_nomes[0]
    for nom in lista_nomes:
        if nom < menor_nome:
            menor_nome = nom
    nomes_ordenados.append(menor_nome)
    lista_nomes.remove(menor_nome)

print(nomes_ordenados)
