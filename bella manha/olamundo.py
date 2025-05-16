def saudacao (nomeUsuario) :
    print(f"Olá {nomeUsuario}")
print("Digite o seu nome: ")
nome = input()
saudacao(nome)
def verificaSexo (sexo):
    if sexo == "f" :
        print ("Femino")
    else:
        print("Masculino")
print("Digite o seu sexo: (f) para femino e (m) para masculino")
sexo = input()
verificaSexo(sexo)
