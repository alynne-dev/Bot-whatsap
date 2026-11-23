from cadastro import listar_usuarios, quantidade_usuarios, cadastrar_usuario

print("🤖 Olá! Sou o seu bot de Estudos")
nome = input("Qual é o seu nome? ")
print("Prazer em conhecer você, " + nome + "!")

def mostrar_menu():
    print("\n==== Menu do Bot ====")
    print("1. Sobre o projeto")
    print("2. Aprender python")
    print("3. Ajuda")
    print("4. Sair")
    print("5. Quantidade de usuarios cadastrados")
    print("6. Cadastrar novo usuario")


def responder_mensagem(opção):
    
    if opção == "1":
        return "Este projeto é um bot de WhatsApp simples que responde a mensagens de acordo com as opções escolhidas pelo usuário."
    elif opção == "2":
        return "Python é uma linguagem de programação poderosa e fácil de aprender. Você pode começar com os fundamentos e ir avançando conforme sua experiência."
    elif opção == "3":
        return "Para obter ajuda, você pode consultar a documentação oficial do Python ou procurar por tutoriais online."
    elif opção == "4":
        return "Até logo! Se precisar de mais alguma coisa, é só chamar."
    elif opção == "5":
        return "Total de usuarios cadastrados: " + str(quantidade_usuarios())
    elif opção == "6":
        novo_usuario = input("Digite o nome do novo usuario: ")
        cadastrar_usuario(novo_usuario)
        return "Cadastro finalizado!"
    else:
        return "Desculpe, não entendi sua mensagem. Por favor, digite 'menu' para ver as opções disponíveis."

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")
    resposta = responder_mensagem(escolha)

    print("\nBot: " + resposta)
    if escolha == "4":
        break
                                  


