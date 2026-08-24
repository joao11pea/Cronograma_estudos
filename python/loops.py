import random 

#FOR E WHILE
#BREAK E CONTINUE
#RANGE

#TABUADA
n_usuario = input("Digite um numero para ver sua taboada: ")
n_escolhido = int(n_usuario)


for de1_a_10 in range(1,11):
    tabuada = n_escolhido * de1_a_10
    print(f"{n_escolhido}x {de1_a_10}= {tabuada}") 



#JOGO DA ADIVINHAÇÃO 

numero_secreto = random.randint(1, 10)
chute_usuario = int(input("Tente acertar o numero que estou pensando:"))
distancia = numero_secreto - chute_usuario
while True:
    if abs(distancia) >=6:
        print("Esse chute passou longe")
    elif abs(distancia) >=3: 
        print("Voce esta chegando perto")
    elif abs(distancia) >=1:
        print("Voce esta muito perto")
    else:
        print("Parabens voce leu minha mente")
        break
    chute_usuario = int(input("Tente acertar o numero que estou pensando:"))
    distancia = numero_secreto - chute_usuario



