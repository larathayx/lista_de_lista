quant = int(input("Digite a quantidade de palavras que voce deseja para a primeira lista: "))
list_words1 = []
for x in range (0, quant):
    palavra = input("Digite a palavra: ")
    list_words1.append(palavra)

quant = int(input("Digite a quantidade de palavras que voce deseja para a segunda lista: "))
list_words2 = []
for x in range (0, quant):
    palavra = input("Digite a palavra: ")
    list_words2.append(palavra)

lista3 = []

for  word in list_words1:
    if word in list_words1 and word in list_words2:
        lista3.append(word)
    else:
        break

print("elementos em comum:", lista3)
