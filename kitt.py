#!/usr/bin/python3.6
import pygame
class Kitt(object):
	"""docstring for Kitt."""

	def __init__(self):
		self.clock_tick = 20
		self.step = 10
		self.lucesQty = 8
		self.lightsOn = [(0x88,0,0),(0xCC,0,0),(0xFF,0,0)]
		self.square={
			"width": 30,
			"height": 20
		}

	def addLight(self,color):
		self.lightsOn.append(color)

	def run(self):
		pygame.init()
		pygame.display.set_caption("KITT")

		pantalla = pygame.display.set_mode((
			(self.square["width"]+self.step) * self.lucesQty + self.step,
			self.square["height"] + self.step * 2
		))

		# inicializa luces
		luces = []
		for i in range(len(self.lightsOn)):
			luces.append({
				"x": self.step+(self.square["width"] + self.step)*i,
				"color":self.lightsOn[i],
				"dir":"ltr"
			})

		termina = False
		reloj = pygame.time.Clock()
		while not termina:
			# Eventos
			for evento in pygame.event.get():
				if evento.type == pygame.QUIT:
					termina = True

			# Logica
			for luz in range(len(luces)):
				if luces[luz]["dir"]=="ltr":
					if luces[luz]["x"] > (self.square["width"] + self.step)*(self.lucesQty-1):
						luces[luz]["dir"]="rtl"
					else:
						luces[luz]["x"]=luces[luz]["x"]+self.square["width"]+self.step
				if luces[luz]["dir"]=="rtl":
					if luces[luz]["x"]<self.square["width"]+self.step:
						luces[luz]["dir"]="ltr"
						luces[luz]["x"]=luces[luz]["x"]+self.square["width"]+self.step
					else:
						luces[luz]["x"]=luces[luz]["x"]-self.square["width"]-self.step

			# Dibujo
			pantalla.fill((0,0,0))
			for luz in range(len(luces)):
				pygame.draw.rect(pantalla, luces[luz]["color"], [
					luces[luz]["x"], self.step, self.square["width"], self.square["height"]
				])
			pygame.display.flip()
			reloj.tick(self.clock_tick)
