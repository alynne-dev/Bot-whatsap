
# ==================================================
#             MEU CADERNO DE PYTHON
#                 PROJETO BOT-WHATSAPP
# ==================================================

# AULA 1 - PRIMEIROS PASSOS COM PYTHON
#
# print()
# Mostra uma mensagem na tela.
# Exemplo: print("Ola, mundo!")
#
# input()
# Recebe uma informacao digitada pelo usuario.
# Exemplo: nome = input("Digite seu nome: ")
#
# Variavel
# Guarda uma informacao.
# Exemplo: nome = "Maria"
#
# lower()
# Transforma letras em minusculas.
# Exemplo: mensagem.lower()
#
# if
# Executa um codigo se uma condicao for verdadeira.
#
# elif
# Verifica outra condicao.
#
# else
# Executa quando nenhuma condicao anterior e verdadeira.
#
# return
# Devolve um resultado de uma funcao.


# ==================================================
# AULA 2 - CRIANDO UM MENU
#
# def
# Cria uma funcao.
#
# Exemplo:
# def mostrar_menu():
#     print("1 - Opcao 1")
#
# while True
# Cria uma repeticao continua.
#
# break
# Interrompe uma repeticao.
#
# \n
# Faz uma quebra de linha dentro de um texto.
#
# Objetivo:
# Criar um menu com opcoes para o usuario.


# ==================================================
# AULA 3 - ORGANIZANDO O CODIGO COM FUNCOES
#
# Funcao:
# Permite organizar e reutilizar codigos.
#
# Exemplo:
# def responder_mensagem(mensagem):
#     return "Ola!"
#
# Parametro:
# E a informacao recebida pela funcao.
#
# Argumento:
# E o valor enviado para a funcao.
#
# Exemplo:
# nome = input("Digite seu nome: ")
# print("Ola,", nome)
#
# Objetivo:
# Deixar o codigo mais organizado e reutilizavel.


# ==================================================
# AULA 4 - SALVANDO INFORMACOES EM ARQUIVOS
#
# open()
# Abre um arquivo.
#
# "a"
# Abre o arquivo para adicionar informacoes
# sem apagar o conteudo anterior.
#
# "w"
# Abre para escrever, apagando o conteudo anterior.
#
# "r"
# Abre para leitura.
#
# write()
# Escreve informacoes no arquivo.
#
# with open()
# Abre e fecha o arquivo automaticamente.
#
# Exemplo:
#
# with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
#     arquivo.write("Maria\n")
#
# Objetivo:
# Guardar os nomes dos usuarios cadastrados.


# ==================================================
# AULA 5 - LENDO INFORMACOES DOS ARQUIVOS
#
# read()
# Le todo o conteudo do arquivo.
#
# readline()
# Le uma linha do arquivo.
#
# readlines()
# Le todas as linhas e guarda em uma lista.
#
# Exemplo:
#
# with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
#     usuarios = arquivo.readlines()
#
# for
# Percorre os elementos de uma lista.
#
# strip()
# Remove espacos e quebras de linha das extremidades.
#
# Objetivo:
# Conseguir consultar os usuarios salvos.


# ==================================================
# AULA 6 - RECONHECENDO USUARIOS
#
# try
# Tenta executar um codigo.
#
# except
# Trata um erro caso aconteca.
#
# FileNotFoundError
# Erro que acontece quando o arquivo nao existe.
#
# lower()
# Transforma letras em minusculas.
# Ajuda a comparar nomes sem diferenciar maiusculas.
#
# return True
# Retorna verdadeiro.
#
# return False
# Retorna falso.
#
# Objetivo:
# Verificar se um usuario ja esta cadastrado.
#
# Funcao que estamos desenvolvendo:
#
# def buscar_usuario(nome):
#     try:
#         with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
#             usuarios = arquivo.readlines()
#
#             for usuario in usuarios:
#                 if usuario.strip().lower() == nome.lower():
#                     return True
#
#             return False
#
#     except FileNotFoundError:
#         return False

# OBJETIVO:
# Verificar se um usuario ja esta cadastrado.

# 1. def
# Cria uma funcao.
#
# Exemplo:
# def buscar_usuario(nome):

# 2. try
# Tenta executar um codigo.
# Ajuda a evitar que um erro interrompa o programa.

# 3. with open()
# Abre um arquivo e fecha automaticamente.

# 4. "r"
# Abre um arquivo somente para leitura.

# 5. encoding="utf-8"
# Permite trabalhar corretamente com acentos.

# 6. readlines()
# Le todas as linhas do arquivo e guarda em uma lista.

# 7. for
# Percorre os elementos de uma lista.

# 8. strip()
# Remove espacos e quebras de linha das extremidades.

# 9. lower()
# Transforma letras em minusculas.

# 10. if
# Verifica se uma condicao e verdadeira.

# 11. return True
# Retorna verdadeiro.
# Significa que encontrou o usuario.

# 12. return False
# Retorna falso.
# Significa que nao encontrou o usuario.

# 13. except FileNotFoundError
# Trata o erro quando o arquivo nao existe.


