# -*- coding: utf-8 -*-
#==================================================================================================================================#     
#Variáveis
i=1
lista_de_comandos=[0,1,2,3,4,5]
lista_de_produtos=dict()
import json
#==================================================================================================================================#
#chamando estoque
with open('arquivo.txt','r') as arq:
    lista_de_produtos = json.loads(arq.read())
#==================================================================================================================================#
#Print das opções do programa
while i!=0:
    lista=["Controle de Estoque", "0 - sair", "1 - adicionar item", "2 - remover item", "3 - alterar item", "4 - imprimir estoque"]
    for e in lista:
        print(e)
    opcao=int(input("Faça sua escolha:"))   
#==================================================================================================================================#    
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
           if quantidade_inicial<0:
               print("A quantidade inicial não pode ser negativa.")
           else:
               lista_de_produtos[nome_do_produto]['quantidade']=quantidade_inicial
       else:
           print("Produto já está cadastrado.")
#==================================================================================================================================#      
#Opção remover item da lista
    elif opcao==2:
       nome_do_produto=input("Nome do produto:")
       if nome_do_produto in lista_de_produtos:
          del(lista_de_produtos[nome_do_produto])
       else:
          print("Elemento não encontrado.")
#==================================================================================================================================#          
#Opção alterar item da lista          
    elif opcao==3:
       nome_do_produto=input("Nome do produto:")
       if nome_do_produto not in lista_de_produtos:
           print ("Elemento não encontrado.")
       elif nome_do_produto in lista_de_produtos:
           nova_quantidade=int(input("Nova quantidade:"))
           lista_de_produtos[nome_do_produto]['quantidade']+=nova_quantidade
#==================================================================================================================================#          
#Opção imprimir estoque da lista
    elif opcao==4:
        for k in lista_de_produtos:
            print("{0}:{1}".format(k, lista_de_produtos[k])) 
            
            
            
            
            
            
            

original = json.dumps(lista_de_produtos, sort_keys = True, indent=4)
with open('arquivo.txt','w') as arq:
    arq.write(original)
    
