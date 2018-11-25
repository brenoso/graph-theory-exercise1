class Desafio(object):

    '''
    Construtor da classe
    '''
    def __init__(self, arquivo):
        self.__computadores = ['_','_','_','_','_','_','_','_','_','_']
        self.__arquivo = arquivo

    def _executarAtribuicoes(self):

        computadores = self.__computadores
        arquivo = self.__arquivo

        for i, s in enumerate(arquivo):

            job = arquivo[i]
            aplicacao = job[0]
            nroUsuarios = int(job[1])

            # Pega caracteres da posicao 3 em diante, que representa
            # os computadores possíveis
            computadoresPossiveis = list(job[3:])
            # transforma cada valor em inteiro
            computadoresPossiveis = [int(x) for x in computadoresPossiveis]

            # Para cada computador possível, tenta atribuir o job a eles,
            # considerando o número de usuários (que pode ser menor que o número de comp. possíveis)
            for i, s in enumerate(computadoresPossiveis):

                if (computadores[computadoresPossiveis[i]] == '_'):
                    computadores[computadoresPossiveis[i]] = aplicacao
                    nroUsuarios = nroUsuarios - 1

                if (nroUsuarios == 0):
                    break
            
            # Se após a tentativa de atribuir os usuários aos computadores
            # algum usuário ficar de fora, para a execução e retorna '!'
            if (nroUsuarios > 0):
                computadores = "!"
                break
        
        return computadores