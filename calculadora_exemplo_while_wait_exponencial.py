import time
import math

numeroLegal = int(input("vamos contar ate quanto? "))
contador = 0
tempo = 1.1
while contador < numeroLegal:
  contador += 1
  #contador = valor atual do contador + 1
  print(contador)
  time.sleep(tempo)
  tempo = tempo * math.exp(-0.05 * 2) #o -0.05 faz o numero diminiur, se fosse positivo o intervalo iria aumentar

  #SE LEMBRE DE USAR import time PRA PODER USAR time.sleep(numero de segundos)
