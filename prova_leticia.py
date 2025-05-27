def salvar_respostas_em_txt(respostas):
    with open("respostas_quiz.txt", "w", encoding="utf-8") as arquivo:
        for i, resposta in enumerate(respostas, 1):
            arquivo.write(f"Pergunta {i}:\n")
            arquivo.write(f"  Sua resposta: {resposta['usuario']}\n")
            arquivo.write(f"  Resposta correta: {resposta['correta']}\n")
            arquivo.write(f"  Resultado: {'✅ Correto' if resposta['acertou'] else '❌ Errado'}\n\n")


def quiz():
    score = 0
    respostas_usuario = []

    perguntas = [
        {
            "texto": "1) O que será impresso pelo seguinte código?\n"
                     "x = 10\ny = 3\nprint(x // y)",
            "opcoes": ["a) 3", "b) 3.33", "c) 3.0", "d) 4"],
            "correta": "a"
        },
        {
            "texto": "2) Qual é o tipo da variável `resultado` após esta operação?\nresultado = 5 + 2.0",
            "opcoes": ["a) int", "b) float", "c) str", "d) complex"],
            "correta": "b"
        },
        {
            "texto": "3) Qual saída será exibida ao rodar o código abaixo?\n"
                     "def funcao(x=[]):\n    x.append(1)\n    return x\n"
                     "print(funcao())\nprint(funcao())",
            "opcoes": ["a) [1], [1]", "b) [1], [1, 1]", "c) [], []", "d) [1, 1], [1, 1, 1]"],
            "correta": "b"
        },
        {
            "texto": "4) Qual função embutida é usada para obter o tamanho de uma lista?",
            "opcoes": ["a) size()", "b) count()", "c) length()", "d) len()"],
            "correta": "d"
        },
        {
            "texto": "5) Qual código remove a chave `'idade'` com segurança (sem erro se não existir)?\n"
                     "dados = {'nome': 'Ana', 'idade': 28}",
            "opcoes": ["a) dados.pop('idade')", "b) del dados['idade']",
                       "c) dados.remove('idade')", "d) dados.pop('idade', None)"],
            "correta": "d"
        },
    ]

    for i, pergunta in enumerate(perguntas, 1):
        print(f"\n{pergunta['texto']}")
        for opcao in pergunta["opcoes"]:
            print(opcao)

        resposta = input("Sua resposta: ").strip().lower()
        acertou = resposta == pergunta["correta"]

        if acertou:
            print("✅ Correto!\n")
            score += 1
        else:
            print(f"❌ Errado. A resposta correta é {pergunta['correta']})\n")

        respostas_usuario.append({
            "usuario": resposta,
            "correta": pergunta["correta"],
            "acertou": acertou
        })

    print(f"✅ Você acertou {score} de {len(perguntas)} perguntas.")
    salvar_respostas_em_txt(respostas_usuario)
    print("📁 Respostas salvas em 'respostas_quiz.txt'.")


if __name__ == "__main__":
    quiz()
