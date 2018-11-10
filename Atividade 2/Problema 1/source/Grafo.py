# -*- coding: utf-8 -*-

# Representação de Infinito
INF = 1E8

class Grafo(object):

    '''
    Construtor da classe Grafo (Matriz de Adjacências)
    '''
    def __init__(self, arquivo):
        self.__arquivo = arquivo

    '''
    Retorna o grafo original a partir do arquivo
    '''
    def _getGrafoOriginal(self):

        nroIntersecoes = self.__arquivo._getIntersecoes()

        grafoOriginal = self._criaGrafoGenerico(nroIntersecoes)

        for i in range(1, nroIntersecoes+1):

            arquivo = self.__arquivo._getArquivo()
            intersecoes = arquivo[i].split()

            for n in range(len(intersecoes)):
                intersecoes[n] = int(intersecoes[n])

                if intersecoes[n] == i:
                    grafoOriginal[i-1][i-1] = 0

                else:
                    grafoOriginal[i-1][(intersecoes[n]-1)] = 1

        return grafoOriginal

    '''
    Retorna o grafo proposto a partir do arquivo
    '''
    def _getGrafoProposto(self):

        nroIntersecoes = self.__arquivo._getIntersecoes()

        grafoProposto = self._criaGrafoGenerico(nroIntersecoes)

        for i in range(1, nroIntersecoes+1):

            arquivo = self.__arquivo._getArquivo()
            intersecoes = arquivo[i+nroIntersecoes].split()

            for n in range(len(intersecoes)):
                intersecoes[n] = int(intersecoes[n])



                if intersecoes[n] == i:
                    grafoProposto[i-1][i-1] = 0

                else:
                    grafoProposto[i-1][(intersecoes[n]-1)] = 1
        
        return grafoProposto

    '''
    Cria grafo genérico (Matriz) a partir do número de vértices (intersecoes)
    '''
    def _criaGrafoGenerico(self, intersecoes):
        
        return [[INF] * intersecoes for i in range(intersecoes)]

    '''
    Encontra caminho mínimo de todos vértices para todos vértices
    '''
    def _floydWarshall(self, grafo):

        nroIntersecoes = self.__arquivo._getIntersecoes()

        for k in range(nroIntersecoes):
            for i in range(nroIntersecoes):
                for j in range(nroIntersecoes):
                    grafo[i][j] = min(grafo[i][j], grafo[i][k] + grafo[k][j])

        return grafo

    '''
    Resolve o problema proposto a partir das duas matrizes de caminho mínimo
    '''
    def _resolveProblema(self, grafoOriginal, grafoProposto):

        nroIntersecoes = self.__arquivo._getIntersecoes()
        fatorX = self.__arquivo._getFatorX()
        constanteY = self.__arquivo._getConstanteY()

        for i in range(nroIntersecoes):
            for j in range(nroIntersecoes):

                if grafoProposto[i][j] > (fatorX * grafoOriginal[i][j] + constanteY):
                    return False
        
        return True
