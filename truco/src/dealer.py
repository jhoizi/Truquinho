import pygame
from pygame.locals import *
from baralho import *
import random
from configs import posicoes_cartas

class Dealer:

	nome = ""
	baralho = ""
	
	def __init__(self, nome):
		self.nome = nome

	def entregar_cartas(self, jogadores, mao):
		self.baralho = Baralho()
		cartas_entregues = {1 : [], 2 : [], 3 : [], 4: []}
		manilha = ""
		j = 0
		for i in range(0, 13):
			if(j == 4):
				j = 0

			naipe_valor = -1
			carta_valor = -1
			presente = True
			
			while(presente):
				naipe_valor = random.randint(1, 4)
				carta_valor = random.randint(0, 9)
				
				if cartas_entregues[naipe_valor].count(carta_valor) == 0 and i != 12:
					cartas_entregues[naipe_valor].append(carta_valor)
					presente = False
					carta = self.baralho.truco[self.baralho.naipes[naipe_valor - 1]][carta_valor]
					jogadores[j].receber_carta(carta)
					#print("Naipe: " , naipe_valor , "; carta: " , carta_valor , " - " , carta.valor_str)
			
				elif cartas_entregues[naipe_valor].count(carta_valor) == 0 and i == 12:
					manilha = self.baralho.truco[self.baralho.naipes[naipe_valor - 1]][carta_valor]
					manilha.imagem = pygame.transform.rotate(manilha.imagem, 90)
					presente = False		

			j += 1

		mao.definir_manilha(manilha)
		self.valorizar_manilhas(manilha)
		self.posicoes(jogadores)

	def valorizar_manilhas(self, manilha):
		chaves = self.baralho.naipes
		vira_index = manilha.valor - 1
		if vira_index != 9:
			manilha_index = vira_index + 1
		else: 
			manilha_index = 0

		v = 13
		for naipe in chaves:
			self.baralho.truco[naipe][manilha_index].valor += v
			v -= 1
		


	def posicoes(self, jogadores):
		a = 0
		for jogador in jogadores:
			for carta in jogador.mao:
				carta.posicao.left = posicoes_cartas[a][0]
				carta.posicao.top = posicoes_cartas[a][1]
				a += 1	