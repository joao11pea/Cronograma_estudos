#n = 10 

#print(float(n))


#n1 = 10 
#str = str(n1)
#print(type(str))


#EXERCICIO 


operacao_usuario = input("escolha uma das operações +, -, x, / :")
n = input ("digite o primeiro número: ")
n2 = input("o segundo número: ")
resultado = ""
if  operacao_usuario == "+" :
    resultado = float(n) + float(n2) 
elif  operacao_usuario == "-" : 
    resultado = float(n) - float(n2) 
elif operacao_usuario == "x" :
    resultado =float(n) * float(n2) 
else :
    resultado = float(n) / float(n2) 

print(resultado)

