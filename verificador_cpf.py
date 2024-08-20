# Aula de hoje, criar um verificador de CPF...
# lógica https://atitudereflexiva.wordpress.com/2021/05/05/entenda-como-e-gerado-o-numero-do-cpf/
# 333.466.900-91 (https://www.4devs.com.br/gerador_de_cpf)
from rich import print

"333.466.900-91"
cpf_gerado = "333.466.900-91".replace(".", "").replace(
    "-", ""
)  # removendo os caracteres especiais ( '.' e '-' ) # cpf gerado, usando o link acima (obs, converter para str caso esteja em float ou int)
nove_dgt = cpf_gerado[:9]  # pegando os primeiros 9 digitos ( [0:9] )
mult = 10  # primeiro multiplicador (inicia com 10 vai até 2... ordem decrescente)
soma = 0
for dgts in nove_dgt:
    multiplicando = (
        int(dgts) * mult
    )  # convertendo os digitos em int e multiplicando os 9 digitos
    soma += multiplicando
    mult -= 1

pri_dgt = soma * 10 % 11  # resto da conta
# definição final do primeiro digito (se o valor for menor ou igual a 9, então o primeiro digito recebe o valor, caso contrario é 0)
pri_dgt if pri_dgt <= 9 else 0

# print(pri_dgt)  # == 9

dez_dgt = str(nove_dgt) + str(
    pri_dgt
)  # conventendo em str e concatenando o primeiro digito com os 9 digitos

# print(dez_dgt) # == '3334669009'
mult = 11  # segundo multiplicador (inicia com 11 vai até 2... ordem decrescente)
soma = 0
for dgts in dez_dgt:
    multiplicando = (
        int(dgts) * mult
    )  # convertendo os digitos em int e multiplicando os 10 digitos
    soma += multiplicando
    mult -= 1

seg_dgt = soma * 10 % 11  # resto da conta
# definição final do segundo digito (se o valor for menor ou igual a 9, então o segundo digito recebe o valor, caso contrario é 0)
seg_dgt if seg_dgt <= 9 else 0

# print(seg_dgt) # == 1

# concatenando os digitos e verificando com o cpf informado:
dgts = str(pri_dgt) + str(seg_dgt)
comparador = cpf_gerado[9:]

cpf = nove_dgt + dgts  # concatenando os 9 digitos com os 2 digitos do calculo

print("Esse é o numero final do CPF:", cpf)

if dgts == comparador:
    print("CPF [green]Válido[/]")
else:
    print("CPF [red]Inválido[/]")
