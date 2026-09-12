"""
.upper() deixa a strig toda em maiuscula
.lower() deixa a strig toda minuscula 
.split() quebra a string em pedaços, transformando em uma lista, com o separador padrão sendo espaço
.strip() retira os espaços(ou quebra de linhas) em  brancos no inicio e no final da string
"".join() junta os items de uma lista em uma unica string, ela funciona de maneira contraria as outra, deve-se primeiro passar o separador(entre ""), e dentro do () passar a lista
"""

#exemplo de splip
frutas = "maçã,banana,uva"
print(frutas.split(","))

#exemplo de strip
nome = "   joão   "
print(nome.strip())

#limpa somente os espaços do inicio e final da string, a identação é mantida
animais = """   cachorro,
        gato,
        papagaio
"""
print(animais.strip())

#exemplo upper
print("minusculo".upper())

#exemplo lower
print("MAIUSCULO".lower())


#list comprehensions, é um metodo para reduzir funciona com a seguinte sintaxe: [EXPRESSAO for VARIAVEL in SEQUENCIA if CONDICAO], podendo ser ou não com if(condição)
#exemplo de coprehensions com condição
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
pares = [n for n in numeros if n % 2 == 0] #passa para a lista apenas numeros pares 
print(pares)

#exemplo de comprehensions sem if 
dobrados = [n * 2 for n in numeros]
print(dobrados)



#exercicio
tarefas = ["Estudar POO", " ler livros   ", "Estudar C", "Fazer 40 barras"]
estudos_do_dia = [item.strip().upper() for item in tarefas ]
filtro_estudos = [item for item in estudos_do_dia if "Estudar".upper() in item   ]
print(estudos_do_dia)
print(filtro_estudos)

