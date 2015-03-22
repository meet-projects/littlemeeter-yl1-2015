
import turtle
class player(turtle):
	def __init__(self,canvas,x,y,dx,dy,health,mana,weapon,shape):
		RawTurtle.__init__(self,canvas)
		self.penup()
		self.goto(x,y)
		self.health=health
		self.mana=mana
		self.weapon=weapon
		self.dx = dx
        self.dy = dy
        self.current_mana = max_mana
		self.shape("player")



	def use_mana(self):
		if ((self.current_mana - weapon.get_mana_use()) > 0):
			

		else: 

			print("not enough mana")

	
	def change_weapon_status(self):
		if (weapon.status()):#show inside weapon should return the status of showing and hiding
			
			weapon.hide()

		else:
			weapon.show()

	def get_hit (self,damage):
		self.health = self.health-damage

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


turtle.mainloop()