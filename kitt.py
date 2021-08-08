#!/usr/bin/python3.6
import pygame
pygame.init()
pygame.display.set_caption("KITT")

#setup
step=15
lucesQty=8
lightsOn=[(0x88,0,0),(0xCC,0,0),(0xFF,0,0)]
square={
	"width":50,
	"height":30
}


# and go...
pantalla = pygame.display.set_mode((
	(square["width"]+step)*lucesQty+step,
	square["height"]+step*2
))

# inicializa luces
luces = []
for i in range(len(lightsOn)):
	luces.append({"x":step+(square["width"]+step)*i, "color":lightsOn[i], "dir":"ltr"})

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
			if luces[luz]["x"] > (square["width"]+step)*(lucesQty-1):
				luces[luz]["dir"]="rtl"
			else:
				luces[luz]["x"]=luces[luz]["x"]+square["width"]+step
		if luces[luz]["dir"]=="rtl":
			if luces[luz]["x"]<square["width"]+step:
				luces[luz]["dir"]="ltr"
				luces[luz]["x"]=luces[luz]["x"]+square["width"]+step
			else:
				luces[luz]["x"]=luces[luz]["x"]-square["width"]-step

	# Dibujo
	pantalla.fill((0,0,0))
	for luz in range(len(luces)):
		pygame.draw.rect(pantalla, luces[luz]["color"], [
			luces[luz]["x"], step, square["width"], square["height"]
		])
	pygame.display.flip()
	reloj.tick(8)
