# Questão 3 do desafio Fullstack da Storm
# Nome do aplicante: Gustavo Zalcman

def findProfit(array):
    profitMargin = list()

    for day, price in enumerate(array):
        if price == max(array[day:]):
            continue
        else:
            profitMargin.append([day, array.index(max(array[day:])),max(array[day:]) - price])
    
    bigBucks = biggestProfit(profitMargin)

    if bigBucks == 0:
        print("0 (Nesse caso nenhuma transação deve ser feita, lucro máximo igual a 0)")
    else:
        print (bigBucks[2], " (Comprou no dia ", bigBucks[0] + 1, " (preço igual a ", array[bigBucks[0]], ")", end = "")
        print (" e vendeu no dia ", bigBucks[1] + 1, " (preço igual a ", array[bigBucks[1]], ") lucro foi de ", end = "")
        print (array[bigBucks[1]], " - ", array[bigBucks[0]], " = ", bigBucks[2])

def biggestProfit(profitMargin):
    if not profitMargin:
        return 0
    profits = [row[2] for row in profitMargin]
    profitInfo = profitMargin[profits.index(max(profits))]
    return profitInfo


def main():
    prices = [9,21,7,1,5,8,15,2]
    print (prices, "\n")
    findProfit(prices)

main()