# Criando matriz 4x4 vazia
matriz = [[0] * 4 for _ in range(4)]

# Preenchendo a matriz com entradas do usuário
print("Digite os valores da matriz 4x4:")
for i in range(4):
    for j in range(4):
        matriz[i][j] = int(input(f"Elemento [{i}][{j}]: "))

# Exibindo a matriz
print("\nMatriz digitada:")
for linha in matriz:
    print(*linha)
