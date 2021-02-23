'''
Programação Orientada a Objetos
Técnico em Informática
2º Ano Matutino
Alunas: Emmanuele Holanda, Fátima Gonzaga e Mikaelly da Silva Santos

'''

import time
import getpass
import os

class minhaexception (Exception):
  pass
class ExececaoVazio (Exception):
  pass

def vazio_error(x):
  if x =="":
    raise ExececaoVazio()  
  else:
    return  

class Pessoa:
  def __init__(self, nome, email, senha, telefone):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.tel = telefone

  def cadastro(self):
    if menu1 == '1':
#Exceçaõ em nome: campo vazio.
      while True: 
        try:
          self.nome = input('Nome: ')
          vazio_error(self.nome)
        except ExececaoVazio:
          print ("Preencha todos os campos")
        else:
          break

#Exceção em email: campo vazio.
      while True:
        try:
          self.email = input('Email: ')
          vazio_error(self.email)
        except ExececaoVazio:
          print ("Preencha todos os campos")
        else:
          break

#Exceção em senha: campo vazio.      
      while True:
        try:
          self.senha = getpass.getpass ('Senha: ')
          #Senha oculta
          vazio_error(self.senha)
        except ExececaoVazio:
          print ("Preencha todos os campos")
        else:
          break
 
#Exceção em telefone: apenas números, campo vazio.
      while True:
        try:
          self.tel = input('Telefone: ')
          vazio_error(self.tel)
          for r in self.tel:
            if r.isdigit==False:
              raise ValueError
          
          if len(self.tel) != 11:
            raise IndexError 

            
        except ExececaoVazio:
          print ("Preencha todos os campos")
        except ValueError:
          print("Número inválido. ")
        except IndexError:
          print("oia")

        
        else:
          break  
          
#Exceçaõ em cpf: apenas números, campo vazio.
      while True:
        try:
          self.cpf= input('cpf:')
          vazio_error(self.cpf)
          self.cpf = int(self.cpf)
        except ExececaoVazio:
          print ("Preencha todos os campos")
        except ValueError:
          print("CPF foi preenchido incorretamente. Use apenas números.")
        else:
          break

#Exceçaõ em endereço: campo vazio.
      while True:
        try:
          self.endereco = input('Endereço: ') 
          vazio_error(self.endereco)
        except ExececaoVazio:
          print ("Preencha todos os campos")
        else:
          break  
      
    elif menu1 == '2':
      senhafunc = '9247'  #senha de acesso do sistema 
      while True:
        cod = input('Digite o código de funcionários: ')
        if cod == senhafunc:
          self.nome = input('Nome: ')
          self.email = input('Email: ')
          self.senha = input('Senha: ')
          self.tel = input('Telefone: ')
          break
        else:
          print('Código inválido')
          continue

  def alterarDados(self):
    while True:
      if menu1 == '1':
        escolherDado = input("\n '1': Nome\n '2': Email\n '3': Senha\n '4': Telefone\n '5': Endereço| ")
        if escolherDado == '1':
          self.nome = input('Digite novo nome: ')
          print("Alteração concluída!")
          break
        if escolherDado == '2':
          self.email = input('Digite novo email: ')
          print("Alteração concluída!")
          break
        if escolherDado == '3':
          while True: 
            senha = input('Digite senha antiga: ')
            if senha == self.senha:
              self.senha = input('Digite nova senha: ')
              print("Alteração concluída!")
              break
            else: 
              print('Senha inválida')
              continue
        if escolherDado == '4':
          self.telefone = input('Digite novo número: ')
          print("Alteração concluída!")
          break
        if escolherDado == '5':
          self.endereco = input('Digite novo endereço: ')
          print("Alteração concluída!")
          break

      elif menu1 == '2':
        escolherDado = input(" '1': Nome\n '2': Email\n '3': Senha\n '4': Telefone| ")
        if escolherDado == '1':
          self.nome = input('Digite novo nome: ')
          print("Alteração concluída!")
          break
        if escolherDado == '2':
          self.email = input('Digite novo email: ')
          print("Alteração concluída!")
          break
        if escolherDado == '3':
          while True: 
            senha = input('Digite senha antiga: ')
            if senha == self.senha:
              self.senha = input('Digite nova senha: ')
              break
            else: 
              print('Senha inválida')
              continue
        if escolherDado == '4':
          self.telefone = input('Digite novo número: ')
          print("Alteração concluída!")
          break
        continue
 
