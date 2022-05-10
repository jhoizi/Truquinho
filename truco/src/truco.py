from imports import *

class Truco:

	partidas = []
	dealer = Dealer("Mary")

	def definir_jogadores(self, jogadores):
		if not len(jogadores) > 0:
			c = 1
			for equipe in self.partidas[-1].equipes:
				
				print("Digite o nome do jogador da equipe ", c, " :")
				nome1 = input()
				print("Digite o nome do outro jogador da equipe ", c, " :")
				nome2 = input()
				equipe.definir_jogadores([Jogador(nome1), Jogador(nome2)])
				c += 1
		else:
			c = 0
			e = 1
			for equipe in self.partidas[-1].equipes:
				equipe.definir_jogadores([Jogador(jogadores[c]), Jogador(jogadores[c+1])])
				equipe.codigo = e
				c += 2
				e += 1

	def nova_partida(self, jogadores=[]):
		self.partidas.append(Partida())
		self.definir_jogadores(jogadores)

	def nova_mao(self):
		self.partidas[-1].maos.append(Mao())

	def nova_rodada(self):
		self.partidas[-1].maos[-1].adicionar_rodada(Rodada())