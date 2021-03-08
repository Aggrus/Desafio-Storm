# Questão 2 do desafio Fullstack da Storm
# Nome do aplicante: Gustavo Zalcman

def bracketMaker():
    return input("Bote uma cadeia de caracteres formada de parenteses colchetes e chaves ('()','[]', '{}'): ")

#Bracket Balance Checker
def BBC(brackets):
    openList = list() #Lista das brackets abertas em "brackets"

    #Check primário para ver se há algo em brackets, se o numero de brackets é par 
    # (se for impar automaticamente nao eh balancado), e se brackets comeca com um símbolo de fechar
    # ou termina com um símbolo de abrir
    if  not brackets or len(brackets) % 2 != 0 or isOpen(brackets[-1]) or not isOpen(brackets[0]):
        return "NAO"
    for i, element in enumerate(brackets):
        #Se o elemento atual é um bracket aberto ele é adicionado ao fim de OpenList
        if isOpen(element):
            openList.append(element)
        #Se o elemento atual for fechado e não corresponder com o último bracket aberto da sequencia
        # ou se for um bracket fechado quando não existem brackets abertos à sua esquerda quer dizer que
        # a sequência não é balanceada
        elif not isOpen(element) and (not openList or bracketType(element) != bracketType(openList[-1])):
            return "NAO"
        #Se o elemento atual for fechado e o último símbolo aberto for correspondente, tirar ele da 
        # lista de abertos
        elif not isOpen(element) and bracketType(element) == bracketType(openList[-1]):
            openList.pop()
    #Se todos os brackets abertos foram fechados corretamente então a sequência é equilibrada
    if not openList:
        return "SIM"
        
def isOpen(brack):
    openBrackets = ['{', '[', '(']
    closeBrackets = ['}', ']', ')']
    return True if brack in openBrackets else False

def bracketType(element):
    parenteses = ['(', ')']
    colchetes = ['[', ']']
    if element in parenteses:
        return 'parenteses'
    elif element in colchetes:
        return 'colchetes'
    else:
        return 'chaves'


print(BBC(bracketMaker()))