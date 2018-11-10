# -*- coding: utf-8 -*-

from Vertice import Vertice
from Aresta import Aresta

# Representação de infinito
INF = 1E8

class ListaAdj(object):

    '''
    Construtor da classe
    '''
    def __init__(self, nroVertices):
        
        # Lista de adjacencia de vertices (Membro privado da classe)
        self.__lista = [] 
        
        # Numero de vertices (Membro privado da classe)
        self.__nVertices = 0 
        
        # Dicionario que contem o nome do vertice como chave e 
        # como valor, sua posicao na lista
        self.__posicoes = {}
        self._direcionado = True
        self._nroVertices = nroVertices

    '''
    Destrutor da classe
    '''
    def __del__(self):  
        for v in self.__lista:
            del v 
    
    '''
    Impressão da lista
    '''
    def __str__(self):
        saida = "V = { "
        for v in self.__lista:
            saida += v._obtemNome() + " "
        saida += "}\n\n"

        # Impressão da lista de arestas
        saida += "Vizinhanca dos vertices: \n\n"
        for v in self.__lista:
            saida += v._obtemNome() + ": "
            aux = v._obtemProximo()
            if aux is not None:
                while(aux._obtemProximo() != None):
                    saida += aux._obtemNome() + "(" + str(aux._obtemPeso()) + ") "
                    aux = aux._obtemProximo()
                saida += aux._obtemNome() + "(" + str(aux._obtemPeso()) + ") "
            saida += "\n"
            saida += "\n"
        return saida    
  
    '''
    Dada uma posição na lista, retorna o vértice correspondente
    '''
    def _obtemVertice(self, pos):
        return self.__lista[pos]

    '''   
    Dado um vértice, retorna sua posição relativa na lista
    '''
    def _obtemPosicao(self, v):
        try:
            return self.__posicoes[str(v)]
        except:
            return -1
 
    '''
    Verifica se o vertice v é vizinho de u.
    Em grafos direcionados serão considerados vizinhos apenas
    os sucessores diretos do vértice
    '''
    def _ehVizinho(self, u, v):
        vertice_u = str(u)
        vertice_v = str(v)

        # Busca o vértice u
        pos_u = self._obtemPosicao(vertice_u)
        aux = self.__lista[pos_u]
        while(aux != None): # Buscamos na lista do vértice 'u'
            # Se encontramos vértice v nesta lista
            if(aux._obtemNome() == vertice_v): 
                return True # Retorna True caso 'u' e 'v' sejam vizinhos
            aux = aux._obtemProximo() # Caso contrário vai para o próximo da lista
        
        # Caso não encontremos 'v' na lista de 'u', retorna False
        return False

    
    '''
    Resolve o exercício de Implementação 1 (Problema 1)
    Utilizando uma busca em profundidade adaptada para efetuar
    uma ordenação topológica no grafo, que serve como resposta
    para o trajeto ideal para o gerente.
    '''
    def _resolveProblemaUm(self, exploreObj=None, exploredResult=False):

        self.__listaOrdenacaoTopologica = list()

        caminhoInvalido = False
        self.__verticesVisitados = 0
        
        # Inicia a busca em profundidade pelo primeiro vértice
        # A busca não está em um for com todos os vértices pois
        # o gerente sempre inicia pelo primeiro vertice e, se não conseguir
        # atingir todos os vértices a partir dele, retornaremos um erro.
        self._ordenacaoTopologica(self.__lista[0])

        # Verifica se todos os vértices foram atingidos pela busca.
        # Caso não foram, significa que o grafo é desconexo
        # ou não existe um caminho iniciando pelo vértice 1 que passa por todos os vértices
        if (self.__verticesVisitados < self._nroVertices):
            print("\nSolução não pode ser encontrada.")
        else:
            print("\nSolução encontrada!")
            print("Ordem de visitação das atividades:")
            print(self.__listaOrdenacaoTopologica)

    def _ordenacaoTopologica(self, vertex):

        self.__verticesVisitados += 1
        
        while (vertex._obtemProximo() != None):

            # Obtem o label do próximo (vizinho) vértice
            vizinho_relativo = vertex._obtemProximo()

            # Atualiza a lista de vizinhos do vértice
            # Isso é necessário para quando for chamada a função de obterProximo do vértice
            # na recursão não entrar em loop chamando sempre o 'mesmo' próximo
            vertex._modificaProximo(vizinho_relativo._obtemProximo())

            # Acessa o próximo 'real' através do label obtido
            pos_u = self._obtemPosicao(vizinho_relativo._obtemNome())
            vizinho_real = self.__lista[pos_u]

            if(not vizinho_real._foiVisitado()):
                self._ordenacaoTopologica(vizinho_real)
        
        # Salva vértice na lista final de ordenação topológica
        # Equivalente a etapa de 'colorir de preto'
        self.__listaOrdenacaoTopologica.insert(0, vertex._obtemNome())

        vertex._visitar()

        return
      
    '''
    Adiciona um novo elemento ao grafo
    '''
    def _add(self, u, v = None, peso = 1):
        if(u == None):
            return # Nem  vértice de origem é válido
        
        vertice_u = str(u)
    
        # Se v for None, então verificamos a inserção de um vértice
        if(v == None):
            # Se u não foi inserido, vamos inserí-lo
            if(not (u in self.__lista)):
                self.__criaVertice(u)
                self.__nVertices += 1

        else:
            vertice_v = str(v)
            pos_u = self._obtemPosicao(u)
            pos_v = self._obtemPosicao(v)

            # Se u e v não são vizinhos, cria a ligação entre eles
            if(pos_u >= 0 and pos_v >= 0 and not(self._ehVizinho(u, v))):
                self.__criaAresta(u, v, peso)

                if(not self._direcionado):
                    self.__criaAresta(v, u, peso)
    
    '''
    Cria uma aresta de ligação entre os vértices u e v, dado um 
    peso (1, por default)
    '''
    def __criaAresta(self, u, v, peso = 1):
        pos1 = self._obtemPosicao(u)
        pos2 = self._obtemPosicao(v)
        
        if(pos1 >= 0 and pos2 >= 0):
            aux = self.__lista[pos1] # Vértice auxiliar
            # Encontra o próximo elemento do vetor
            while(aux != None and aux._obtemProximo() != None):                
                aux = aux._obtemProximo()
            # Cria um nó na lista de u contendo o vértice v
            aux._criaProximo(Vertice(self.__lista[pos2]._obtemNome(), peso))    

            # Modifica o último para apontar para nulo
            prox = aux._obtemProximo()
            prox._modificaProximo(None)

    '''
    Criacao de um vertice para a lista
    '''
    def __criaVertice(self, u):

        # Verifica se o vértice u é novo (ou seja: nao foi encontrado 
        # no grafo)
        if(self._obtemPosicao(u) == -1):
            vertice = Vertice(u)
            self.__lista.append(vertice)
            self.__posicoes[str(u)] = self.__lista.index(vertice)