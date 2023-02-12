

print('..................vamos calcular sua media do ENEM..................')
# var nome da faculdade
nome = str(input('nome da instituição :'))

ling = float(input('Nota em linguagens :'))
mat = float(input('Nota em matematica :'))
cieh = float(input('Nota em ciencias humanas :'))
natu = float(input('Nota em natureza :'))
reda = float(input('Nota na redação :'))
print ('............pesos............')
# vars valor dos pesos
ling_p = float(input('Pesos em linguagens :'))
mat_p = float(input('Pesos em matematica :'))
cieh_p = float(input('Pesos em ciencias humanas :'))
natu_p = float(input('Pesos em natureza :'))
reda_p = float(input('peso da redação :'))
# calculo das notas
  # multiplicação
resu_ling = ling * ling_p #linguagens
resu_mat = mat_p * mat #matematica
resu_cin_h = cieh_p * cieh #ciencias humanas
resu_natu = natu_p * natu #natureza
resu_reda = reda_p * reda #redação
# soma dos pesos

soma_pesos = ling_p + mat_p + cieh_p + natu_p + reda_p
# soma das multiplicaçôes das notas
soma_notas = resu_ling + resu_mat + resu_cin_h + resu_natu + resu_reda
# divisão notas por pesos
final = soma_notas / soma_pesos
print(f'sua media final na instituição ( {nome} )  é de {final}')
