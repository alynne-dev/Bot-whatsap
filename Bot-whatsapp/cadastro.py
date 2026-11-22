def buscar_usuario(nome):
    try:
        with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
            usuarios = arquivo.readlines()
            for usuario in usuarios:
                if usuario.strip().lower() == nome.lower():
                    return True
            return False
    except FileNotFoundError:
        return False
    
def cadastrar_usuario(nome):
    if buscar_usuario(nome):
        print("Usuário já cadastrado.")
        return
    else:
        print("Cadastrando usuário...")
        with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(nome + "\n")

def listar_usuarios():
    try:
       with open("usuarios.txt","r", encoding="utf-8") as arquivo:
        usuarios = arquivo.readlines()
        lista = []
        for usuario in usuarios:
            lista.append(usuario.strip())
            return lista
 
    except FileNotFoundError:
        return[]
    
def quantidade_usuarios():
    usuarios = listar_usuarios()
    return len(usuarios)
