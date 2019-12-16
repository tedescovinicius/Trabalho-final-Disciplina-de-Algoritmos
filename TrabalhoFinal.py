import os
def clear(): #Importação biblioteca para limpeza de tela
    os.system('cls' if os.name == 'nt' else 'echo -e \\\\033c')

class cadastro: # Classe cadastro para tipos de dados
	nome=''
	sobrenome=''
	cpf=''
	email=''
	endereco=''
	telefone=0
	nconta=0
	lcredito= 1000
	saldo= 0.0

def dados (l): # Função dados, cadastrar cliente
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
	
	if (len(l) !=0): # se o tamanho da lista l for diferente de 0
		for i in range (len(l)): # Percorre a lista l
			if (l[i].cpf == p1.cpf): # Se o cpf na lista l é igual cpf digitado, cpf ja cadastrado
				clear() #Limpa tela
				print (' Cpf já cadastrado')
				return
			if (l[i].nconta == p1.nconta): #Se a conta na lista l é igual a conta digitada, conta já digitada
				 print ('Conta existente:')
				 print ('Informe uma nova conta:')
				 p1.nconta=int(input('>'))
	l.append(p1) #Adiciona no elemento p1
	if (p1 !=''): 
		print ('Cadastro realizado com sucesso')
		
def menu (): # Função com as opções para o usuário
	print()
	print ('Digite abaixo a opção que desejar !')
	print()
	print('1 - Inserir cliente:')
	print('2 - Alterar dados de um clientes:')
	print('3 - Excluir cliente:')
	print('4 - Listar clientes:')
	print('5 - Movimento da conta:')
	print('6 - Sair')
	print ()
	x=int(input('Digite a opção:'))
	clear() #Limpa tela
	return x 

def menu2 (): #Função realizar novamente operação, ou voltar no menu geral.
	print('Digite a opção:')
	print('1 - Para realizar novamente a operação')
	print('0 - Para voltar ao menu anterior')
	print('Digite a operação que deseja realizar')
	y = int(input('>'))
	clear() #Limpa tela
	return y

def menubusca(): # Função para buscar 
	print('Digite a opção de filtro desejado')
	print('1 - Nome')
	print('2 - Sobrenome')
	print('3 - CPF')
	print('4 - E-mail')
	print('5 - Endereço')
	print('6 - Telefone')
	print('7 - Numero da conta')
	print('8 - Limite de credito')
	print('9 - Saldo')
	bc = int(input('Digite a opção:'))
	if(bc == 1):
		bc='nome'
	if(bc==2):
		bc='sobrenome'
	if(bc==3):
		bc='cpf'
	if(bc==4):
		bc='email'
	if(bc==5):
		bc='endereco'
	if(bc==6):
		bc='telefone'
	if(bc==7):
		bc='Numero'
	if(bc==8):
		bc='Limite'
	if(bc==9):
		bc='saldo'
	print('O valor do bc dentro da função é', bc)
	return bc
   
def listcad(l): # Função para listar clientes
    print('1 - Para listar todos os cadastros')
    print('2 - Para buscar cadastro especifico')
    print('Digite a opção desejada')
    op = int(input('-->'))
    clear()
    if(op == 1): # Se digitar 1, lista todos clientes cadastrados
        for i in range(len(l)): # Percorre a lista l
            print('Nome: ', l[i].nome) #Acessa o nome na lista l
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
    else: # Se digitar 2, cadastro especifico de um cliente
        print('Digite o CPF que deseja consultar')
        value = int(input('-->'))
        for i in range(len(l)): # Percorre a lista l
           if(l[i].cpf == value): #Se o cpf na lista l é igual ao cpf digitada, ok
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

def dadosaltera (l): # Função para alterar dados cliente
	value = int(input('Digite o CPF que deseja fazer alterações:'))
	for i in range(len(l)): # Percorre a lista l
		if(l[i].cpf == value): #Se o cpf na lista l é igual ao cpf digitada, ok
			p1=cadastro()
			p1.nome=input('Nome:')
			p1.sobrenome=input('Sobrenome:')
			p1.cpf=int(input('CPF:'))
			p1.email = input('E-mail:')
			p1.endereco = input('Endereço:')
			p1.telefone = int(input('Telefone:'))
			p1.nconta=input('Numero da conta:')
			p1.limite = float(input('Limite de credito aprovado:'))
			p1.saldo = float(input('Seu saldo em conta:'))
			
			l[i] = (p1)
			if(p1!=''):
				print('Dados alterados com sucesso')

def excluiclientes(l): #Função para excluir clientes
    value = int(input('Digite o CPF que deseja excluir:'))
    for i in range(len(l)): # Percorre a lista l
        if(l[i].cpf == value): #Se o cpf na lista l é igual ao cpf digitada, ok
            p1 = i
    print('1 - Confirmar a exclução dos dados do CPF.',l[p1].nome)
    print('0 - Para cancelar a operação')
    r = int(input('>'))
    if(r == 1):
        del(l[p1]) #Deleta cliente

