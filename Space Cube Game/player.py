
# Importing Required Libraries
import pygame
import bullet
import character

# Creating Player Class
class Player(character.Character):

    # Defining inputs for object
    def __init__( self, xPos, yPos, width, height ):

        # Setting variable values
        self.colour = ( 0, 255, 0 )
        
        self.xPos = xPos
        self.yPos = yPos
        self.playerRect = pygame.Rect( xPos, yPos, width, height )

        self.maxHp = 3
        self.Hp = self.maxHp
        
        self.playerSpeed = 1

        self.bulletSpeed = 1
        self.power = 1
        self.reloadTime = 500

        self.singleShoot = True
        self.doubleShoot = False
        self.tripleShoot = False

    # Drawing player on window
    def draw( self, surface ):

        # Deciding coolour of enemy depending on hp
        if self.maxHp >= self.Hp >= self.maxHp*0.5:
            self.colour = ( (int)(255-((self.Hp - self.maxHp*0.5)/(self.maxHp*0.5))*255), 255, 0 )

        else:
            self.colour = ( 255, (int)(255*(self.Hp/(self.maxHp*0.5))), 0 )

        # Drawing Player
        pygame.draw.rect( surface, self.colour, self.playerRect )

    # Moving player around the screen
    def move( self, axis, direction ):

        # Checking which direction to move and then moving player
        if axis == "y" or axis == "Y":
            self.yPos -= direction*self.playerSpeed
            self.playerRect.y = self.yPos
        elif axis == "x" or axis == "X":
            self.xPos += direction*self.playerSpeed
            self.playerRect.x = self.xPos

    # Shooting Bullet
    def shoot( self ):

        bullets = [ bullet.Bullet( "Player", "bomb", self.bulletSpeed, self.power, self.playerRect.x+self.playerRect.w, self.playerRect.y + self.playerRect.h*(1/3), self.playerRect.w, self.playerRect.h*(1/3) ),
                    bullet.Bullet( "Player", "normal", self.bulletSpeed, self.power, self.playerRect.x-30, self.playerRect.y+self.playerRect.h*(1/3), self.playerRect.w, self.playerRect.h*(1/3) ),
                    bullet.Bullet( "Player", "normal", self.bulletSpeed, self.power, self.playerRect.x-self.playerRect.w-60, self.playerRect.y + self.playerRect.h*(1/3), self.playerRect.w, self.playerRect.h*(1/3) ) ]
        
        # Returning bullet object
        if self.singleShoot:
            return [ bullets[0] ]
        
        elif self.doubleShoot:
            return [ bullets[0], bullets[1] ]

        elif self.tripleShoot:
            return [ bullets[0], bullets[1], bullets[2] ]
        
    # Taking damage
    def takeDamage( self, damageAmount ):

        if damageAmount > self.Hp: damageAmount = self.Hp

        #Reducing hp according to bullet damage
        self.Hp = self.Hp - damageAmount

    # Getting upgrade prices for all upgrades
    def getHpUpgradePrice( self ):

        if self.maxHp == 3: upgradePrice = 50
        elif self.maxHp == 10: upgradePrice = 500
        elif self.maxHp == 50: upgradePrice = 3000
        elif self.maxHp == 150: upgradePrice = 10000
        else: upgradePrice = "Max"

        return upgradePrice

    def getPowerUpgradePrice( self ):

        if self.power == 1: upgradePrice = 50
        elif self.power == 5: upgradePrice = 500
        elif self.power == 15: upgradePrice = 3000
        elif self.power == 50: upgradePrice = 10000
        else: upgradePrice = "Max"

        return upgradePrice

    def getPlayerSpeedUpgradePrice( self ):

        if self.playerSpeed < 1.1: upgradePrice = 50
        elif self.playerSpeed < 1.2: upgradePrice = 500
        elif self.playerSpeed < 1.3: upgradePrice = 3000
        elif self.playerSpeed < 1.4: upgradePrice = 10000
        else: upgradePrice = "Max"

        return upgradePrice

    def getBulletSpeedUpgradePrice( self ):

        if self.bulletSpeed == 1: upgradePrice = 50
        elif self.bulletSpeed == 2: upgradePrice = 500
        elif self.bulletSpeed == 3: upgradePrice = 3000
        elif self.bulletSpeed == 4: upgradePrice = 10000
        else: upgradePrice = "Max"

        return upgradePrice

    def getReloadTimeUpgradePrice( self ):

        if self.reloadTime == 500: upgradePrice = 50
        elif self.reloadTime == 450: upgradePrice = 500
        elif self.reloadTime == 400: upgradePrice = 3000
        elif self.reloadTime == 350: upgradePrice = 10000
        else: upgradePrice = "Max"

        return upgradePrice

    # Upgrading all the types of upgrades if given enough money
    def upgradeHp( self, gameSystem ):

        if self.getHpUpgradePrice( ) == "Max": return gameSystem.money

        hpPercentage = self.Hp/self.maxHp

        if gameSystem.money >= self.getHpUpgradePrice( ):
        
            if self.maxHp == 3:
                gameSystem.money -= self.getHpUpgradePrice( )
                self.maxHp = 10
                
            elif self.maxHp == 10:

                gameSystem.money -= self.getHpUpgradePrice( )
                self.maxHp = 50
                
            elif self.maxHp == 50:

                gameSystem.money -= self.getHpUpgradePrice( )
                self.maxHp = 150
                
            elif self.maxHp == 150:

                gameSystem.money -= self.getHpUpgradePrice( )
                self.maxHp = 450
            
        self.Hp = self.maxHp*hpPercentage
            
    def upgradePower( self, gameSystem ):

        if self.getPowerUpgradePrice( ) == "Max": return gameSystem.money

        if gameSystem.money >= self.getPowerUpgradePrice( ):
        
            if self.power == 1:

                gameSystem.money -= self.getPowerUpgradePrice( )
                self.power = 5
                
            elif self.power == 5:

                gameSystem.money -= self.getPowerUpgradePrice( )
                self.power = 15
                
            elif self.power == 15:

                gameSystem.money -= self.getPowerUpgradePrice( )
                self.power = 50
                
            elif self.power == 50:

                gameSystem.money -= self.getPowerUpgradePrice( )
                self.power = 150

    def upgradePlayerSpeed( self, gameSystem ):

        if self.getPlayerSpeedUpgradePrice( ) == "Max": return gameSystem.money

        if self.playerSpeed < 1.4 and gameSystem.money >= self.getPlayerSpeedUpgradePrice( ):

            gameSystem.money -= self.getPlayerSpeedUpgradePrice( )
            self.playerSpeed += 0.1

    def upgradeBulletSpeed( self, gameSystem ):

        if self.getBulletSpeedUpgradePrice( ) == "Max": return gameSystem.money

        if self.bulletSpeed < 6 and gameSystem.money >= self.getBulletSpeedUpgradePrice( ):

            gameSystem.money -= self.getBulletSpeedUpgradePrice( )
            self.bulletSpeed += 1

    def upgradeReloadTime( self, gameSystem ):

        if self.getReloadTimeUpgradePrice( ) == "Max": return gameSystem.money

        if self.reloadTime > 300 and gameSystem.money >= self.getReloadTimeUpgradePrice( ):

            gameSystem.money -= self.getReloadTimeUpgradePrice( )
            self.reloadTime -= 50










        
