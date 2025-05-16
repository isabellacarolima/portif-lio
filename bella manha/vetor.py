MATRIZ = [[0] * 4 for _ in range (4)]
MATRIZ[0][0] = input()
MATRIZ[0][1] = input()
MATRIZ[0][2] = input()
MATRIZ[0][3] = input()
MATRIZ[1][0] = input()
MATRIZ[1][1] = input()
MATRIZ[1][2] = input()
MATRIZ[1][3] = input()
for contador1 in range(4):
    for contador2 in range(4):
        print(MATRIZ[contador1][contador2], end=" ")
    
    print()
