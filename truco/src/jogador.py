class Jogador:

	nome = ""
	mao = ""

	def __init__(self, nome):
		self.nome = nome
		self.mao = list()

	def receber_carta(self, carta):
		self.mao.append(carta)

	def jogar_carta(self, rodada, carta):
		rodada.jogar_carta(self.nome, carta)
		self.mao.pop(self.mao.index(carta))