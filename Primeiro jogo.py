from random import choice
from time import sleep
print('=' * 23)
print('  PEDRA-PAPEL-TESOURA  ')
print('=' * 23)
indice1 = str('pedra')
indice2 = str('papel')
indice3 = str('tesoura')
lista = [indice1, indice2, indice3]
sorteio = choice(lista)
escolha = str(input('pedra papel tesoura: ')).strip()
print('Processando...')
sleep(1)
if escolha == indice1 and sorteio == indice2:
    print(f'O computador escolheu {indice2} e você {indice1}')
    print('O COMPUTADOR GANHOU')
elif escolha == indice1 and sorteio == indice3:
    print(f'O computador escolheu {indice3} e você {indice1}')
    print('VOCÊ GANHOU')
elif escolha == indice2 and sorteio == indice1:
    print(f'O computador escolheu {indice1} e você {indice2}')
    print('VOCÊ GANHOU')
elif escolha == indice2 and sorteio == indice3:
    print(f'O computador escolheu {indice3} e você {indice2}')
    print('O COMPUTADOR GANHOU')
elif escolha == indice3 and sorteio == indice1:
    print(f'O computador escolheu {indice1} e você {indice3}')
    print('O COMPUTADOR GANHOU')
elif escolha == indice3 and sorteio == indice2:
    print(f'O computador escolheu {indice2} e você {indice3}')
    print('VOCÊ GANHOU')
elif escolha == indice1 and sorteio == indice1 or escolha == indice2 and sorteio == indice2 or escolha == indice3 and sorteio == indice3:
    print('EMPATE! JOGUEM NOVAMENTE')