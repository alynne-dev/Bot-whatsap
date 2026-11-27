def salvar_pontuacao(nome, acertos, total):
    with open("pontuacoes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(nome + ";" + str(acertos) + ";" + str(total) + "\n")