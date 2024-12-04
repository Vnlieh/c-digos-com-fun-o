def calculadora():

   resposta = input("Qual operação voce deseja realizar?")
   if resposta == "soma":
      x = int (input("Digite o primeiro número:"))
      y = int (input("Digite o segundo número:"))
      resultadoSOM = x + y
      print(f"{x} + {y} = {resultadoSOM}")
   elif resposta == "subtração":
      x = int (input("Digite o primeiro número:")) 
      y = int (input("Digite o segundo número:"))
      resultadoSUB = x - y
      print(f"{x} - {y} = {resultadoSUB}")
   elif resposta == "multiplicação":
      x = int (input("Digite o primeiro número:")) 
      y = int (input("Digite o segundo número:"))
      resultadoMUL = x * y
      print(f"{x} * {y} = {resultadoMUL}")
   elif resposta == "divisão":
      x = int (input("Digite o primeiro número:")) 
      y = int (input("Digite o segundo número:"))
      resutadoDIV = x / y
      print(f"{x} / {y} = {resutadoDIV}") 
   else:
      print("Operação não encontrada. Tente novamente")

calculadora()