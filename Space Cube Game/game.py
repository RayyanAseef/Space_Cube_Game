
# Importing Required Libraries
import pygame
import player
import bullet
import enemy

# Intializing Pygame
pygame.init( )

# Creating colour variables
white = ( 255, 255, 255 )
black = ( 0, 0, 0 )
red = ( 255, 0, 0 )
yellow = ( 255, 255, 0 )

# Defining method to draw text at the center of given locations
def TextBlitCenter( surface, text, xPos, yPos ):

    text_rect = text.get_rect( center = ( xPos, yPos ) )
    surface.blit( text, text_rect )

# Creating Game Class
class Game:
    
    # Defining inputs for object
    def __init__( self, width, height, gameOpen ):

        # Getting Window Widgh and Height
        self.width = width
        self.height = height

        # Checking if Game is starting On or Off
        self.gameOpen = gameOpen

        self.money = 0
        self.font = pygame.font.SysFont( "arial", 25 )

        # Setting player varaibles
        self.playerObject = player.Player( 0, 0, min(width, height)/22.5, min(width, height)/22.5 )
        self.playerSpace = self.width*0.30

        # Setting Enemy List
        self.enemyObjects = [ enemy.Enemy( "Easy", 500, 100, width, height ),
                 enemy.Enemy( "Medium", 500, 200, width, height ),
                 enemy.Enemy( "Hard", 500, 300, width, height ),
                 enemy.Enemy( "Very Hard", 500, 400, width, height ),
                 enemy.Enemy( "Impossible", 500, 500, width, height ) ]

        # Setting bullet variables
        self.bullets = []
        self.Shot = False
        self.shootWaitedTime = 0

    # This runs the game system by drawing everything on the screen
    # and checking for key inputs
    def run( self, surface ):

        if self.gameOpen:
            
            self.drawBrackground( surface )

            self.playerUpdate( surface )
            self.enemyUpdate( surface )
            self.bulletUpdate( surface )

        else:

            surface.fill( black )
            self.text = self.font.render( f"Money: {self.money}", 1, ( 255, 255, 255 ) )
            TextBlitCenter( surface, self.text, self.width*(4/5), 15 )

    # This drawsthe backgorund, player, enemies and bullets onto the screen
    def drawBrackground( self, surface ):

        # Drawing background
        surface.fill( black )
        pygame.draw.line( surface, white, ( self.playerSpace , 0), ( self.playerSpace , self.height ), 4 )

        self.text = self.font.render( f"Money: {self.money}", 1, ( 255, 255, 255 ) )
        TextBlitCenter( surface, self.text, self.width*(4/5), 15 )
        
    def playerUpdate( self, surface ):

        self.playerObject.draw( surface )

        # Checking for key inputs
        key = pygame.key.get_pressed()

        # Performing actions depending on key pressed
        if key[pygame.K_UP] and self.playerObject.playerRect.y > 0:
            self.playerObject.move( "y", 1 )
        if key[pygame.K_DOWN] and self.playerObject.playerRect.y < self.height - self.playerObject.playerRect.h:
            self.playerObject.move( "y", -1 )
        if key[pygame.K_RIGHT] and self.playerObject.playerRect.x < self.playerSpace - self.playerObject.playerRect.w:
            self.playerObject.move( "x", 1 )
        if key[pygame.K_LEFT] and self.playerObject.playerRect.x > 0:
            self.playerObject.move( "x", -1 )

        if key[pygame.K_SPACE] and self.Shot == False:

            newBullets = self.playerObject.shoot( )
            
            self.bullets.append( newBullets[0] )
            if self.playerObject.doubleShoot or self.playerObject.tripleShoot: self.bullets.append( newBullets[1] )
            if self.playerObject.tripleShoot: self.bullets.append( newBullets[2] )
            
            self.Shot = True

        # Toggling shoot to false after 500 frames so player can shoot again
        if self.Shot == True: self.shootWaitedTime += 1
        if self.shootWaitedTime >= self.playerObject.reloadTime:
            self.Shot = False
            self.shootWaitedTime = 0

    def enemyUpdate( self, surface ):

        # Goes through the enemy List to auto shoot or check if they are dead
        for enemyObject in self.enemyObjects:

            # If enemy isnt lowest type, when it dies it changes it type to
            # be one step weaker. If it is the weakest is dies completly
            if enemyObject.Hp <= 0:
                
                if enemyObject.enemyType == "Impossible":

                    enemyObject.changeType( "Very Hard" )
                    self.money += 1000
                    
                elif enemyObject.enemyType == "Very Hard":

                    enemyObject.changeType( "Hard" )
                    self.money += 300
                    
                elif enemyObject.enemyType == "Hard":

                    enemyObject.changeType( "Medium" )
                    self.money += 100
                    
                elif enemyObject.enemyType == "Medium":

                    enemyObject.changeType( "Easy" )
                    self.money += 50
                    
                elif enemyObject.enemyType == "Easy":

                    self.enemyObjects.remove( enemyObject )
                    self.money += 10

            else:

                enemyObject.draw( surface )
                
                # Enemy automatically shoots every interval
                enemyShoot = enemyObject.shoot( )
                if enemyShoot != None: self.bullets.append( enemyShoot )

    def bulletUpdate( self, surface ):

        # Gets list of all enemy rects
        enemyRectList = [ enemyObject.enemyRect for enemyObject in self.enemyObjects ]

        # Goes through the bullet List to move them and check for collision
        for Bullet in self.bullets:
            
            # Removing bullets outside the screen
            if Bullet.bulletRect.x > self.width: self.bullets.remove( Bullet )

            # Damaging Enemy or Player if come in contact
            if Bullet.bulletRect.colliderect( self.playerObject.playerRect ) and Bullet.characterType == "Enemy":
                self.playerObject.takeDamage( Bullet.bulletDamage )
                self.bullets.remove( Bullet )
            if Bullet.bulletRect.collidelist( enemyRectList ) != -1 and Bullet.characterType == "Player":
                self.enemyObjects[Bullet.bulletRect.collidelist( enemyRectList )].takeDamage( Bullet.bulletDamage )
                self.bullets.remove( Bullet )

            if not ( Bullet.characterType == "Player" and Bullet.bulletRect.x < self.playerObject.playerRect.x ): Bullet.draw( surface )

            Bullet.move( )

    def reset( self ):

        # Setting player varaibles
        self.playerObject = player.Player( 0, 0, self.playerObject.playerRect.w, self.playerObject.playerRect.h )

        # Setting Enemy List
        self.enemyObjects = [ enemy.Enemy( "Easy", 500, 100, self.width, self.height ),
                 enemy.Enemy( "Medium", 500, 200, self.width, self.height ),
                 enemy.Enemy( "Hard", 500, 300, self.width, self.height ),
                 enemy.Enemy( "Very Hard", 500, 400, self.width, self.height ),
                 enemy.Enemy( "Impossible", 500, 500, self.width, self.height ) ]

        # Setting bullet variables
        self.bullets = []
        self.Shot = False
        self.shootWaitedTime = 0

    # Toggling menu on and off
    def open( self ): self.gameOpen = True
    def close( self ): self.gameOpen = False
                
            
