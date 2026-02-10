nota1 = int(input("digite sua nota1: "))
nota2 = int(input("digite sua nota2: "))
nota3 = int(input("digite sua nota3: "))
media = nota1 /3 + nota2 /3 + nota3  /3
print(media)

if media <5:
    print("reprovado")

elif media <9.9:
    print("aprovado")

else:
    print("nota perfeita")
