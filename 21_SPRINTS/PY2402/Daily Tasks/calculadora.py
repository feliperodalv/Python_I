# Calculadora com as funções soma, sobtração divisão e multiplicação

val1,operacao,val2=input('operação:').split()

print(val1,operacao,val2)

val1=int(val1)

val2 = int(val2)

resultado=[]

if operacao == '+':
  resultado = val1+val2

elif operacao == '-':
  resultado = val1-val2

elif operacao == '*' or operacao=='x':
  resultado = val1*val2

elif operacao == '/':
  resultado = val1 / val2



print(resultado)

