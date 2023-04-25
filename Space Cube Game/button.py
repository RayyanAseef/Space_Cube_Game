
# Importing Required Libraries
import pygame

# Defining method to draw text at the center of given locations
def TextBlitCenter( surface, text, width, height ):

    text_rect = text.get_rect( center = ( width, height ) )
    surface.blit( text, text_rect )

# Creating button class
class Button:

    # Setting the required parameters
    def __init__( self, name, xPos, yPos, width, height, colourOff, colourOn ):
        
        self.colourOff = colourOff
        self.colourOn = colourOn
        self.buttonRect = pygame.Rect( xPos, yPos, width, height )

        self.pressed = False
        self.on = False

        # Creating font for the text on the buttons
        # Making sure that the text font will fit in the button
        font = pygame.font.SysFont( "arial", (int)(self.findFontSize( name, width, height-10 )) )
        self.text = font.render( name, 1, ( 255, 255, 255 ) )

    # Finding the perfect size for the button using recursion
    def findFontSize( self, text, width, maxSize ):

        # Definfing a minimum size for text as 5
        minSize = 5
        if maxSize <= minSize: return minSize

        # Creating the text with the given size and checking its size
        testFont = pygame.font.SysFont( "arial", (int)(maxSize) )
        textSpace = testFont.size(text)[0]

        # Checking how much space the texts takes for the given size
        # If the size fits it i will return the size or else it will use this function again with a smaller size
        if textSpace < width-10: return maxSize
        else: return self.findFontSize( text, width, maxSize-1 )

    # Drawing the bullet on the screen
    def draw( self, surface ):

        # Checking where the mouse is
        self.checkMouseOn( )

        # Changing the colour depending on if the mouse is above or away from the button
        if self.on: colour = self.colourOn
        elif self.on == False: colour = self.colourOff

        # Drawing the base rectangle
        surface.fill( colour, self.buttonRect )

        # Drawing the outlines of the rectangle
        pygame.draw.line( surface, ( 255, 255, 255 ), self.buttonRect.topleft, self.buttonRect.bottomleft, 5 )
        pygame.draw.line( surface, ( 255, 255, 255 ), self.buttonRect.bottomleft, self.buttonRect.bottomright, 5 )
        pygame.draw.line( surface, ( 255, 255, 255 ), self.buttonRect.bottomright, self.buttonRect.topright, 5 )
        pygame.draw.line( surface, ( 255, 255, 255 ), self.buttonRect.topright, self.buttonRect.topleft, 5 )

        # Drawing the text
        TextBlitCenter( surface, self.text, self.buttonRect.centerx, self.buttonRect.centery )

    # Checking where the mouse is
    def checkMouseOn( self ):

        # Getting mouse position
        mousePos = pygame.mouse.get_pos()

        # Determing whether or not the mouse is above the button
        if self.buttonRect.collidepoint( mousePos ): self.on = True
        else: self.on = False

        
