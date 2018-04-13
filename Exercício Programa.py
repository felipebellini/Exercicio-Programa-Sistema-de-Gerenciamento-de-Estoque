# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:21:25 2018

@author: danielcgc
"""
#==================================================================================================================================#
#Print das opções do programa
i=1
while i!=0:
    lista=["Controle de Estoque", "0 - sair", "1 - adicionar item", "2 - remover item", "3 - alterar item", "4 - imprimir estoque"]
    for e in lista:
        print(e)
#==================================================================================================================================#     
#Variáveis
    opcao=int(input("Faça sua escolha:"))
    lista_de_comandos=[0,1,2,3,4]
    lista_de_produtos=dict()
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
       quantidade_inicial=int(input("Quantidade inicial:"))
       if nome_do_produto not in lista_de_produtos: 
           if quantidade_inicial<0:
               print("A quantidade inicial não pode ser negativa.")
           else:
               lista_de_produtos[nome_do_produto]=quantidade_inicial
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
