
import turtle
class player(turtle):
	def _init_(self,canvas,x,y,dx,dy,health,mana,weapon,shape):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.health=health
		self.mana=mana
		self.weapon=weapon
		self.dx = dx
        self.dy = dy
		self.shape("player")



	def use_mana(self):
		if mana_power>mana_cost use_mana
		else print"not enof mana"

	
	def weapon(self):
		if  weapon.show():#show inside weapon should return the status of showing and hiding
			weapon.hide()

		else:
			weapon.show()

	def gethit (self):
		self.health-10

	def moveup (self):
		x = self.xcor() 
        y = self.ycor()
		 
		x= x
		y= self.dy+y

		self.goto(x,y)

	def movedown (self):
		x = self.xcor() 
        y = self.ycor()
		 
		x= x
		y= self.dy-y

		self.goto(x,y)

	def moveright (self):
		x = self.xcor() 
        y = self.ycor()
		
		x= x+self.dx
		y= y
		self.goto(x,y)

	def moveleft (self):
		x = self.xcor() 
        y = self.ycor()
		
		x= x-self.dx
		y= y
		self.goto(x,y)


turtle.mainloop()