class Funcionarios(Pessoa): 
  def __init__(self, nome, email, senha, telefone):
    super().__init__(nome, email, senha, telefone)
  pass

  def confirmarPedidos(self):
    pass

class Cliente(Pessoa):
  def __init__(self, nome, email, senha, telefone, endereco, cpf):
    self.ender= endereco
    self.cpf= cpf
    super().__init__(nome, email, senha, telefone)

# A classe Produto compõe o item Pedido
class Produto: 
  def __init__(self, nome, preco, quantidade):
    self.nome = nome
    self.preco = preco
    self.qntd = quantidade

class Bebidas(Produto):
  def __init__(self, nome, preco, quantidade):
    super().__init__(nome, preco, quantidade)
  
  def escolherQntd(self, prece):
    ml = input(f" '1' - 300ml   \n '2' - 500ml| ")
    if ml == '1':
      self.preco = 3.00 + prece
      self.qntd = '300 ml'
    elif ml == '2':
      self.preco = 5.00 + prece
      self.qntd = '500 ml'

class Adicionais(Produto):
  def __init__(self, nome, preco, quantidade):
    super().__init__(nome, preco, quantidade)

  def escolherFormato(self):
    formato = input("\n1- O adicional será enviado separado.  \n2- O adicional será enviado junto| ")
    if formato == '1':
      print('O produto será enviado separado.')
      time.sleep(3) #tempo

    elif formato =='2':
      print('O produto será enviado junto')
      time.sleep(2)
           
class Pedido:
  def __init__(self, pagamento):
    self.pagament = pagamento

  def formaPagamento(self):
    pagamento = input('FORMA DE PAGAMENTO:\n 1- Cartão de Crédito\n 2- Cartão de Débito \n 3- Dinheiro| ')
    if pagamento == '1':
       print("\nOk, efetue o pagamento com o entregador.")
    elif pagamento == '2':
       print("\nOk, efetue o pagamento com o entregador.")
    elif pagamento == '3':
       input("\nVai precisar de troco? Se SIM, informe o valor,\ncaso NÃO somente clique 'Enter' e finalize a compra: ")

class Item_Pedido:
  def __init__(self):
    self.produtos = []
    
  def inserirProdutos(self, produto):
    self.produtos.append(produto)

  def listaProdutos(self):
     for produto in self.produtos:  
       print(produto.nome, produto.preco)
  
  def cardapio(self):#estava faltando self
    while True:
      menu = input("'1'- Bebidas \n'2'- Adicionais\n'3'- Finalizar| ")
      if os.name == "nt":
        os.system("cls")
      else:
        os.system ("clear")
      if menu == '1':
        print('-------------------')
        print(" '1'- ", sucoUva.nome,"   300ml: R$4,00  500ml: R$6,00")
        print(" '2'- ", sucoLimao.nome, "   300ml: R$3,00  500ml: R$5,00")
        print(" '3'- ", sucoLaranja.nome, "   300ml: R$3,00  500ml: R$5,00")
        print(" '4'- ", sucoMaracuja.nome, "   300ml: R$3,00  500ml: R$5,00")
        print(" '5'- ", sucoMorango.nome, "   300ml: R$4,00  500ml: R$6,00")
        print(" '6'- ", sucoAcerola.nome, "   300ml: R$3,00  500ml: R$5,00")
        print('-------------------')
        
        pedido = input("Digite pedido: ")
        if pedido == '1':
          sucoUva.escolherQntd(1)
          valorT(sucoUva.preco)#valorT=Valor Total
          #inserindo suco de uva na lista de itens pedidos
          self.inserirProdutos(sucoUva)
        elif pedido == '2':
          sucoLimao.escolherQntd(0)
          valorT(sucoLimao.preco)
          self.inserirProdutos(sucoLimao)
        elif pedido == '3':
          sucoLaranja.escolherQntd(0)
          valorT(sucoLaranja.preco)
          self.inserirProdutos(sucoLaranja)
        elif pedido == '4':
          sucoMaracuja.escolherQntd(0)
          valorT(sucoMaracuja.preco)
          self.inserirProdutos(sucoMaracuja)
        elif pedido == '5':
          sucoMorango.escolherQntd(1)
          valorT(sucoMorango.preco)
          self.inserirProdutos(sucoMorango)
        elif pedido == '6':
          sucoAcerola.escolherQntd(0)
          valorT(sucoAcerola.preco)
          self.inserirProdutos(sucoAcerola)
        continue

      elif menu == '2':
        if menu == '2':
          print('-------------------')
          print(" '1'- ", leite.nome, "   R$3,00")
          print(" '2'- ", aguadecoco.nome, "   R$2,00")
          print(" '3'- ", mel.nome, "   R$5,00")
          print('-------------------')
          pedidoA = input("Digite pedido: ")
          if pedidoA == '1':
            valorT(leite.preco)
            self.inserirProdutos(leite)
            leite.escolherFormato()
          elif pedidoA == '2':
            valorT(aguadecoco.preco)
            self.inserirProdutos(aguadecoco)
            aguadecoco.escolherFormato()
          elif pedidoA == '3':
            valorT(mel.preco)
            self.inserirProdutos(mel)
            mel.escolherFormato()

          if os.name == "nt":         
            os.system("cls")
          else:
            os.system ("clear")
            
        continue
      
      elif menu == '3':
        print('---------------------')
        print('  LISTA DE COMPRAS')
        print('---------------------')
        self.listaProdutos()
        print('---------------------')
        print('Total: R$', sum(valor))
        print('---------------------')
        time.sleep(3)
        if os.name == "nt": 
          os.system("cls")
        else:
          os.system ("clear")
          
        ped.formaPagamento()
        
        pagar = input("\nDigite 2 para finalizar compra| ")
        if pagar == '2':
          print('\n----------------------')
          print('Agradecemos por comprar no UNIVERSO DE SABORES! \nAguarde que seu pedido logo chegará no endereço,', cliente.endereco, ', caso o endereço de entrega for outro, por favor, informe a seguir:' )
          cliente.endereco = input ("\nEndereço para entrega: ")
          print('-----------------------')
          print ("\nOBRIGADO E DESFRUIT! \nSeu pedido está sendo preparado e sairá para entrega em breve!")
          break

