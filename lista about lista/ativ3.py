num = [1,2,3,4,5,6,7,8,9,10]
tamanho = len(num)
for i in range(tamanho // 2):
    num[i], num[tamanho - 1 - i] = num[tamanho - 1 - i], num[i]

print(num)