from Avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo):
     self._nome = nome.title()
     self._categoria = categoria.upper()
     self._ativo = False
     self._avaliacao = []
     Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(38)} {'Categoria do Restaurante'.ljust(36)} {'Status'.ljust(33)} {'Nota'}\n')
        for restaurante in cls.restaurantes:
            print (f'Restaurante - {restaurante._nome.ljust(25)}Categoria - {restaurante._categoria.ljust(25)}Ativo - {restaurante.ativo.ljust(25)} Nota - {restaurante.media_avaliacoes}\n')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    def alterar_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            sem_nota = 'Sem notas'
            return sem_nota
        soma_nota = sum(avalicao._nota for avalicao in self._avaliacao)
        media_nota = round(soma_nota / len(self._avaliacao),1)
        return media_nota