# EXEMPLO PRATICO:
#
# buscar_usuario("Maria")
# Resultado: True
#
# buscar_usuario("JoaoTeste123")
# Resultado: False


# O QUE APRENDI:
# O Python consegue procurar nomes dentro
# de um arquivo e identificar se ja existem.
#
# ==================================================
# FIM DA AULA 6
# ==================================================


# ==================================================
# DICAS IMPORTANTES
#
# Ctrl + S = Salvar arquivo.
#
# Ctrl + C = Interromper execucao no terminal.
#
# Ctrl + Z = Desfazer.
#
# Ctrl + Shift + P = Abrir paleta de comandos do VS Code.
#
# py bot.py = Executar o arquivo principal no Windows.
#
# LEMBRETE:
# Sempre tente entender o codigo antes de copiar.
# Errar faz parte do aprendizado!
#
# ==========================================
# AULA 7 - CADASTRO DE USUÁRIOS (EM ANDAMENTO)
# ==========================================

# Também criamos no cadastro.py uma função para adicionar um nome
# ao final do arquivo usuarios.txt.

# def cadastrar_usuario(nome):
#     with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
#         arquivo.write(nome + "\n")

# O modo "a" adiciona o nome ao final do arquivo sem apagar os anteriores.
# A expressão nome + "\n" escreve o nome e depois pula para outra linha.

# Testamos o cadastro de "CarlosTeste" e depois usamos buscar_usuario()
# para confirmar que a função retornava True.


# ------------------------------------------
# AULA 7 - EVITANDO CADASTROS DUPLICADOS
# ------------------------------------------

# Estamos aprendendo a verificar se o nome já existe antes de gravar.
#
# if buscar_usuario(nome):
#     print("Usuario ja cadastrado!")
#     return
#
# Explicação:
# - buscar_usuario(nome) retorna True se o nome já estiver no arquivo.
# - if executa o bloco quando a condição é verdadeira.
# - print() mostra o aviso no terminal.
# - return encerra a função naquele ponto.
# - Assim, se o usuário já existe, a função para e não grava outra cópia.
#
# Próximo passo da aula:
# adicionar um else para cadastrar o nome somente quando ele ainda não existir.
#
# Estrutura que estamos construindo:
#
# def cadastrar_usuario(nome):
#     if buscar_usuario(nome):
#         print("Usuario ja cadastrado!")
#         return
#
#     # Na próxima etapa, vamos adicionar aqui a parte que grava
#     # o usuário quando ele ainda não estiver cadastrado.
#  A funcao cadastrar_usuario agora verifica se o nome existe antes de gravar.
# Se buscar_usuario(nome) retornar True, avisa e usa return para sair.
# Caso contrario, else grava o nome com modo "a" e mostra uma confirmacao.
#
# Estrutura atual (no cadastro.py):
# def cadastrar_usuario(nome):
#     if buscar_usuario(nome):
#         print("Usuario ja cadastrado!")
#         return
#     else:
#         with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
#             arquivo.write(nome + "\\n")
#         print("Usuario cadastrado com sucesso!")

# ==========================================
# AULA 8 - LISTAR USUARIOS
# ==========================================
# readlines() le todas as linhas do arquivo.
# Criamos uma lista vazia e usamos append() para adicionar cada nome,
# removendo a quebra de linha com strip().
# A funcao listar_usuarios() devolve a lista com return.
# Se usuarios.txt nao existir, devolve uma lista vazia: return [].
#
# Estrutura atual (no cadastro.py):
# def listar_usuarios():
#     try:
#         with open("usuarios.txt", "r", encoding="utf-8") as arquivo:
#             usuarios = arquivo.readlines()
#             lista = []
#             for usuario in usuarios:
#                 lista.append(usuario.strip())
#             return lista
#     except FileNotFoundError:
#         return []

# ==========================================
# AULA 9 - RETURN, LISTAS E CONTAGEM (CONCLUIDA)
# ==========================================
# print() exibe informacao no terminal; return devolve um valor.
# lista = [] cria uma lista vazia.
# append() adiciona um elemento na lista.
# len(lista) conta quantos elementos existem na lista.
# Podemos reutilizar uma funcao dentro de outra.
#
# Funcao criada no cadastro.py para contar usuarios:
# def quantidade_usuarios():
#     usuarios = listar_usuarios()
#     return len(usuarios)
#
# listar_usuarios() recupera os nomes; len() conta os nomes;
# quantidade_usuarios() devolve o total.
#
# Testes no terminal (na pasta do projeto):
# py -c "from cadastro import listar_usuarios; print(listar_usuarios())"
# py -c "from cadastro import quantidade_usuarios; print(quantidade_usuarios())"
# ==========================================
# DICAS IMPORTANTES
# ==========================================

# 1. A indentação (espaços no começo da linha) é importante em Python.
# 2. Texto deve ficar entre aspas.
# 3. = atribui um valor; == compara dois valores.
# 4. Uma função só executa quando é chamada.
# 5. Teste pequenas partes do código para encontrar erros mais facilmente.

# ==================================================
# FIM DO CADERNO DE ESTUDOS
# ==================================================

