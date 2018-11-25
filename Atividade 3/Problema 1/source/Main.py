import os

from Arquivo import Arquivo
from Desafio import Desafio

# ---------------------- Definição dos Menus ---------------------- #
def print_menu_arquivo():
    print ("\nDigite o nome do arquivo a ser lido:")

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

# ------------------------------ Execução ------------------------------ #

arquivo = Arquivo(path)
arquivo = arquivo._removerCaracteres(arquivo)

desafio = Desafio(arquivo)
resposta = desafio._executarAtribuicoes()

print(resposta)
print()
