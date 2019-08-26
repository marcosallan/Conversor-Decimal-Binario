def rotina (n_str): # Função para realizar conversão
    v_binario = []
    n = int(n_str)
    while True:
        if n // 2 == 0:
            break
        r = n % 2
        v_binario.append(r)
        n //= 2

    if int(n_str) == 0:
        v_binario.append(0)
    elif int(n_str) > 0:
        v_binario.append(1)

    v_binario.reverse()

    num_bin = ''

    for i in v_binario:
        num_bin += str(i)

    print('O número %s vale %s no sistema binário' %(n_str, num_bin))

while True:
    print()
    d = input('Digite um número para ser convertido para binário: ')
    print()

    rotina(d)

    r = input('\nDeseja continuar ? [s/n] \nR: ')
    if r == 'n':
        print('\n' + 20 * '#' + ' FIM ' + 20 * '#' + '\n')
        break
    else:
        continue # Este bloco não é necessário
