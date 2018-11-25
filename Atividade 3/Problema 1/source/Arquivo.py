class Arquivo(object):

    '''
    Construtor da classe
    '''
    def __init__(self, path):
        self.__arquivo = self._lerArquivo(path)

    '''
    Efetua a leitura no arquivo
    '''
    def _lerArquivo(self, path):
        arquivo = open(path, 'r')
        return arquivo.readlines()

    '''
    Remove caracteres indesejados do arquivo
    '''
    def _removerCaracteres(self, arquivo):

        arquivo = [arquivo.replace(";", "").replace("\n", "") for arquivo in arquivo.__arquivo]

        return arquivo