def movimentaconta(l): #Função para realizar movimentos na conta
    print('Movimentações')
    print('1 - Realizar debito')
    print('2 - Realizar credito')
    op=int(input('Digite a opção:'))
    if(op == 1): #Se op = 1, operação débito
        print('Operação de debito')
        c=int(input('Digite o CPF para fazer o debito:'))
        clear() #Limpa tela
        for i in range(len(l)): # Percorre a lista l
            if(l[i].cpf == c): # Se o cpf digitado no inicio, for igual ao cpf digitado agora, ok
                print('Digite o valor que deseja debitar')
                val = float(input('-->'))
                if(l[i].saldo >= val): #Se o saldo na lista l é maior ou igual ao val digitada, ok
                    l[i].saldo -= val # Saldo na lista l - o val digitado. Conta saldo atual
                    print('Seu saldo atual é de ',round(l[i].saldo))
                    print('Seu limite de credito é de ',round(l[i].lcredito, 2))
                elif(l[i].saldo >= 0): #Se o saldo na lista l é menor ou igual a 0, ok
                    l[i].saldo -= val # Saldo na lista l - val digitado
                    l[i].saldo *=-1
                    if(l[i].saldo <= l[i].lcredito): # Se o saldo na lista l for menor ou igual a credito na lista l, ok
                        print('Seu saldo esta abaixo do valor informado para debito')
                        print('O valor de ',round(l[i].saldo, 2) ,'esta sendo debitado do seu limite de credito')
                        l[i].lcredito -= l[i].saldo
                        l[i].saldo = 0.00
                        print('Seu saldo atual é de R$ ',l[i].saldo)
                        print('Seu limite de credito é de R$ ',round(l[i].lcredito, 2))
                    else:
                        clear()
                        print('operação não foi realizada')
                        print('Seu saldo + limite esta abaixo do valor informado para debito')
            else:
                print('CPF informado não foi localizado no sistema')
                
    if(op == 2): # Se op = 2, operção crédito
        print('Credito')
        c = int(input('Digite o CPF que deseja realizar a operação:'))
        for i in range(len(l)): # Percorre a lista l
            if(l[i].cpf == c): # Se o cpf digitado no inicio, for igual ao cpf digitado agora, ok
                print('Digite o valor que deseja depositar')
                val = float(input('-->'))
                if(l[i].lcredito == 1000): # Se o lcredito na lista l for = 1000,ok
                    l[i].saldo += val # Saldo na lista l + val digitado
                    print('Deposito realizado com sucesso')
                    print('Seu saldo atual é de R$ ',round(l[i].saldo, 2))
                    print('Seu limite de credito é de R$ ',round(l[i].lcredito, 2))
                elif(l[i].lcredito < 1000 and l[i].lcredito > 0): # Percorre lcredito na lista l, tendo valor menor que 1000 e maior que 0, ok
                    l[i].lcredito += val # Credito na lista l + val digitado
                    if(l[i].lcredito > 1000): #Se o lcredito na lista l for maior que 1000, ok
                        val = l[i].lcredito - 1000 # lcredito na lista l - 1000
                        l[i].lcredito -= val # lcredito na lista l - val digitado
                        l[i].saldo += val # Saldo na lista l + val digitado
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
    if(op !=1 and op !=2): #Se op !=1 e !=2, operacão finalizada
        print('operação não localizada')

#Condições do acesso menu principal!
i=1
while(i > 0):
	clear()
	l = [] 
	opcao=1
	while(opcao != 6): #Se digitar 6, sai do programa
		opcao = menu()
		subMenu = 1
		if(opcao == 1): #Se digitar 1, vai para inserir dados
			while(subMenu == 1):
				dados(l) #Cadastrar clientes
				subMenu = menu()
		if(opcao == 2): #Se digitar 2, vai para alterar dados clientes
			while(subMenu == 1):
				dadosaltera(l) #Alterar dados clientes
				subMenu = menu2()
		if(opcao == 3): #Se digitar 3, vai para deletar dados clientes
			while(subMenu == 1):
				excluiclientes(l) #Excluir clientes
				subMenu = menu2()
		if(opcao == 4): #Se digitar 4, vai para listar clientes
			while(subMenu == 1):
				listcad(l)# Listar clientes
				subMenu = menu2()
		if(opcao == 5): #Se digitar 5, vai para movimentar conta
			while(subMenu == 1):
				movimentaconta(l) #Movimentar conta
				subMenu = menu2()
		else: # Se caso não digitou nenhum dos números a cima, tentativa invalida
			i -=1
			print('Credenciais invalidas, você possui mais',i, 'tentativa(s)')
