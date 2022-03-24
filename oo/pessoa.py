class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=27,):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    felipe = Mutante(nome = 'Felipe')
    daniel = Homem(nome='Daniel')
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
    print(daniel.olhos)
    print(felipe.olhos)
    print(Pessoa.olhos)
    print(id(Pessoa.olhos), id(daniel.olhos), id(felipe.olhos))
    print(Pessoa.metodo_estatico(), daniel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), daniel.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(felipe, Pessoa))
    print(isinstance(felipe, Homem))
    print(felipe.olhos)
    print(felipe.cumprimentar())
    print(daniel.cumprimentar())


