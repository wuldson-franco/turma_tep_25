from fpdf import FPDF
import datetime

# === Função para gerar relatório em PDF ===
def gerar_pdf(respostas, aluno_nome, matricula):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    titulo = f"Relatório de Respostas - {aluno_nome} ({matricula})"
    pdf.cell(200, 10, txt=titulo, ln=True, align='C')
    pdf.ln(10)

    for i, resposta in enumerate(respostas, 1):
        pdf.cell(200, 10, txt=f"Pergunta {i}:", ln=True)
        pdf.cell(200, 10, txt=f"  Sua resposta: {resposta['usuario']}", ln=True)
        pdf.cell(200, 10, txt=f"  Resposta correta: {resposta['correta']}", ln=True)
        resultado = 'Correto' if resposta['acertou'] else 'Errado'
        pdf.cell(200, 10, txt=f"  Resultado: {resultado}", ln=True)
        pdf.ln(5)

    data_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo = f"respostas_{matricula}_{data_hora}.pdf"
    pdf.output(nome_arquivo)
    print(f"\n📄 Relatório em PDF salvo como '{nome_arquivo}'.")

# === Função principal do quiz ===
 quiz():
    print("🧑‍🎓 Bem-vindo ao Quiz de Python!")
    aluno_nome = input("Digite seu nome completo: ").strip()
    matricula = input("Digite sua matrícula: ").strip()
    print("\nIniciando o questionário...\n")

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
            "texto": "3) Qual é a principal função do Git?\n",
            "opcoes": ["a) Gerenciamento de projetos ", "b) Controle de versão", 
                       "c) Desenvolvimento de aplicativos móveis", "d) Subir os códigos para deixar organizado", "e) Criação de repositório e compartilhamento de códigos"],
            "correta": "b"
        },
        {
            "texto": "4) Qual função embutida é usada para obter o tamanho de uma lista?",
            "opcoes": ["a) size()", "b) count()", "c) length()", "d) len()"],
            "correta": "d"
        },
        {
            "texto": "5) Qual é o comando utilizado para fazer o upload de um arquivo para o GitHub?\n",
            "opcoes": ["a) git push -u origin “nome da branch”", "b) git add",
                       "c) git commit -m “<descrição>”", "d) git clone", "e) git pull origin"],
            "correta": "a"
        },
    ]

    for i, pergunta in enumerate(perguntas, 1):
        print(f"\n{pergunta['texto']}")
        for opcao in pergunta["opcoes"]:
            print(opcao)

        resposta = input("Sua resposta: ").strip().lower()
        acertou = resposta == pergunta["correta"]

        if acertou:
            print("Correto!\n")
            score += 1
        else:
            print("Errado. A resposta correta é {pergunta['correta']})\n")

        respostas_usuario.append({
            "usuario": resposta,
            "correta": pergunta["correta"],
            "acertou": acertou
        })

    prin(f"\nVocê acertou {score} de {len(perguntas)} perguntas.")
    gerar_pdf(respostas_usuario, aluno_nome, matricula)


if __name__ == "__main__":
    quiz()
