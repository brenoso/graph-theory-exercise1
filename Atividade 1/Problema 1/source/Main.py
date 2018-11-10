# -*- coding: utf-8 -*-

from Grafo import Grafo
import os

# ---------------------- Definição dos Menus ---------------------- #
def print_menu_arquivo():
    print ("\nDigite o nome do arquivo a ser lido:")

def print_menu_geral():
    print ("\n" + 67 * "-")
    print ("\nSelecione a operacao para executar no grafo:\n")
    print("1. Problema 1")
    print("2. Problema 2")
    print ("3. Sair\n")

# Variáveis auxiliares para os menus
sair = False
loop = False

# ---------------------- Menu de leitura do arquivo ---------------------- #

loop=True      
  
while loop:
    print_menu_arquivo()
    arquivo = input()
    path = None
   
    # Navega pela pasta a procura do arquivo
    for root, dirs, files in os.walk("../instances"):
        if path is None: # Evita encontrar dois arquivos com o mesmo nome
            for file in files:
                if arquivo in file:
                    print("\nArquivo encontrado!")
                    path = os.path.join(root, file)
                    print("Caminho: " + path +"\n")
                    loop = False
                    break # Evita encontrar dois arquivos com o mesmo nome
    
    if path is None:
        print("\nArquivo nao encontrado! Certifique-se de estar rodando o sistema a partir da pasta raiz 'source'!\n")

# ---------------------- Menu de Estrutura de Dados ---------------------- #

def cria_grafo():
    global grafo # Torna o grafo acessível fora desse contexto
    grafo = Grafo(tipo_estrutura, path)
    grafo = grafo._cria()
    print(grafo)

tipo_estrutura = 3
print ("\nLista de Adjacencia selecionada!\n")
cria_grafo()

# ------------------------------ Menu Geral ------------------------------ #

loop=True

while loop and not sair:
    print_menu_geral()
    escolha = input("Digite sua escolha [1-3]: ")
    escolha = int(escolha)

    if escolha == 1:
        grafo._resolveProblemaUm()
        sair = True
        loop = False

    elif escolha == 2:
        print ("Ainda não implementada!")
        print ("Saindo...")
        sair = True
        loop = False

    elif escolha == 3:
        print ("Saindo...")
        sair = True
        loop = False

    else:
        print ("\nOpcao escolhida invalida!\n")