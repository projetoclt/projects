#1- menu= apresentar as opções do menu
#2- opções= adicionar conta, pesquisar, debitar ou receber
#3- adicionar conta= nome,cpf,endereço,saldo = mínimo 500

import os
import pickle

dados = []
if os.path.exists("dados") and os.path.getsize("dados") > 0:
    try:
        with open("dados", 'rb') as file:
            dados = pickle.load(file)
    except (EOFError, pickle.UnpicklingError) as e:
        print("Erro ao carregar os dados. O arquivo pode estar corrompido.")
        dados = []
dados_provisorio = []

def formatar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  
    cpf_formatado = ""
    
    for i, digito in enumerate(cpf):
        if i in [3, 6]:
            cpf_formatado += "." 
        if i == 9:
            cpf_formatado += "-"  
        cpf_formatado += digito
        
    return cpf_formatado

def adicionar():
    os.system('cls' if os.name == 'nt' else 'clear')  # Excluir o histórico do terminal

    print("Adicionar conta\n") 
    print('coloque o nome do cliente')
    nome = input("Nome: \n") 
    if nome == '5':
        menu()
    
    dados_provisorio.append(nome)
    
    print('coloque o endereço do cliente')
    endereço = input("Endereço: \n")
    if endereço == '5':
        menu()
    dados_provisorio.append(endereço)
    
    print('coloque o CPF do cliente')
    cpf = input("CPF: \n")
    if cpf == '5':
        menu()
    
    cpf = formatar_cpf(cpf)

    if cpf in dados:
        print("\nesse cpf já esta cadastrado")
        sair3 = input("\nDigite '5' para sair: ")
        if sair3 == '5':
            menu()


    if len(cpf) != 14:  
        print('Número de CPF deve conter 11 dígitos')
        sair3 = input("\nDigite '5' para sair: ")
        if sair3 == '5':
            menu()
    
    dados_provisorio.append(cpf)
    
    print('coloque o saldo do cliente')
    saldo = int(input("Saldo: \n"))
    if saldo == 5:
        menu()
    if saldo < 500:
        print("Saldo mínimo não atingido")
        sair2 = input("\nDigite '5' para voltar ao menu: ")
        if sair2 == '5':
            menu()
    else:
        dados.append(nome)
        dados.append(endereço)
        dados.append(cpf)
        dados.append(saldo)
        dados_provisorio.append(saldo)
    
    print("Conta adicionada com sucesso")
    print(dados_provisorio)
    with open("dados", 'wb') as file:
        pickle.dump(dados, file)
    
    sair2 = input("\nDigite '5' para voltar ao menu: ")
    if sair2 == '5':
        menu()
    return dados

def pesquisar():
    os.system('cls' if os.name == 'nt' else 'clear')

    confirmar = input("Digite o CPF do cliente para ver se está cadastrado: \n")
    confirmar = formatar_cpf(confirmar)
    
    if confirmar in dados:
        print("\nCliente cadastrado\n")
        print("Nome: ", dados[dados.index(confirmar) - 2])   
        print("Endereço: ", dados[dados.index(confirmar) - 1])
        print("CPF: ", dados[dados.index(confirmar)])
        print("Saldo: ", dados[dados.index(confirmar) + 1])
    else:
        print('\nCliente não cadastrado')
        
    sair2 = input("\nDigite '5' para voltar ao menu: ")
    if sair2 == '5':
        menu()

def debitar(cpf1):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'Esse cliente tem esse saldo: {dados[dados.index(cpf1) + 1]}')
    deb1 = int(input('\nDeseja debitar quanto: '))

    if deb1 < 0:
        print('\nValor a debitar não pode ser negativo.')
        sair3 = input("\nDigite '5' para voltar ao menu: ")
        if sair3 == '5':
            menu()

    sub = dados[dados.index(cpf1) + 1] - deb1
    print(f'\nO saldo atual é: {sub}')
    dados[dados.index(cpf1) + 1] = sub
    
    with open("dados", 'wb') as file:
        pickle.dump(dados, file)
         
    sair2 = input("\nDigite '5' para voltar ao menu: ")
    if sair2 == '5':
        menu()
    
def receber(cpf1):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f'Esse cliente tem esse saldo: {dados[dados.index(cpf1) + 1]}')
    deb1 = int(input('Deseja receber quanto: '))

    if deb1 < 0:
        print('\nValor a debitar não pode ser negativo.')
        sair3 = input("\nDigite '5' para voltar ao menu: ")
        if sair3 == '5':
            menu()
            
    sub = dados[dados.index(cpf1) + 1] + deb1
    print(f'O saldo atual é: {sub}')
    dados[dados.index(cpf1) + 1] = sub
    
    with open("dados", 'wb') as file:
        pickle.dump(dados, file)
         
    sair2 = input("\nDigite '5' para voltar ao menu: ")
    if sair2 == '5':
        menu()

def depositar():
    os.system('cls' if os.name == 'nt' else 'clear')

    cpf1 = input('Digite o CPF do cliente: ')
    cpf1 = formatar_cpf(cpf1)
    
    if cpf1 in dados:
        print('\n1- Debitar')
        print('2- Receber\n')
        oqvc = int(input('O que você deseja fazer?: \n\nSair = 5: '))
        if oqvc == 1:
            debitar(cpf1)
        elif oqvc == 2:
            receber(cpf1)
        elif oqvc == 5:
            menu()
    else:
        print('\nCPF não cadastrado')
        sair2 = input("\nDigite '5' para voltar ao menu: ")
        if sair2 == '5':
            menu()

def Créditos():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(
        'Participantes deste projeto:\n Felippe, Kaique, Giovanni e Miguel\n e o professor Guilherme :)\n'
    )
    sair = input("Digite '5' para voltar ao menu: ")

    try:
        sair = int(sair)
    except ValueError:
        Créditos()
        return

    if sair > 5 or sair < 5:
        Créditos()

    if sair == 5:
        menu()

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print(
        'Bem-vindo ao Banco da Coreia do Norte!\n Digite o valor de 1 a 4!\n Nós amamos o Capitalismo!\n'
    )
    print("1- Adicionar conta")
    print("2- Pesquisar")
    print("3- Depositar e sacar")
    print("4- Créditos\n")
    pesq = input("O que você deseja fazer?: ")

    try:
        pesq = int(pesq)
    except ValueError:
        menu()
        return

    if pesq > 4 or pesq < 1:
        menu()

    if pesq == 1:
        adicionar()
    elif pesq == 2:
        pesquisar()
    elif pesq == 3:
        depositar()
    elif pesq == 4:
        Créditos()

menu()
