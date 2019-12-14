class cadastro:
	nome=''
	sobrenome=''
	cpf=0.0
	email=''
	endereco=''
	telefone=0.0
	nconta=0.0
	lcredito=0.0
	saldo=0.0
cad=[]
def opção (x):
	p1=cadastro()
	p1.nome=input('Nome:')
	p1.sobrenome=input('Sobrenome:')
	p1.cpf=input('CPF:')
	p1.email=input('Email:')
	p1.endereco=input('Endereço:')
	p1.telefone=input('Telefone:')
	p1.nconta=input('Numero da conta:')
	p1.lcredito=input('Limite de crédito:')
	p1.saldo=input('Saldo da conta:')
	cad.append(p1)
	pergunta=int(input('Deseja cadastrar um novo cliente, se deseja digite 1 caso contrario digite 0 :'))
	while pergunta >=0:
		if pergunta==1:
			menu(opção(1))
		elif pergunta==0:
			menu()
		else:
			print('Opção invalida digite novamente:')
			x=int(input('Digite a opção desejada:'))
def menu ():
	print('1 para Inserir usuário:')
	print('2 para alterar dados de clientes:')
	print('3 Excluir cliente:')
	print('4 listar clientes:')
	print('5 para movimentar a conta:')
	print('6 sair')
	x=int(input('Digite a opção desejada:'))
	while x >= 0:
		if x==1:
			opção (x)
		if x==0:
			menu()
		if x==2:
			alteracad(x)
		if x==3:
			exclui(x)
	else:
		print('Opção invalida digite novamente:')
		x=int(input('Digite a opção desejada:'))
	return x
def alteracad (x):
	for i in range (3):
		input(cad[i].email)
		input(cad[i].endereco)
		input(cad[i].telefone)
		input(cad[i].saldo)
def exclui (x):
	numero=int(input('Informe o numero da conta que você deseja exluir:')
	for p1.conta in 
#x=input('Informe seu usuário:')
#if x=='Vinicius':
menu()	
#else:
	#print('Usuário invalido')

		
		
