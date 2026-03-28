import time
numeroLegal = int(input("vamos contar ate quanto? "))
contador = 0
while contador < numeroLegal:
  contador += 1
  #contador = valor atual do contador + 1
  print(contador)
  time.sleep(1)

  #SE LEMBRE DE USAR import time PRA PODER USAR time.sleep(numero de segundos)
