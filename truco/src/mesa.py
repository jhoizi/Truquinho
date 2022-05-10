class Mesa:

	cartas = {}

	def adicionar_carta(self, jogador, carta):
		self.cartas[jogador] = carta