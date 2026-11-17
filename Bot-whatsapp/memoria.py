nome = input("Qual é o seu nome? ")
arquivo = open("usuarios.txt", "a")
arquivo.write(nome + "\n")
arquivo.close()
print("Nome salvo com sucesso!")


arquivo = open("usuarios.txt", "r")
nomes = arquivo.readlines()
arquivo.close()
print("\nUsuários cadastrados:")
for nome in nomes:
    print(nome.strip())

