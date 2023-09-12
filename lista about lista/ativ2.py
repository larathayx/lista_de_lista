quant = int(input("Digite a quantidade de palavras que voce deseja: "))
list_words = []
for x in range (0, quant):
    palavra = input("Digite a palavra: ")
    list_words.append(palavra)

list_words5 = []

for word in list_words:
    if len(word) > 5:
        list_words5.append(word)

print("As palavras com mais de 5 letras são:", list_words5)