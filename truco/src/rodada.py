from mesa import Mesa

class Rodada:

	cartas_mesa = Mesa()
	ganhador = ""
	equipe_ganhadora = 0

	def jogar_carta(self, jogador, carta):
		self.cartas_mesa.adicionar_carta(jogador, carta)

	def definir_ganhador(self, equipes, truco=False, ganhador=""):
		cartas = self.cartas_mesa.cartas
		if not truco:
			jogadores = cartas.keys()
			maior_carta = -1
			
			for jogador in list(jogadores):
				if cartas[jogador].valor > maior_carta:
					maior_carta = cartas[jogador].valor
					self.ganhador = jogador
				
				elif cartas[jogador].valor == maior_carta:
					self.ganhador = ""

		else:
			self.ganhador = ganhador

		for equipe in equipes:
			for jogador in equipe.jogadores:
				if jogador.nome == self.ganhador:
					self.equipe_ganhadora = equipe.codigo
					continue