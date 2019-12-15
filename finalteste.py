import os
def clear():
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')
class cadastro:
	nome=''
	sobrenome=''
	cpf=''
	email=''
	endereco=''
	telefone=0
	nconta=0
	lcredito= 1000
	saldo= 0.0

def dados (l):
	p1=cadastro()
	p1.nome=input('Nome:')
	p1.sobrenome=input('Sobrenome:')
	p1.cpf=int(input('CPF:'))
	p1.email=input('Email:')
	p1.endereco=input('Endereço:')
	p1.telefone=input('Telefone:')
	p1.nconta=input('Numero da conta:')
	p1.lcredito= 1000.00
	p1.saldo=float(input('Saldo da conta:'))
	
	if (len(l) !=0):
		for i in range (len(l)):
			if (l[i].cpf == p1.cpf):
				clear()
				print (' Cpf já cadastrado')
				return
			if (l[i].nconta == p1.nconta):
				 print ('Conta já existente:')
				 print ('Informe uma nova conta:')
				 p1.nconta=int(input('>'))
	l.append(p1)
	if (p1 !=''):
		print ('Sucesso no cadastro')
		
def menu ():
	print()
	print ('Seja bem vindo!')
	print ('Abaixo realize a opção que desejar !')
	print()
	print('1 - Para Inserir usuário:')
	print('2 - Para alterar dados de clientes:')
	print('3 - Deletar dados de cliente:')
	print('4 - Listar clientes:')
	print('5 - Para movimentar a conta:')
	print('6 - Sair')
	print ()
	x=int(input('Digite a opção desejada:'))
	clear()
	return x

def menu2 ():
	print('Digite a opção desejada')
	print('1 - Para realizar novamente a operação')
	print('0 - Para voltar ao menu anterior')
	print('Digite a operação que deseja realizar')
	y = int(input('>'))
	clear()
	return y
def menubusca():
	print('Digite a opção de filtro desejado')
	print('1 - Nome')
	print('2 - Sobrenome')
	print('3 - CPF')
	print('4 - E-mail')
	print('5 - Endereço')
	print('6 - Complemento')
	print('7 - Telefone')
	print('8 - Numero da conta')
	print('9 - Agência')
	print('10 - Limite de credito')
	print('11 - Saldo')
	bc = int(input('Digite a opção desejada'))
	if(bc == 1):
		bc='nome'
	if(bc==2):
		bc='sobre Nome'
	if(bc==3):
		bc='cpf'
	if(bc==4):
		bc='email'
	if(bc==5):
		bc='endereco'
	if(bc==6):
		bc='complemento'
	if(bc==7):
		bc='tel'
	if(bc==8):
		bc='conta'
	if(bc==9):
		bc='agencia'
	if(bc==10):
		bc='limite'
	if(bc==11):
		bc='saldo'
	print('O valor do params dentro da função é', bc)
	return bc
   
def listcad(l):
    print('1 - Para listar todos os cadastros')
    print('2 - Para buscar um cadastro especifico')
    print('Digite a opção desejada')
    op = int(input('-->'))
    clear()
    if(op == 1):
        for i in range(len(l)):
            print('Nome: ', l[i].nome)
            print('Sobre nome: ',l[i].sobrenome)
            print('CPF: ',l[i].cpf)
            print('E-mail: ',l[i].email)
            print('Endereço: ',l[i].endereco)
            print('Telefone: ',l[i].telefone)
            print('Conta: ',l[i].nconta)
            print('Limite: ',l[i].lcredito)
            print('Saldo: ',l[i].saldo)
            print('------------------------------//----------------------------------')
            print()
    else:
        print('Digite o CPF que dseja consultar')
        value = int(input('-->'))
        for i in range(len(l)):
           if(l[i].cpf == value):
               print('Nome: ', l[i].nome)
               print('Sobre nome: ',l[i].sobrenome)
               print('CPF: ',l[i].cpf)
               print('E-mail: ',l[i].email)
               print('Endereço: ',l[i].endereco)
               print('Telefone: ',l[i].telefone)
               print('Conta: ',l[i].nconta)
               print('Limite: ',l[i].lcredito)
               print('Saldo: ',l[i].saldo)
           else:
               print('Registro não encontrado')
