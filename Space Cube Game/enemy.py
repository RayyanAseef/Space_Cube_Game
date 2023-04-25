
# Importing Required Libraries
import pygame
import bullet
import character

# Creating Enemy Class
class Enemy(character.Character):

    def settingBaseValues( self, xPos, yPos ):

        # Setting enemy variable values depending on enemy type
        if self.enemyType == "Easy":
            
            self.maxHp = 3
            self.Hp = self.maxHp
            
            self.power = 1
            
            self.bulletSpeed = 1
            self.reloadTime = 500
            
            self.Shot = False
            self.shootWaitedTime = 0
            
            self.enemyRect = pygame.Rect( xPos, yPos, min(self.width, self.height)/36, min(self.width, self.height)/36 )

        elif self.enemyType == "Medium":
            
            self.maxHp = 10
            self.Hp = self.maxHp
            
            self.power = 5
            
            self.bulletSpeed = 2
            self.reloadTime = 400

            self.Shot = False
            self.shootWaitedTime = 0
            
            self.enemyRect = pygame.Rect( xPos, yPos, min(self.width, self.height)/30, min(self.width, self.height)/30 )

        elif self.enemyType == "Hard":
            
            self.maxHp = 50
            self.Hp = self.maxHp
            
            self.power = 15
            
            self.bulletSpeed = 5
            self.reloadTime = 300

            self.Shot = False
            self.shootWaitedTime = 0
            
            self.enemyRect = pygame.Rect( xPos, yPos, min(self.width, self.height)/22.5, min(self.width, self.height)/22.5 )
        
        elif self.enemyType == "Very Hard":
            
            self.maxHp = 150
            self.Hp = self.maxHp
            
            self.power = 50
            
            self.bulletSpeed = 5
            self.reloadTime = 200

            self.Shot = False
            self.shootWaitedTime = 0
            
            self.enemyRect = pygame.Rect( xPos, yPos, min(self.width, self.height)/18, min(self.width, self.height)/18 )

        elif self.enemyType == "Impossible":
            
            self.maxHp = 500
            self.Hp = self.maxHp
            
            self.power = 100
            
            self.bulletSpeed = 5
            self.reloadTime = 200

            self.Shot = False
            self.shootWaitedTime = 0

            self.enemyRect = pygame.Rect( xPos, yPos, min(self.width, self.height)/15, min(self.width, self.height)/15 )

    # Defining inputs for object
    def __init__( self, enemyType, xPos, yPos, width, height ):

        self.width = width
        self.height = height

        # Setting varaibles that are global to all enemy types
        self.colour = ( 0, 255, 0 )
        self.enemyType = enemyType

        # Setting enemy variable values depending on enemy type
        self.settingBaseValues( xPos, yPos )

    # Drawing player on window
    def draw( self, surface ):

        # Deciding colour of enemy depending on hp
        if self.maxHp >= self.Hp >= self.maxHp*0.5:
            self.colour = ( (int)(255-((self.Hp - self.maxHp*0.5)/(self.maxHp*0.5))*255), 255, 0 )

        else:
            self.colour = ( 255, (int)(255*(self.Hp/(self.maxHp*0.5))), 0 )

        # Drawing Enemy 
        pygame.draw.rect( surface, self.colour, self.enemyRect )

    # Shooting Bullet Automatically
    def shoot( self ):

        if self.Shot == True: self.shootWaitedTime += 1
        if self.shootWaitedTime >= self.reloadTime:
            self.Shot = False
            self.shootWaitedTime = 0
        if self.Shot == False:
            self.Shot = True
            return bullet.Bullet( "Enemy", "normal", self.bulletSpeed, self.power, self.enemyRect.x-self.enemyRect.w, self.enemyRect.y + self.enemyRect.h*(1/3), self.enemyRect.w, self.enemyRect.h*(1/3) )

        return None

    # Taking damage
    def takeDamage( self, damageAmount ):

        if damageAmount > self.Hp: damageAmount = self.Hp

        #Reducing hp according to bullet damage
        self.Hp = self.Hp - damageAmount

    def changeType( self, newType ):

        # Setting enemy type as new enemy type
        self.enemyType = newType
        self.settingBaseValues( self.enemyRect.x, self.enemyRect.y )
        
    
