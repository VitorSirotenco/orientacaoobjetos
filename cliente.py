class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property #isso indica que esse metodo é uma propriedade da classe nome, sendo chamado por cliente.nome
    def nome(self):
        print('chamando proprerty nome')
        return self.__nome.title()

    @nome.setter #pra mudar o atributo nome diretamente
    def nome(self, nome):
        print('chamando setter nome')
        self.__nome = nome
