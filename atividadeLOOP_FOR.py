listaalunisimos = ["han diesel", "miguel", "heitor", "pedro", "gabriel"]
print(listaalunisimos [0],listaalunisimos [1],listaalunisimos [2],listaalunisimos [3], listaalunisimos [4])
index_escolhido = int(input("qual aluno voce quer saber mais sobre?   (escolha o index de 0 a 4)"))
if index_escolhido == 0:
    print(listaalunisimos [0]+ ",", "ele gosta de beber diesel porque seu nome é han diesel")
elif index_escolhido == 1:
    print(listaalunisimos [1]+ ",", "é uma pessoa muito legal")
elif index_escolhido == 2:
    print(listaalunisimos [2]+ ",", "é uma pessoa que é muito boa em fazer piadas eu acho😂 ✌ 🗣 🔥")
elif index_escolhido == 3:
    print(listaalunisimos  [3]  + ",", "sou eu, sou um otimo progamador tipo nao escrevo isto com zoom a 1300" )
elif index_escolhido == 4:
    print(listaalunisimos [4] + ",", "é o melhor professor de todos, na studiogames do iguatemi, se voce quiser estudar com ele, estara desponivel tanto no curso SG Coder Kids e SG Python")
else:
    print("erro tente novamente um numero de 0 a 4")    