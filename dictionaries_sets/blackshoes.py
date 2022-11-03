blackShoes ={42:2,41:3, 40:4, 39:1, 38:0}
print (blackShoes)
while (True):
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    if purchaseSize < 0:
        break
    if blackShoes.purchaseSize > 0:
        blackShoes.purchaseSize -= 1
    else:
        print("Shoes are no longer in stock")
        
    print(blackShoes)