# -*- coding: utf-8 -*-

class Arquivo(object):

    '''
    Construtor da classe
    '''
    def __init__(self, path):
        self.__arquivo = self._lerArquivo(path)
        self.__intersecoes = int(self.__arquivo[0])
        self.__fatorX = int(self.__arquivo[len(self.__arquivo) - 1][0])
        self.__constanteY = int(self.__arquivo[len(self.__arquivo) - 1][2])

    '''
    Efetua a leitura no arquivo
    '''
    def _lerArquivo(self, path):
        arquivo = open(path, 'r')
        return arquivo.readlines()

    '''
    Lê no arquivo as intersecoes
    '''
    def _getIntersecoes(self):

        return self.__intersecoes

    '''
    Retorna o fator X 
    '''
    def _getFatorX(self):

        return self.__fatorX

    '''
    Retorna a constante Y
    '''
    def _getConstanteY(self):

        return self.__constanteY

    '''
    Retorna o arquivo
    '''
    def _getArquivo(self):

        return self.__arquivo
    

