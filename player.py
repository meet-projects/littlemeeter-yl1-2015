
from turtle import *
class player(Turtle):
	def __init__(self,canvas,x,y,dx,dy,health,mana,weapon,shape):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.health=health
		self.weapon=weapon
		self.dx=dx
		self.dy=dy
		self.current_mana=max_mana
		self.shape("player")



	def mana_status(self):
		if self.current_mana() >= weapon.mana_use():
			return True

	def player_damage(self,enemy):
		x= self.xcor()
		y=self.ycor()

		if self.ycor ()==weapon.ycor() and weapon.xcor()==self.xcor():
			self.health = self.health-damage

	
	def change_weapon_status(self):
		if weapon.status():#show inside weapon should return the status of showing and hiding
			
			weapon.hide()

		else:
			weapon.show()

		

	def move_up (self):
		x = self.xcor() 
		y = self.ycor()
		 
		y = self.dy+y

		self.goto(x,y)

	def move_down (self):
		x = self.xcor() 
		y = self.ycor()
		 
		x= x
		y= y-self.dy

		self.goto(x,y)

	def move_right (self):
		x = self.xcor()
		y = self.ycor()
		
		x= x+self.dx
		self.goto(x,y)

	def move_left (self):
		x = self.xcor() 
		y = self.ycor()
		
		x= x-self.dx
		y= y
		
		self.goto(x,y)

	screen.getscreen(self).onkeypress(move_up, Up)

	screen.getscreen(self).onkeypress(move_down, Down)

	screen.getscreen(self).onkeypress(move_right, Right)
	
	screen.getscreen(self).onkeypress(move_left, Left)



from turtle import *

class weapon(Turtle):
	def __init__(self,canvas,x,y,dz,dy,shape,damage,mana_cost,mana_use):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.status_bool = False
		self.goto(x,y)
		self.damage=damage
		self.mana_cost=mana_cost
		self.dx = dx
		self.dy = dy
		self.mana_use = mana_use
		self.shape("weapon")

	def enemyisinrange(self,enemy):
		x=self.xcor()
		y=self.ycor()

		if self.ycor()==enemy.ycor() and enemy.xcor()==self.xcor():
			return True
	
		
	def get_mana_use(self):

		return self.mana_use
		


	def show(self):
		self.showturtle()
		self.status_bool = True

	def status(self):
		return self.status_bool


	def hide(self):
		self.hideturtle()
		self.status_bool=False


	def shoot(self):
		if mana_status()==True:
			for x in range(0,800,1):
				x= self.xcor()
				y=self.ycor()
				self.goto (x,y)
		else:
			print("not enof mama")	
	

	def return_weapon (self,player):
		if enemyisinrange== True:
			hide() 
			self.goto(player.xcor(),player.ycor())
#make sure

	screen.getscreen(self).onkeypress(shoot, Space)
	screen.getscreen(self).onkeypress(change_weapon_status, Space)

turtle.mainloop()