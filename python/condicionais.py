nota_usuario = input("digite sua nota: ")
nota = float(nota_usuario)

if nota >= 7 and nota <=10 :
    print("Parabens, você foi aprovado(a)")
elif nota >= 5 :
    print("Você esta de recuperação")
else:
     print("Você esta reprovado")