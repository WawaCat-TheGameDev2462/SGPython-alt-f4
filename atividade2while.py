import random

numero_maximo = int(input("qual o numero maximo que voce adivinharahra? "))
while numero_maximo <=1:
  print("é pra escolher um numero maior que 1")
  numero_maximo = int(input("qual o numero maximo que voce adivinharahra? "))
#serve pra nao deixar a pessoa escolher um numero negativo

chances=int(input("quantas chances vc quer ter? "))
while chances <1 :
    print("é pra escolher um numero maior que 1")
    chances=int(input("quantas chances vc quer ter? "))
#serve pra nao deixar a pessoa escolher um numero negativo

resposta = random.randint(1,numero_maximo) 

numero_escolhido = -1

while numero_escolhido != resposta and chances != 0:
  numero_escolhido = int(input("adivinhe o numero secreto (adivinhe de 1 a "  + str(numero_maximo) + ": " ))
  if numero_escolhido == resposta:
    chances += 1
  elif numero_escolhido > numero_maximo or numero_escolhido <1:
    print("É PRA ADIVINHAR UM NUMERO DE 1 A "  + str(numero_maximo))
  elif numero_escolhido < resposta :
    print("voce errou, tente um numero maior")
  elif numero_escolhido > resposta:
    print("voce errou, tente um numero menor")
  else:
    print("erro, delete o arquvio System32 (nao faca isso)")

  chances -= 1
  print("chances restantes: " + str(chances))

if chances != 0:
    print("voce ganhou")
else: 
   print("voce perdeu seu cara de bacalhau cozido com alface e azeite")