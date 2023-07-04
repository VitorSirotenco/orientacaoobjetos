class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print('Construindo objeto')
        self.__numero = numero #__ pra deixar os atributos privados
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo = '001'

    def extrato(self):
        print('O titular {} tem {} reais de saldo'.format(self.__titular,self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self,valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            print('Saque de {} reais realizado com sucesso'.format(valor))
        else:
            print('Voce não pode sacar essa quantidade')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod #metodos estaticos da classe
    def codigo_banco():
        return '001'



