#!/usr/bin/python3.6
from kitt import Kitt
kitt=Kitt()
kitt.clock_tick=100
kitt.step=1
kitt.lucesQty=50
kitt.lightsOn=[
	(0x11,0,0),(0x22,0,0),(0x33,0,0),(0x44,0,0),(0x55,0,0),
	(0x66,0,0),(0x77,0,0),(0x88,0,0),(0x99,0,0),(0xaa,0,0),
	(0xbb,0,0),(0xCC,0,0),(0xdd,0,0),(0xee,0,0),(0xFF,0,0)
]
kitt.square["width"]=10
kitt.square["height"]=60
kitt.run()
