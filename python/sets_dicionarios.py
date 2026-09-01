#dictionary {}
# chave e valor, é possivel associar a forma de uma variavel a um valor, e esse valor pode ser de qualquer tipo, inclusive outro dicionario

#EXXEMPLO DE DICIONARIO
ex_dics = {
    "nome": "João",
    "idade": 19, 
    "cidade": "São Paulo",
    "atuação": "Programador(estudante de Ciencia da Computação)",
}

#Como atualizar ou acrescentar um valor no dicionario
ex_dics["idade"] = 20 #atualizando o valor da chave idade
ex_dics["estado"] = "SP" #adicionando uma nova chave e valor

print(ex_dics["atuação"])

for chave, valor in ex_dics.items():
    print(chave, valor)# sem f string pois a saida não precisa ser formatada, apenas exibida


#SETs {}
# Um set é uma coleção desordenada de elementos únicos, onde ele descarta automaticamente elementos duplicados. Ele não garante uma ordem especifica 

#exemplo de set
ex_set = {1, 1 , 2, 3, 9, 3, 4, 5}
print(ex_set) #saida: {1, 2, 3, 4, 5} - elementos duplicados foram descartados

sub_rotina = {
    "titulo": "estudar classes e objetos",
    "descricao": "estudar classes e objetos em python",
    "horario": "15:00",
    "materiais": ["livro", "notebook", "Alura"],
    "prioridade": "",
    "concluida": False
}

df_prioridade = {
    "1": "alta",
    "2": "media",
    "3": "baixa"
}

determinar_prioridade = input("Qual a prioridade da sub-rotina? (alta(1)/média(2)/baixa(3)): ").lower()
if determinar_prioridade in df_prioridade:
    sub_rotina["prioridade"] = df_prioridade[determinar_prioridade]
terminada = input("Você concluiu a sub-rotina? (sim/não): ").lower()
if terminada == "sim":
    sub_rotina["concluida"] = True

for chave, valor in sub_rotina.items():
    print(chave, valor)
