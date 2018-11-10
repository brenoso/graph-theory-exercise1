import os

from Arquivo import Arquivo
from Grafo import Grafo


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

'''

A solução do problema consiste em:

1 - Cria dois grafos/matrizes (original e proposto) a partir da leitura do arquivo
2 - Roda o algoritmo de Floyd-Warshall para obter o caminho mínimo de todos vértices para todos.
3 - Com as duas matrizes (original e proposto) de caminhos mínimos de todos para todos,
    cruza as distâncias de cada vértice do grafo original e propostos, verificando a condição
    do enunciado 'grafoProposto[i][j] < (fatorX * grafoOriginal[i][j] + constanteY)'. Caso
    não for satisfeita para qualquer 'novas intersecoes', retornamos False.

'''

arquivo = Arquivo(path)

grafo =  Grafo(arquivo)

grafoOriginal = grafo._getGrafoOriginal()
grafoProposto = grafo._getGrafoProposto()

GrafoOriginalCaminhosMinimos = grafo._floydWarshall(grafoOriginal)
GrafoPropostoCaminhosMinimos = grafo._floydWarshall(grafoProposto)

resposta = grafo._resolveProblema(GrafoOriginalCaminhosMinimos, GrafoPropostoCaminhosMinimos)
resposta = 'Sim' if resposta else 'Não'

print("Resposta: "+ resposta +'\n')