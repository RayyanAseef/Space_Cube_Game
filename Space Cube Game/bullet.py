
# Importing Required Libraries
import pygame

# Creating Bullet Class
class Bullet:

    # Defining inputs for object
    def __init__( self, characterType, bulletType, bulletSpeed, bulletDamage, xPos, yPos, width, height ):

        # Setting variable values
        self.characterType = characterType
        
        if bulletType == "normal": self.bulletColour = ( 255, 255, 0 )
        if bulletType == "bomb": self.bulletColour = ( 255, 0, 0 )

        self.bulletSpeed = bulletSpeed
        self.bulletDamage = bulletDamage
            
        self.bulletRect = pygame.Rect( xPos, yPos, width, height )

    # Drawing bullet on window
    def draw( self, surface ):

        pygame.draw.rect( surface, self.bulletColour, self.bulletRect )

        bulletBorderColour = ( 255, 255, 255 )
        
        pygame.draw.line( surface, bulletBorderColour, self.bulletRect.topleft, self.bulletRect.bottomleft, 5 )
        pygame.draw.line( surface, bulletBorderColour, self.bulletRect.bottomleft, self.bulletRect.bottomright, 5 )
        pygame.draw.line( surface, bulletBorderColour, self.bulletRect.bottomright, self.bulletRect.topright, 5 )
        pygame.draw.line( surface, bulletBorderColour, self.bulletRect.topright, self.bulletRect.topleft, 5 )

    # Moving bullet
    def move( self ):

        if self.characterType == "Player": self.bulletRect.x += self.bulletSpeed
        if self.characterType == "Enemy": self.bulletRect.x -= self.bulletSpeed
