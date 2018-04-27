# -*- coding: utf-8 -*-


#==================================================================================================================================#             
#==================================================================================================================================#                                 
#firebase
from firebase import firebase
firebase = firebase.FirebaseApplication ('https://desoft-cdf.firebaseio.com/', None)

if firebase.get('DeSoft CDF') is None:
    estoque = {}
else:
    estoque = firebase.get('DeSoft CDF', None)
   
    firebase.patch('https://desoft-cdf.firebaseio.com/', estoque)
   

#==================================================================================================================================#             
#==================================================================================================================================#             
Loja=dict()
lista_de_produtos={}
i=1
lista_de_comandos=[0,1,2,3,4]
lista_de_comandos2=[0,1,2,3,4,5,6]
#==================================================================================================================================#
#Print das opções do programa    
while i!=0:
    lista=["Controle de Loja", "0 - sair", "1 - analisar loja", "2 - adicionar loja", "3 - remover loja","4 - imprimir lojas cadastradas"]
    for e in lista:
        print(e)
    opcao=int(input("Faça sua escolha:"))       
    if opcao not in lista_de_comandos:
        print("Comando inválido.")
#==================================================================================================================================# 
#Opção sair do programa 
    elif opcao==0:
       i=0 
       print("Obrigado por utilizar nosso sistema.")
#==================================================================================================================================# 
#Opção analisar loja
    elif opcao == 1:
        nome_da_loja=input("Digite o nome da loja:")
        if nome_da_loja not in Loja:
            print("Loja não encontrada.")
        while i!=0:
              print(nome_da_loja)
              lista=["Controle de Estoque", "0 - sair", "1 - adicionar item", "2 - remover item", "3 - alterar item", "4 - imprimir estoque", "5 - produtos com quantidade negativa","6 - valor monetário do estoque"]
              for e in lista:
                  print(e)
              opcao=int(input("Faça sua escolha:"))       
              if opcao not in lista_de_comandos2:
                      print("Comando inválido.")
#==================================================================================================================================#                       
#Opção sair do programa 
              elif opcao==0:
                     i=0 
                     print("Obrigado por utilizar nosso sistema.")  
#==================================================================================================================================#                       
#Opção adicionar item à lista                     
              elif opcao==1:
                   nome_do_produto=input("Nome do produto:")
                   if nome_do_produto not in lista_de_produtos: 
                          lista_de_produtos[nome_do_produto] = {}
                          quantidade_inicial=int(input("Quantidade inicial:"))
                          while quantidade_inicial<0:
                              quantidade_inicial=int(input("A quantidade inicial não pode ser negativa. Digite uma nova quantidade:"))
                          lista_de_produtos[nome_do_produto]['quantidade']=quantidade_inicial    
                          preco_unitario=float(input("Preço unitário:"))    
                          while preco_unitario<0:
                                  preco_unitario=float(input("O preço não pode ser negativo. Digite novamente:"))
                          while preco_unitario==0:
                                  preco_unitario=float(input("O preço não pode ser nulo. Digite novamente:"))
                          lista_de_produtos[nome_do_produto]['preço unitário']=preco_unitario
                          Loja[nome_da_loja]['Lista de produtos']=lista_de_produtos
                          print("Produto cadastrado com sucesso.")
                   else:
                          print("Produto já está cadastrado.")
#==================================================================================================================================#      
#Opção remover item da lista
              elif opcao==2:
                  nome_do_produto=input("Nome do produto:")
                  if nome_do_produto in lista_de_produtos:
                      del(lista_de_produtos[nome_do_produto])
                      print("Produto removido com sucesso.")
                  else:
                      print("Elemento não encontrado.")  
