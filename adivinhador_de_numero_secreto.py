numero_escolhido = int(input("qual o numero secreto? (escolha de 1 a 10): "))
#escolhe o numero secreto

while numero_escolhido >10 or numero_escolhido <1:
  print("é pra escolher um numero de 1 a 10")
  numero_escolhido = int(input("qual o numero secreto? (escolha de 1 a 10): "))
#serve pra nao deixar a pessoa escolher um numero acima de 10 ou menor que 1 ou maior que 10

contador = 1
while contador <100:
  print("passe pro seu amigo agora")
  contador += 1
#serve pra que o numero escolhido nao seja visto

numero_adivinhado = 67 #inicializando numero_adivinhado diferente de numero_escolhido

while numero_escolhido != numero_adivinhado:
  numero_adivinhado = (int(input("adivinhe o numero secreto (adivinhe de 1 a 10): ")))
  if numero_adivinhado == numero_escolhido:
    print("voce acertou")
  elif numero_adivinhado >10 or numero_adivinhado <1:
    print("É PRA ADIVINHAR UM NUMERO DE 1 A 10")
  elif numero_adivinhado <numero_escolhido:
    print("voce errou, tente um numero maior")
  else:
    print("voce errou, tente um numero menor")
