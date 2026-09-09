#EXERCIO DE TREINO DE BRANCHS -- AGENDA

agenda = []
def novo_contato(nome, telefone): 
    agenda.append({"nome": nome, "telefone": telefone})

while True:
    novo_contato(nome=input("Digite o nome do novo contato:"), telefone=(input("Digite o telefone aqui:")))

    print(
        f"""Novo contato salvo:
        Nome:{agenda[-1]["nome"]}, numero :{agenda[-1]["telefone"]}""")
    print(f"Sua lista de contatos:")
    for i in range(len(agenda)):
        print(f"{agenda[i]["nome"]} = {agenda[i]["telefone"]}")
    continuar = input("Deseja adicionar um novo contato: (sim) ou (não)? ")
    if continuar == "não":
        break
    else:
        continue
            