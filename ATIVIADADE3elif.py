idade = int(input("digite sua idade: "))
cartao_vip = input("voce tem cartao vip? (sim/nao): ") 
ingresso = input("voce tem ingresso? (sim/nao): ")
if idade <= 18:
    autorizacao_dos_pais = input("voce tem autorizacao dos pais? (sim/nao): ")

if idade >= 18 and (ingresso == "sim" or cartao_vip == "sim"):
    print("pode entrar e seja bem vindo")
elif idade <12:
    print("peco desculpas mas voce nao pode entrar")
elif idade <18 and autorizacao_dos_pais == "sim" and (ingresso == "sim"  or cartao_vip == "sim"):
    print("pode entrar, meu jovem")
else:
    print("nem tente pular o muro seu babaca")
