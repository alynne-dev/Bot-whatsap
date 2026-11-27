perguntas = [
    {
        "pergunta": "Qual função mostra uma mensagem na tela?",
        "opcoes": ["input()", "print()", "return", "len()"],
        "resposta": "2",
    },
    {
        "pergunta": "Qual modo do open() adiciona texto sem apagar o arquivo?",
        "opcoes": ['"r"', '"w"', '"a"', '"x"'],
        "resposta": "3",
    },
    {
        "pergunta": "Qual função cria uma nova função?",
        "opcoes": ["def()", "len()", "print()", "while()"],
        "resposta": "1"
    }
]

def fazer_quiz():
    acertos = 0
    for item in perguntas:
        print("\n" + item["pergunta"])
        for numero, opcao in enumerate(item["opcoes"], start=1):
            print(str(numero) + ") " + opcao)
        resposta = input("Sua resposta: ")
        if resposta == item["resposta"]:
            print("Acertou! ✅")
            acertos += 1
        else:
            print("Errou ❌")
    return "Você acertou " + str(acertos) + " de " + str(len(perguntas))