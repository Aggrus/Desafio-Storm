# Questão 2 do desafio Fullstack da Storm
# Nome do aplicante: Gustavo Zalcman

def somaNivel(Array):
    left = list()
    right = [None]*len(Array)
    total = 0

    for i in range(len(Array)):        
        if i == 0:
            left.append(Array[0])
            right[-1] = Array[-1]
        else:
            left.append(max(left[i-1], Array[i]))
            right[-(i+1)] =  max(right[-i], Array[-(i+1)])
    for i in range(len(Array)):
        total += min(left[i], right[i]) - Array[i]
    return total

def main():
    l1 = [2,1,1,1,2,1,0,1]
    l2 = [0,1,0,2,1,0,1,3,2,1,2,1]
    l3 = [3,2,1,1,0,1,2,3,4,0,1]
    soma1 = somaNivel(l1)
    soma2 = somaNivel(l2)
    soma3 = somaNivel(l3)
    print("Soma 1: %d\nSoma 2: %d\nSoma 3: %d\n\n"%(soma1,soma2,soma3))

main()