#==================================================================================================================================#          
#Opção alterar item da lista          
              elif opcao==3:
                  nome_do_produto=input("Nome do produto:")
                  if nome_do_produto not in Loja[nome_da_loja]['Lista de produtos']:
                      print ("Elemento não encontrado.")
                  elif nome_do_produto in Loja[nome_da_loja]['Lista de produtos']:
                          print("1 - alterar quantidade")
                          print("2 - alterar preço unitário")
                          print("3 - alterar ambos")
                          opcao=int(input("Faça sua escolha:"))
                          while opcao < 1 or opcao > 3:
                              opcao=int(input("Comando inválido.Digite novamente:"))
                          if opcao == 1:
                              print("Quantidade atual:{0}".format(Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['quantidade']))
                              nova_quantidade=int(input("Nova quantidade:"))
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['quantidade']+=nova_quantidade
                              print("Quantidade alterada com sucesso.")
                          elif opcao == 2:
                              print("Preço atual:{0}".format(Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário']))
                              novo_preco=float(input("Novo preço unitário:"))
                              while novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário'] < 0 or novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário'] == 0 :
                                  novo_preco=float(input("O preço não pode ser negativo. Digite novamente:"))    
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário']+=novo_preco
                              print("Preço alterado com sucesso.")
                          elif opcao == 3:
                              print(Loja[nome_da_loja]['Lista de produtos'][nome_do_produto])
                              nova_quantidade=int(input("Nova quantidade:"))
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['quantidade']+=nova_quantidade
                              novo_preco=float(input("Novo preço unitário:"))
                              while novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário'] < 0 :
                                  novo_preco=float(input("O preço não pode ser negativo. Digite novamente:"))
                              while novo_preco + Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário'] == 0:
                                  novo_preco=float(input("O preço não pode ser nulo. Digite novamente:"))
                              Loja[nome_da_loja]['Lista de produtos'][nome_do_produto]['preço unitário']+=novo_preco
                              print("Item alterado com sucesso.") 
#==================================================================================================================================#          
#Opção imprimir estoque da lista
              elif opcao==4:
                  for k in Loja[nome_da_loja]['Lista de produtos']:
                      print("{0}:{1}".format(k, Loja[nome_da_loja]['Lista de produtos'][k]))                               
#==================================================================================================================================# 
#Opcão imprimir produtos com quantidade negativa
              elif opcao==5:  
                  for produto in Loja[nome_da_loja]['Lista de produtos']:
                      if Loja[nome_da_loja]['Lista de produtos'][produto]["quantidade"] < 0:
                          print("{0}:{1}".format(produto, Loja[nome_da_loja]['Lista de produtos'][produto]["quantidade"]))
#==================================================================================================================================#          
#Opção de Imprimir o valor monetário total em estoque
              elif opcao==6:
                  valor_monetario = 0
                  for item in Loja[nome_da_loja]['Lista de produtos']:
                      valor_monetario += Loja[nome_da_loja]['Lista de produtos'][item]['quantidade'] * Loja[nome_da_loja]['Lista de produtos'][item]['preço unitário']
                  print("O valor monetário total no estoque é:{0}".format(valor_monetario))                          
#==================================================================================================================================#  
#==================================================================================================================================#                       
#Opção adicionar loja
    elif opcao==2:
                   nome_da_loja=input("Digite o nome da loja:")
                   if nome_da_loja not in Loja:
                       Loja[nome_da_loja]={}
                       Loja[nome_da_loja]['Lista de produtos']={}
                       print("Loja cadastrada com sucesso.")
                   else:
                       print("Loja já cadastrada.")
#==================================================================================================================================#          
#==================================================================================================================================#                       
#Opção remover loja
    elif opcao == 3:
                  nome_da_loja=input("Digite o nome da loja:")
                  if nome_da_loja not in Loja:
                      print("Loja não encontrada.")
                  else:
                      del(Loja[nome_da_loja])    
                      print("Loja removida com sucesso.")             
#==================================================================================================================================#             
#==================================================================================================================================#             
#Opção imprimir lojas cadastradas
    elif opcao == 4:
                for e in Loja:
                    print(e)
#==================================================================================================================================#             
#==================================================================================================================================#                                 
#firebase
firebase.patch('https://desoft-cdf.firebaseio.com/estoque', lojas)
