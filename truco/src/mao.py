from rodada import Rodada

class Mao:

	rodadas = []
	manilha = ""
	valor = 1
	equipe_ganhadora = 0

	def __init__(self):
		self.rodadas = list()


	def adicionar_rodada(self):
		self.rodadas.append(Rodada())

	def definir_aumento_pontos(self, valor):
		self.valor = valor

	def definir_manilha(self, manilha):
		self.manilha = manilha

	def definir_ganhador(self):
		e1 = 0
		e2 = 0
		r = 0
		for rodada in self.rodadas:
			if rodada.equipe_ganhadora != 0:
				if rodada.equipe_ganhadora == 1:
					e1 += 1
				else:
					e2 += 1
			else:
				
				if r == 0:
					e1 = 1
					e2 = 1 

				elif r == 1:
					self.equipe_ganhadora = self.rodadas[0].equipe_ganhadora
					continue

				else:
					 self.equipe_ganhadora = self.rodadas[0].equipe_ganhadora
					 continue

			r += 1 

		if e1 == 2:
			self.equipe_ganhadora = 1
			
		elif e2 == 2:
			self.equipe_ganhadora = 2