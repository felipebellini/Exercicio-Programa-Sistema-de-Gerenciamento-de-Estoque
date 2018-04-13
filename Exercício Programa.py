# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:21:25 2018

@author: danielcgc
"""
#==================================================================================================================================#
#Print das opções do programa
lista=["Controle de Estoque", "0 - sair", "1 - adicionar item", "2 - remover item", "3 - alterar item", "4 - imprimir estoque"]
for e in lista:
    print(e)
#==================================================================================================================================#     
#Variáveis
opcao=int(input("Faça sua escolha:"))    
lista_de_produtos=dict()
#==================================================================================================================================# 
#Opção sair do programa 
    if opcao==0:
       print("Obrigado por utilizar nosso sistema.")
#==================================================================================================================================#   
#Opção adicionar produto à lista
    if opcao==1:
       nome_do_produto=input("Nome do produto:")
       quantidade_inicial=int(input("Quantidade inicial:"))
       if quantidade_inicial<0:
          print("A quantidade inicial não pode ser negativa.")
       else:
          lista_de_produtos[nome_do_produto]=quantidade_inicial
#==================================================================================================================================#      
#Opção remover item da lista
      