def dadosaltera (l):
	value = int(input('Digite o CPF que deseja fazer alterações:'))
	for i in range(len(l)):
		if(l[i].cpf == value):
			p1=cadastro()
			p1.nome=input('Nome:')
			p1.sobrenome=input('Sobrenome:')
			p1.cpf=int(input('CPF:'))
			p1.email = input('E-mail:')
			p1.endereco = input('Endereço:')
			p1.telefone = int(input('Telefone:'))
			p1.limite = float(input('Limite de credito aprovado:'))
			p1.saldo = float(input('Seu saldo em conta:'))
			
			l[i] = (p1)
			if(p1!=''):
				print('Dados alterados com sucesso')
def excluiclientes(l):
    value = int(input('Digite o CPF que deseja excluir:'))
    for i in range(len(l)):
        if(l[i].cpf == value):
            p1 = i
    print('1 - Confirmar a exclução dos dados do CPF.',l[p1].nome)
    print('0 - Para cancelar a operação')
    r = int(input('>'))
    if(r == 1):
        del(l[p1])
def movimentaconta(l):
    print('Movimentações')
    print('1 - Realizar debito')
    print('2 - Realizar credito')
    op=int(input('Digite a opção desejada:'))
    if(op == 1):
        print('Operação de debito')
        c=int(input('Digite o CPF para fazer o debito:'))
        clear()
        for i in range(len(l)):
            if(l[i].cpf == c):
                print('Digite o valor que deseja debitar')
                val = float(input('-->'))
                if(l[i].saldo >= val):
                    l[i].saldo -= val
                    print('Saque realizado com sucesso')
                    print('Seu saldo atual é de ',round(l[i].saldo))
                    print('Seu limite de credito é de ',round(l[i].lcredito, 2))
                elif(l[i].saldo >= 0):
                    l[i].saldo -= val
                    l[i].saldo *=-1
                    if(l[i].saldo <= l[i].lcredito):
                        print('Seu saldo esta abaixo do valor informado para saque')
                        print('O valor de ',round(l[i].saldo, 2) ,'esta sendo sacado do seu limite de credito')
                        l[i].lcredito -= l[i].saldo
                        l[i].saldo = 0.00
                        print('Saque realizado com sucesso')
                        print('Seu saldo atual é de R$ ',l[i].saldo)
                        print('Seu limite de credito é de R$ ',round(l[i].lcredito, 2))
                    else:
                        clear()
                        print('operação não foi realizada')
                        print('Seu saldo + limite esta abaixo do valor informado para saque')
            else:
                print('CPF informado não foi localizado no sistema')
                
    if(op == 2):
        print('Cŕedito')
        c = int(input('Digite o CPF que deseja realizar a operação:'))
        for i in range(len(l)):
            if(l[i].cpf == c):
                print('Digite o valor que deseja depositar')
                val = float(input('-->'))
                if(l[i].lcredito == 1000):
                    l[i].saldo += val
                    print('Deposito realizado com sucesso')
                    print('Seu saldo atual é de R$ ',round(l[i].saldo, 2))
                    print('Seu limite de credito é de R$ ',round(l[i].lcredito, 2))
                elif(l[i].lcredito < 1000 and l[i].lcredito > 0):
                    l[i].lcredito += val
                    if(l[i].lcredito > 1000):
                        val = l[i].lcredito - 1000
                        l[i].lcredito -= val
                        l[i].saldo += val
                        print('Deposito realizado com sucesso')
                        print('Seu saldo atual é de R$ ',round(l[i].saldo, 2))
                        print('Seu limite de credito é de R$ ',round(l[i].lcredito, 2))
                    else:
                        print('Deposito realizado com sucesso')
                        print('Seu saldo atual é de R$ ',round(l[i].saldo, 2))
                        print('Seu limite de credito é de R$ ',round(l[i].lcredito, 2))
                else:
                    print('Operação não realizada, tente novamente mais trade')
            else:
                print('CPF informado não foi localizado no sistema')
    if(op !=1 and op !=2):
        print('operação não localizada')
#Exec
i=1
while(i > 0):
	clear()
	l = []
	opcao=1
	while(opcao != 6):
		opcao = menu()
		subMenu = 1
		if(opcao == 1):
			while(subMenu == 1):
				dados(l)
				subMenu = menu()
		if(opcao == 2):
			while(subMenu == 1):
				dadosaltera(l)
				subMenu = menu2()
		if(opcao == 3):
			while(subMenu == 1):
				excluiclientes(l)
				subMenu = menu2()
		if(opcao == 4):
			while(subMenu == 1):
				listcad(l)
				subMenu = menu2()
		if(opcao == 5):
			while(subMenu == 1):
				movimentaconta(l)
				subMenu = menu2()
		else:
			i -=1
			print('Credenciais invalidas, você possui mais',i, 'tentativa(s)')

