total = 0 
while True:
    preco = input("Digite o preço do produto: ")
    if preco == "=":
        print("O valor total das compras é: ", total)
        break
    else:
        total = total + float(preco) #Acumulador