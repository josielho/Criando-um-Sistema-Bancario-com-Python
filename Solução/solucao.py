menu = '''

[u] Criar usuário
[c] Criar conta corrente
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

mensagem_depositar = '''
Você selecionou a opção Depositar!
Informe o valor do depósito:
=> '''
mensagem_sacar = '''
Você selecionou a opção Sacar!
Informe o valor do saque:
=> '''
mensagens_criar_usuario = [
{'chave' : 'nome',
'mensagem' :'''
Você selecionou a opção Criar usuário!
Informe o nome do usuário:
=> '''},
{'chave' : 'data_de_nascimento',
'mensagem' :'''
Informe a data de nascimento do usuário, ex: 01/01/2001
=> '''},
{'chave' : 'cpf',
'mensagem' :'''
Informe o cpf do usuário, ex: 111.222.333-44
=> '''},
{'chave' : 'endereco',
'mensagem' :'''
Informe o endereço do usuário, ex: logradouro, nro - bairro - cidade/sigla estado
=> '''}]

mensagem_criar_conta = '''
Você selecionou a opção Criar conta corrente!
Informe o cpf do usuário cadastrado, ex: 111.222.333-44
=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
lista_users = []
lista_contas = []
LIMITE_SAQUES = 3
ultimo_numero_da_conta = 0
AGENCIA = '0001'

#POSITIONAL ONLY
def Deposito( saldo, valor_deposito, extrato, /):
    saldo += valor_deposito
    mensagem_deposito_sucesso = '\n=====================DEPÓSITO=====================\n'
    mensagem_deposito_sucesso += f'Depósito de R$: {valor_deposito:.2f}\n'
    mensagem_deposito_sucesso += '=================================================='
    extrato += mensagem_deposito_sucesso
    print(mensagem_deposito_sucesso)
    return saldo, extrato

#KEYWORD ONLY
def Saque( *, saldo, valor_saque, numero_saques, extrato):
    saldo -= valor_saque
    numero_saques += 1
    mensagem_saque_sucesso = '\n======================SAQUE=======================\n'
    mensagem_saque_sucesso += f'Saque de R$: {valor_saque:.2f}\n'
    mensagem_saque_sucesso += '=================================================='
    extrato += mensagem_saque_sucesso
    print(mensagem_saque_sucesso)
    return numero_saques, saldo, extrato

#saldo -> POSITIONAL ONLY && extrato -> KEYWORD ONLY
def Extrato( saldo, / , *, extrato):
    if extrato:
        print(extrato)
        print(f'Saldo atual R$ {saldo:.2f}')
    else:
        print('Não foram realizadas movimentações.')
        print(f'Saldo atual R$ {saldo:.2f}')

def Validar_cpf( valorcpf, lista_users):
    str_cpf = ''
    cpf_existe = False
    for caracter in list(valorcpf):
        try:
            int(caracter)
        except:
            pass
        else:
            str_cpf += caracter
    for dict_user in lista_users:
        if dict_user['cpf'] == str_cpf:
            cpf_existe = True
            break
    return str_cpf, cpf_existe
    
def Add_conta_new_cpf( agencia, ultimo_numero_da_conta, str_cpf,lista_contas):
    dict_new_conta = dict(agencia = agencia, numero_da_conta = [ultimo_numero_da_conta])
    dict_cpf = {str_cpf : dict_new_conta}
    lista_contas.append(dict_cpf)


def Add_conta( str_cpf, cpf_existe, ultimo_numero_da_conta, lista_contas, agencia):
    if cpf_existe:
        ultimo_numero_da_conta += 1

        if lista_contas:
            conta_cpf_existe = False
            for contas_cpf in lista_contas:
                if str_cpf in contas_cpf:
                    conta_cpf_existe = True
                    contas_cpf[str_cpf]['numero_da_conta'].append(ultimo_numero_da_conta)
                    break
        if (not lista_contas) or (not conta_cpf_existe):
            Add_conta_new_cpf( agencia, ultimo_numero_da_conta, str_cpf, lista_contas)

        print(lista_contas)

    else:
        print('Nenhum usuário registrado na base para o cpf informado, por favor registre um usuário com esse cpf.')

    return ultimo_numero_da_conta


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
                saldo, extrato = Deposito( saldo, valor_deposito, extrato)
            
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
                        numero_saques, saldo, extrato = Saque( saldo = saldo, valor_saque = valor_saque, numero_saques = numero_saques, extrato = extrato)
    
    elif opcao == 'e':
        Extrato(saldo, extrato = extrato)

    elif opcao == 'u':
        new_dict_user = {}
        for dicionario in mensagens_criar_usuario:
            if dicionario['chave'] == 'cpf':
                valorcpf = input(dicionario['mensagem'])
                str_cpf, cpf_existe = Validar_cpf(valorcpf, lista_users)

                if cpf_existe:
                    break
                new_dict_user['cpf'] = str_cpf
            else:
                new_dict_user[dicionario['chave']] = input(dicionario['mensagem'])

        if not cpf_existe:
            lista_users.append(new_dict_user)
            print(new_dict_user)
        else:
            print('Já existe um usuário registrado na base para o cpf informado!')

    elif opcao == 'c':
        valorcpf = input(mensagem_criar_conta)
        str_cpf, cpf_existe = Validar_cpf( valorcpf, lista_users = lista_users)
        ultimo_numero_da_conta = Add_conta( str_cpf, cpf_existe, ultimo_numero_da_conta, lista_contas, AGENCIA)

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')