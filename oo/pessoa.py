class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=27,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    felipe = Pessoa(nome = 'Felipe')
    daniel = Pessoa(felipe, nome='Daniel')
    print(Pessoa.cumprimentar(daniel))
    print(id(daniel))
    print(daniel.cumprimentar())
    print(daniel.nome)
    print(daniel.idade)
    for filho in daniel.filhos:
        print(filho.nome)
    daniel.sobrenome = 'Silva'
    del daniel.filhos
    daniel.olhos = 1
    del daniel.olhos
    print(daniel.__dict__)
    print(felipe.__dict__)
    Pessoa.olhos = 3
    print(daniel.olhos)
    print(felipe.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(daniel.olhos), id(felipe.olhos))
    print(Pessoa.metodo_estatico(), daniel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), daniel.nome_e_atributos_de_classe())


