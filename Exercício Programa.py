# -*- coding: utf-8 -*-
#==================================================================================================================================#     
#Variáveis
i=1
lista_de_comandos=[0,1,2,3,4,5,6]
lista_de_produtos=dict()
import json
#==================================================================================================================================#
#chamando estoque
with open('Lista de produtos.txt','r') as arquivo:
    lista_de_produtos = json.loads(arquivo.read())
#==================================================================================================================================#
#Print das opções do programa
while i!=0:
    lista=["Controle de Estoque", "0 - sair", "1 - adicionar item", "2 - remover item", "3 - alterar item", "4 - imprimir estoque", "5 - produtos com quantidade negativa","6 - valor monetário do estoque"]
    for e in lista:
        print(e)
    opcao=int(input("Faça sua escolha:"))       
    if opcao not in lista_de_comandos:
        print("Comando inválido.")    
#==================================================================================================================================# 
#Opção sair do programa 
    if opcao==0:
       i=0 
       print("Obrigado por utilizar nosso sistema.")
#==================================================================================================================================#   
#Opção adicionar produto à lista
    elif opcao==1:
       nome_do_produto=input("Nome do produto:")
       if nome_do_produto not in lista_de_produtos: 
           lista_de_produtos[nome_do_produto] = {}
           quantidade_inicial=int(input("Quantidade inicial:"))
           while quantidade_inicial<0:
               quantidade_inicial=int(input("A quantidade inicial não pode ser negativa. Digite uma nova quantidade:"))
           lista_de_produtos[nome_do_produto]['quantidade']=quantidade_inicial    
           preco=float(input("Preço unitário:"))    
           while preco<0:
               preco=float(input("O preço não pode ser negativo. Digite novamente:"))
           while preco==0:
               preco=float(input("O preço não pode ser nulo. Digite novamente:"))
           lista_de_produtos[nome_do_produto]['preço unitário']=preco
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
       if nome_do_produto not in lista_de_produtos:
           print ("Elemento não encontrado.")
       elif nome_do_produto in lista_de_produtos:
           print("1 - alterar quantidade")
           print("2 - alterar preço unitário")
           print("3 - alterar ambos")
           opcao=int(input("Faça sua escolha:"))
           while opcao < 1 or opcao > 3:
               opcao=int(input("Comando inválido.Digite novamente:"))
           if opcao == 1:
               print("Quantidade atual:{0}".format(lista_de_produtos[nome_do_produto]['quantidade']))
               nova_quantidade=int(input("Nova quantidade:"))
               lista_de_produtos[nome_do_produto]['quantidade']+=nova_quantidade
               print("Quantidade alterada com sucesso.")
           elif opcao == 2:
               print("Preço unitário atual:{0}".format(lista_de_produtos[nome_do_produto]['preço unitário']))
               novo_preco=float(input("Novo preço unitário:"))
               while novo_preco + lista_de_produtos[nome_do_produto]['preço unitário'] < 0 or novo_preco + lista_de_produtos[nome_do_produto]['preço unitário'] == 0 :
                   novo_preco=float(input("O preço unitário não pode ser negativo. Digite novamente:"))    
               lista_de_produtos[nome_do_produto]['preço unitário']+=novo_preco
               print("Preço unitário alterado com sucesso.")
           elif opcao == 3:
               print(lista_de_produtos[nome_do_produto])
               nova_quantidade=int(input("Nova quantidade:"))
               lista_de_produtos[nome_do_produto]['quantidade']+=nova_quantidade
               novo_preco=float(input("Novo preço unitário:"))
               while novo_preco + lista_de_produtos[nome_do_produto]['preço unitário'] < 0 :
                   novo_preco=float(input("O preço unitário não pode ser negativo. Digite novamente:"))
               while novo_preco + lista_de_produtos[nome_do_produto]['preço unitário'] == 0:
                   novo_preco=float(input("O preço unitário não pode ser nulo. Digite novamente:"))
               lista_de_produtos[nome_do_produto]['preço unitário']+=novo_preco
               print("Item alterado com sucesso.")
#==================================================================================================================================#          
#Opção imprimir estoque da lista
    elif opcao==4:
        for k in lista_de_produtos:
            print("{0}:{1}".format(k, lista_de_produtos[k])) 
#==================================================================================================================================#          
#Opcão imprimir produtos com quantidade negativa
    elif opcao==5:  
        for produto in lista_de_produtos:
            if lista_de_produtos[produto]["quantidade"] < 0:
                print("{0}:{1}".format(produto, lista_de_produtos[produto]["quantidade"]))
#==================================================================================================================================#          
#Opção de Imprimir o valor monetário total em estoque
    elif opcao==6:
        valor_monetario = 0
        for item in lista_de_produtos:
            valor_monetario += lista_de_produtos[item]['quantidade'] * lista_de_produtos[item]['preço unitário']
        print("O valor monetário total no estoque é: {0}".format(valor_monetario))

atualizacao = json.dumps(lista_de_produtos, sort_keys = True, indent=4,ensure_ascii=False)
with open('Lista de produtos.txt','w') as arquivo:
    arquivo.write(atualizacao)
