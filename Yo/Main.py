from turtle import *
import random
import math
import tkinter
import tkinter.messagebox

from Player import Player
from Weapon import Weapon
from Enemy import Enemy

waveFinished = True
deadEnemys = 0
enemyList = []
wave = 0

def main():
	global waveFinished
	global deadEnemys
	global enemyList
	global wave

	root = tkinter.Tk()
	root.title("LittleMeeter")
	cv = ScrolledCanvas(root,600,600,600,600)
	cv.pack(side = tkinter.LEFT)
	t = RawTurtle(cv)
	screen = t.getscreen()
	screen.setworldcoordinates(0,0,500,500)

	if wave == 0:
		player = Player(100,100,1,cv,250,250)
		wave = 1

	if waveFinished :
		for a in range(5*wave) :
			del enemyList
			enemyList = []
			enemyList.append(Enemy(cv,400,50*(a+1)))
			enemyList[a].artificialIntelegence(player)
			
		waveFinished = False 

	

	screen.onkeypress(player.goUp,"Up")
	screen.onkeypress(player.goDown,"Down")
	screen.onkeypress(player.goRight,"Right")
	screen.onkeypress(player.goLeft,"Left")
	screen.onkeypress(player.attack,"a")

	screen.listen()
	tkinter.mainloop()

if __name__ == "__main__":
    main()