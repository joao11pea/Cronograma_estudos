perguntas =[
    "para atribuir numero deve se usar aspas?",
    "gitignore serve para salvar aquivos ?",
    "git init trasforma a pasta em um repositorio git?",
    "gh repo create ... --public --source=. --remote=oringin --push, cria um repositorio e ja configura ele ?"
]

respostas =[
    "Não",
    "Não",
    "Sim",
    "Sim"
]
total_acerto = int()
for i in range(len(perguntas)):
    print(perguntas[i])
    resposta_usuario = input("responda com Sim ou Não:")
    if  resposta_usuario == respostas[i]:
        total_acerto = total_acerto + 1

print(f"Parabens voce acertou {total_acerto}")