valor = []

#PESSOAS
cliente = Cliente('', '', '','', '','')
func = Funcionarios('','','','')
ped = Pedido ('')
produto = Produto ('', '', '')
itempedido = Item_Pedido () #tirar cardápio se não for utilizar

#PRODUTOS
sucoUva = Bebidas('Suco de Uva', 'x', 'x')
sucoLimao = Bebidas('Suco de Limão', 'x', 'x')
sucoLaranja = Bebidas('Suco de Laranja', 'x', 'x')
sucoMaracuja = Bebidas('Suco de Maracujá', 'x', 'x')
sucoAcerola = Bebidas('Suco de Acerola', 'x', 'x')
sucoMorango = Bebidas('Suco de Morango', 'x', 'x')
mel = Adicionais('Mel', 5.00, 'x')
leite = Adicionais('Leite', 3.00, 'x')
aguadecoco = Adicionais('Água de coco', 2.00, 'x')


def valorT(bebide):
  val = bebide
  valor.append(val)
  total = sum(valor)
  print('R$',total)


print("UNIVERSO DE SABORES")
while True:
  menu = input("Digite '1' para fazer cadastro| ")
  if menu == '1':
    if os.name == "nt":  #Limpar tela     
      os.system("cls")
    else:
      os.system ("clear")
    menu1 = input("\nDigite '1' se você for cliente\nDigite '2' se for funcionário| ")
    if os.name == "nt": #Limpar tela
      os.system("cls")
    else:
      os.system ("clear")

    if menu1 == '1': #MENU CLIENTES
      cliente.cadastro()
      print('\nBEM VINDO', cliente.nome.upper())
      time.sleep(2)
      if os.name == "nt": #Limpar tela
        os.system("cls")
      else:
        os.system ("clear")
      while True: 
        menuCliente = input("""\nDigite 1 para alterar dados
Digite 2 para fazer pedido| """)
        if menuCliente == '1':
          cliente.alterarDados()
          continue
        elif menuCliente == '2':
          itempedido.cardapio()#vamos utilizar objetos para manipular
          break

    elif menu1 == '2': #MENU FUNCIONÁRIOS
      func.cadastro()
      print()
      print('\nBEM VINDO', func.nome.upper(), "!")
      print()
      menuFunc = input("""\nDigite '1' para alterar dados
Digite '2' para ver pedidos| """)
      if menuFunc == '1':
        func.alterarDados()
        continue
      if menuFunc == '2':
        #print: (ped)
        pass
    break
  else: 
    print('Inválido')
    continue

'''if len(self.cpf()) != 11:
  print("fgjfddf")
else:
  continue

def diminuir(str):
    max = 10 # Numero Maximo de caracteres Permitidos.
    if len(str) > max:
      print("jhtfjyhfjjgg")
      break
    else:
      continue
'''