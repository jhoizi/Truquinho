from truco import *
import pygame
from pygame.locals import *
from random import *
import sys
from configs import *


class Tela:

	tela = "" 
	truco = Truco()
	baralho = Baralho()
	jogadores = []
	ordem_jogadores = []
	primeiro_jogador = []
	jogador = ""
	humano = ""
	mesa = []
	maior_carta = ""
	nos = 0
	eles = 0
	pausa = False
	carta_virada = Carta(pygame.image.load(baralho_dir + "virada.png"),0, 0, 'virada')
	carta_virada_rodada = Carta(pygame.transform.rotate(pygame.image.load(baralho_dir + "virada.png"), 90),0, 0, 'virada')

	def cartas(self):
		self.tela.fill([0, 64, 0])
		self.baralho_e_vira()
		self.pontuacao()

		for jogador in self.jogadores:
			for i in range(0, len(jogador.mao)):
				if jogador.nome != self.humano.nome:
					if jogador.nome == self.truco.partidas[self.ultima_partida()].equipes[0].jogadores[1].nome:
						self.desenhar_carta(self.carta_virada.imagem, jogador.mao[i].posicao)
					else:
						self.desenhar_carta(self.carta_virada_rodada.imagem, jogador.mao[i].posicao)
				else:
					self.desenhar_carta(jogador.mao[i].imagem, jogador.mao[i].posicao)
		for carta in self.mesa:
			self.tela.blit(carta.imagem, carta.posicao)

	def desenhar_carta(self, carta, posicao):
		self.tela.blit(carta, posicao)

	def baralho_e_vira(self):
		carta = Carta(pygame.image.load(baralho_dir + "virada.png"),0, 0, 'virada')
		c = 0
		self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].manilha.posicao = [posicoes_cartas[-1][0], posicoes_cartas[-1][1] + 20]
		self.tela.blit(self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].manilha.imagem, self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].manilha.posicao)
		
		for i in range(20):
			carta.posicao = [x + c for x in posicoes_cartas[-1]]
			self.tela.blit(carta.imagem, carta.posicao)
			c += 0.4
	
	def pontuacao(self):
		c = 0
		for nome in ["Nós", "Eles"]:
			self.tela.blit(self.fonte1.render(nome, 1, (255, 0, 0)), [c, 0])
			c+= 70
		c = 20
		for ponto in [self.nos, self.eles]:
			self.tela.blit(self.fonte2.render(str(ponto), 1, (255, 0, 0)), [c, 50])
			c+= 70

	def rodar_cartas(self, jogadores):
		for jogador in jogadores:
			for i in range(0, len(jogador.mao)):
				jogador.mao[i].imagem = pygame.transform.rotate(jogador.mao[i].imagem, 90)

	def nova_mao(self):
		self.truco.nova_mao()
		self.limpar_maos()
		self.truco.dealer.entregar_cartas(self.jogadores, self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()])
		self.rodar_cartas(self.jogadores[2:])
		self.nova_radada()
		self.mesa = list() 
		self.cartas()

	def nova_radada(self):
		self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].adicionar_rodada()
		self.mesa = list()

	def ultima_mao(self):
		return len(self.truco.partidas[self.ultima_partida()].maos) - 1

	def ultima_partida(self):
		return len(self.truco.partidas) - 1

	def limpar_maos(self):
		for jogador in self.jogadores:
			jogador.mao = list()

	def ler_entrada(self, tecla):
		maos = self.truco.partidas[self.ultima_partida()].maos
		if tecla[K_SPACE]:
			if len(maos) == 0:
				self.nova_mao()
		if tecla[K_LEFT]:
			self.jogada(self.humano, 0)
		if tecla[K_DOWN]:
			if not len(maos[self.ultima_mao()].rodadas) > 2:
				self.jogada(self.humano, 1)
			else:
				self.jogada(self.humano, 0)
		if tecla[K_RIGHT]:
			if not len(maos[self.ultima_mao()].rodadas) > 1:
				self.jogada(self.humano, 2)
			else:
				if not len(maos[self.ultima_mao()].rodadas) > 2:
					self.jogada(self.humano, 1)
				else:
					self.jogada(self.humano, 0)

	def robo_jogada(self, jogador):
		jogada = 0
		valores = [carta.valor for carta in jogador.mao]
		maos = self.truco.partidas[self.ultima_partida()].maos
		
		if len(maos[self.ultima_mao()].rodadas) == 1:
			valores_cartas_mesa = [carta.valor for carta in self.mesa]
			if e_par(len(self.mesa)):
				if len(self.mesa) == 0:
					jogada = valores.index(max(valores))
				elif len(self.mesa) == 1:
					jogada = valores.index(max(valores))
				else:
					if self.mesa[0].valor ==  max(valores_cartas_mesa):
						jogada = valores.index(min(valores))
					else:
						if max(valores) >= max(valores_cartas_mesa):
							jogada = valores.index(max(valores))
						else:
							jogada = valores.index(min(valores))
			else:
				if max(valores) >= max(valores_cartas_mesa):
					jogada = valores.index(max(valores))
				else:
					jogada = valores.index(min(valores))

		if len(maos[self.ultima_mao()].rodadas) == 2:
			valores_cartas_mesa = [carta.valor for carta in self.mesa]
			if e_par(len(self.mesa)):
				if len(self.mesa) == 0:
					jogada = valores.index(max(valores))
				elif len(self.mesa) == 1:
					jogada = valores.index(max(valores))
				else:
					if self.mesa[0].valor ==  max(valores_cartas_mesa):
						jogada = valores.index(min(valores))
					else:
						if max(valores) >= max(valores_cartas_mesa):
							jogada = valores.index(max(valores))
						else:
							jogada = valores.index(min(valores))
			else:
				if max(valores) >= max(valores_cartas_mesa):
					jogada = valores.index(max(valores))
				else:
					jogada = valores.index(min(valores))
		
		return jogada

	def jogada(self, jogador, carta=""):
		if jogador.nome != self.humano.nome:
			carta = self.robo_jogada(jogador) 
		
		jogador.mao[carta].posicao = posicoes_cartas_jogadas[self.jogadores.index(jogador)]
		self.mesa.append(jogador.mao[carta])
		jogador.jogar_carta(self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].rodadas[-1], jogador.mao[carta])
		self.cartas()

		if not self.ordem_jogadores.index(jogador) == 3:
			self.jogador = self.ordem_jogadores[self.ordem_jogadores.index(jogador) + 1]

	def ordenar_jogadores(self):
		primeiro = self.ordem_jogadores.index(self.jogador)
		self.ordem_jogadores = self.ordem_jogadores[primeiro:] + self.ordem_jogadores[:primeiro - len(self.ordem_jogadores)]

	def inicio(self):
		self.tela.fill([0, 64, 0])
		left = 100
		for naipe in self.baralho.naipes:
			for carta in self.baralho.truco[naipe]:
				if carta.valor == 10:
					self.desenhar_carta(carta.imagem, (left + height / 4 + 20, width / 4 - 10))
					left += 50 
		self.tela.blit(self.fonte3.render("Truquinho", 1, (255, 0, 0)), [height / 2 - 50, width / 4 - 100])
		self.tela.blit(self.fonte2.render("Tecle Espaço para continuar!", 1, (255, 255, 255)), [height / 2 - 100, width / 2 + 150])
		pygame.display.update()

	def main(self):
		pygame.init()
		clock = pygame.time.Clock()
		fonte_arquivo = fonts_dir + "FreeSansBold.ttf"
		self.fonte1 = pygame.font.Font(fonte_arquivo, 30)
		self.fonte2 = pygame.font.Font(fonte_arquivo, 27)
		self.fonte3 = pygame.font.Font(fonte_arquivo, 60)

		self.tela = pygame.display.set_mode(size)
		self.tela.fill([0, 64, 0])

		self.truco.nova_partida(["a", "b", "c", "d"])
		self.jogadores = self.truco.partidas[self.ultima_partida()].equipes[0].jogadores + self.truco.partidas[self.ultima_partida()].equipes[1].jogadores
		self.ordem_jogadores = [self.jogadores[0], self.jogadores[3], self.jogadores[1], self.jogadores[2]]
		self.primeiro_jogador = self.ordem_jogadores[0]
		self.jogador = self.ordem_jogadores[0]
		self.humano = self.jogadores[0]
		self.inicio()
		
		while 1:
			
			tecla = pygame.key.get_pressed()
			
			if self.nos >= 12 or self.eles >= 12:
				self.tela.fill([0, 64, 0])
				if self.nos >= 12:
					self.tela.blit(self.fonte3.render("Sua equipe GANHOU!", 1, (255, 0, 0)), [80, 150])
					self.tela.blit(self.fonte3.render("Parabéns!!!", 1, (255, 0, 0)), [230, 250])
				else:
					self.tela.blit(self.fonte3.render("Sua equipe Perdeu! :(", 1, (255, 0, 0)), [80, 250])
				pygame.display.update()
				pygame.time.delay(5000)
				self.nos = 0
				self.eles = 0
				self.truco.nova_partida(["a", "b", "c", "d"])
				self.inicio()
			else:
				if len(self.mesa) == 4:
					self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].rodadas[-1].definir_ganhador([self.truco.partidas[self.ultima_partida()].equipes[0], self.truco.partidas[self.ultima_partida()].equipes[1]])
					if self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].rodadas[-1].ganhador != "":
						for jogador in self.jogadores:
							if jogador.nome == self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].rodadas[-1].ganhador:
								self.jogador = jogador
								carta = self.mesa[self.ordem_jogadores.index(jogador)]
								self.tela.blit(pygame.transform.scale(carta.imagem, (int(carta.imagem.get_width() * 1.12), int(carta.imagem.get_height() * 1.12))), carta.posicao)
								pygame.display.update()
					else:			
						self.jogador = self.ordem_jogadores[0]

					vencedor = 0
					if len(self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].rodadas) > 1:
						self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].definir_ganhador()
						vencedor = self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].equipe_ganhadora
						if vencedor != 0:
							if vencedor == 1:
								self.nos += 1
							else:
								self.eles += 1
							if self.ordem_jogadores.index(self.primeiro_jogador) < 3:
								self.jogador = self.ordem_jogadores[self.ordem_jogadores.index(self.primeiro_jogador)+1]
								self.primeiro_jogador = self.jogador
							else:
								self.jogador = self.ordem_jogadores[0]
								self.primeiro_jogador = self.jogador
							self.nova_mao()
					
					pygame.time.delay(2000)
					self.ordenar_jogadores()
					if len(self.truco.partidas[self.ultima_partida()].maos[self.ultima_mao()].rodadas) < 3 and vencedor == 0:
						self.nova_radada()

				if self.jogador.nome != self.humano.nome:
					pygame.time.delay(1000)
					self.jogada(self.jogador)	


			for event in pygame.event.get():
				if event.type == QUIT: 
					exit()
				elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
					if self.jogador.nome == self.humano.nome:
						self.ler_entrada(tecla)

			pygame.display.update()
			clock.tick(20)