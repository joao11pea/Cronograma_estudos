# usar * na variavel significa que ela pode receber qualquer 
# quantidade de argumentos e agrupa eles em uma tupla
#exemplo de função com *args
def somar (*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

print(somar(1, 2, 3, 4, 5))


# usar ** na variavel significa que ela pode receber qualquer 
# quantidade de argumentos nomeados e agrupa eles em um dicionario

#exemplo de função com **kwargs
def info_usuario(**dados):
    print(dados)

info_usuario(nome="João", idade=19, cidade="São Paulo")


def criar_tarefa(titulo, horario, materiais):
    return {"titulo": titulo, "horario": horario, "materiais": materiais}

tarefa = criar_tarefa(titulo="Estudar POO", horario= "17:00", materiais=["Carreira backend Alura", "Tutor Claude"])


print (tarefa)





