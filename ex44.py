print('{:=^40}'.format(' Desconto de Loja '))
v = float(input('Qual o valor? R$'))
print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou ma''')
p = int(input('Qual a forma de pagament? '))
if p == 1 :
    t = v-(v*10/100)
elif p == 2:
    t = v - (v*5/100)
elif p == 3:
    t = v
    vp = t / 2
    print('Sua compra será parcelade em 2X sem juros de {}R$'.format(vp))

elif p == 4:
    parcelas = int(input('Quantas parcelas?'))
    t = v + (v*20/100)
    vp = t/parcelas
    print('Sua compra sera parcelada em {}x de R${:.2f} com juros'.format(parcelas,vp))
else:
    t = 0
    print('Opção invalida, tente novamente!')
print('Sua compra é de R${:.2f} vai custar R${:.2f} no final.'.format(v,t))


