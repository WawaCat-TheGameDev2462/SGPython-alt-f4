idade = int(input("qual sua idade: "))
tem_aura = input("voce tem experiencia: (sim/nao)")
antecedentes_criminosos = input("voce tem antecedentes criminosos: (sim/nao)")
foi_indicado_ou_ensino_completo = input("voce foi indicado por alguem que lhe conhece: (sim/nao)")
if idade >= 18 and tem_aura == "sim" and antecedentes_criminosos == "nao":
    print("okay, vamos lhe entrevistar amanha")
if idade >= 18 and foi_indicado_ou_ensino_completo == "sim" and tem_aura == "nao" and antecedentes_criminosos == "nao":
    print("ok, se voce tem um pouco de ensino, vamos lhe entrevistar amanha")
else:
    print("nao podemos aceitar voce, pedimos desculpa")
 
