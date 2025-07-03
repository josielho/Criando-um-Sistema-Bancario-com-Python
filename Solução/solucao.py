menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

mensagem_depositar = f'''
Você selecionou a opção Depositar!
Informe o valor do depósito:
=> '''
mensagem_sacar = f'''
Você selecionou a opção Sacar!
Informe o valor do saque:
=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        try:
            valor_deposito = float(input(mensagem_depositar))
        except:
            print('O valor informado não pode ser utilizado, por favor selecione novamente a operação desejada.')
        else:
            if valor_deposito <= 0 :
                print('Valores menores ou iguais a zero não podem ser utilizados, por favor selecione novamente a operação desejada.')
            else:
                saldo += valor_deposito
                mensagem_deposito_sucesso = '\n=====================DEPÓSITO=====================\n'
                mensagem_deposito_sucesso += f'Depósito de R$: {valor_deposito:.2f}\n'
                mensagem_deposito_sucesso += '=================================================='
                extrato += mensagem_deposito_sucesso
                print(mensagem_deposito_sucesso)
            
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES:
            print('O limite de três saques diários foi atingido, por favor selecione outra operação ou retorne amanhã.')
        else:
            try:
                valor_saque = float(input(mensagem_sacar))
            except:
                print('O valor informado não pode ser utilizado, por favor selecione novamente a operação desejada.')
            else:
                if valor_saque <= 0:
                    print('Valores menores ou iguais a zero não podem ser utilizados, por favor selecione novamente a operação desejada.')
                else:
                    if valor_saque > saldo:
                        print('Saldo insuficiente, por favor selecione novamente a operação desejada.')
                    elif valor_saque > limite:
                        print('O valor informado é superior aos R$ 500 permitidos por saque, por favor selecione novamente a operação desejada.')
                    else:
                        saldo -= valor_saque
                        numero_saques += 1
                        mensagem_saque_sucesso = '\n======================SAQUE=======================\n'
                        mensagem_saque_sucesso += f'Saque de R$: {valor_saque:.2f}\n'
                        mensagem_saque_sucesso += '=================================================='
                        extrato += mensagem_saque_sucesso
                        print(mensagem_saque_sucesso)
    
    elif opcao == 'e':
        if extrato:
            print(extrato)
            print(f'Saldo atual R$ {saldo:.2f}')
        else:
            print('Não foram realizadas movimentações.')
            print(f'Saldo atual R$ {saldo:.2f}')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')