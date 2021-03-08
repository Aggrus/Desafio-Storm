# Questão 1 do desafio Fullstack da Storm
# Nome do aplicante: Gustavo Zalcman

def somaParaAlvo(array, alvo): 
    #Checa se o usuario botou os tipos certos nos parametros
    if type(array) != type(list()) or type(alvo) != type(int()):
        return "por favor, bote paramentros no formato (<list>, <int>)\n"
    # Corre o array 
    for index, element in enumerate(array[:-1]):
        # Se o elemento for um dos certos a diferença do alvo com ele dará o outro elemento
        if (alvo - element) in array:
            return [index, array.index(alvo - element)]
    return "Nenhum resultado..."

def main():
    arr1 = [9,3,2,4,5,-30, -19]
    alvo1 = arr1[0]+arr1[-1]

    arr2 = [2,7, 11, 15]
    alvo2 = 9

    print(somaParaAlvo(arr1,alvo1), "\n")
    print(somaParaAlvo(arr2,alvo2))
    return

main()