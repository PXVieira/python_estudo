# Gerador de CPF:
from random import randint

n_dg = ""
for i in range(9):
    dg = randint(0, 9)
    n_dg += str(dg)
print(n_dg)  # número gerado

n_dg
mult = 10
soma = 0
for dgts in n_dg:
    multiplicando = int(dgts) * mult
    soma += multiplicando
    mult -= 1

pri_dgt = soma * 10 % 11
pri_dgt if pri_dgt <= 9 else 0

dez_dgt = str(n_dg) + str(pri_dgt)

mult = 11
soma = 0
for dgts in dez_dgt:
    multiplicando = int(dgts) * mult
    soma += multiplicando
    mult -= 1

seg_dgt = soma * 10 % 11
seg_dgt if seg_dgt <= 9 else 0

dgts = str(pri_dgt) + str(seg_dgt)
comparador = n_dg

cpf = n_dg + dgts

print("Esse é o numero final do CPF gerado:", cpf)
# pode ser conferido aqui: https://www.4devs.com.br/validador_cpf
