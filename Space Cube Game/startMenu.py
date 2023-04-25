
# Importing Required Libraries
import pygame
import button

# Defining colours
black = ( 0, 0, 0 )

blue = ( 0, 0, 255 )
green = ( 0, 255, 0 )

red = ( 255, 0, 0 )
orange = ( 255, 165, 0 )

# Defining method to draw text at the center of given locations
def TextBlitCenter( surface, text, xPos, yPos ):

    text_rect = text.get_rect( center = ( xPos, yPos ) )
    surface.blit( text, text_rect )

# Creating starting menu class
class StartMenu:

    # Setting the required parameters
    def __init__( self, text, width, height, menuOpen ):

        self.width = width
        self.height = height

        self.menuOpen = menuOpen

        self.startButton = button.Button( "Start", width*(1/5), height*(4/7), width/5, height/4, blue, green )
        self.endButton = button.Button( "Quit", width*(3/5), height*(4/7), width/5, height/4, red, orange )

        # Creating font for the title
        wantedWidth = (self.endButton.buttonRect.x+self.endButton.buttonRect.w) - self.startButton.buttonRect.x + width/5
        maxSize = (self.height/7)*5 - 10
        font = pygame.font.SysFont( "arial", (int)(self.findFontSize( text, wantedWidth, maxSize )) )
        self.text = font.render( text, 1, ( 255, 255, 255 ) )

    # Finding the perfect size for the title using recursion
    def findFontSize( self, text, wantedWidth, maxSize ):

        # Definfing a minimum size for text as 5
        minSize = 5
        if maxSize <= minSize: return minSize

        # Creating the text with the given size and checking its size
        testFont = pygame.font.SysFont( "arial", (int)(maxSize) )
        textSpace = testFont.size(text)[0]

        # Checking how much space the texts takes for the given size
        # If the size fits it i will return the size or else it will use this function again with a smaller size
        if textSpace < wantedWidth: return maxSize
        else: return self.findFontSize( text, wantedWidth, maxSize-1 )

    # Running the menu
    def run( self, surface, gameSystem ):

        # Running the menu if open
        if self.menuOpen:
            
            surface.fill( black )
            TextBlitCenter( surface, self.text, self.width/2, self.height*(2/7) )

            self.updateButtons( surface, gameSystem )

    # Updating what the buttons are doing
    def updateButtons( self, surface, gameSystem ):

        self.startButton.draw( surface )
        self.endButton.draw( surface )
        
        # Defining what start button does
        if self.startButton.pressed:
            self.startButton.pressed = False
            gameSystem.open( )
            self.close( )

        # Defining what end button does
        if self.endButton.pressed:
            self.endButton.pressed = False
            pygame.quit( )
            exit( )

    # Having methods to toggle the start menu on and off
    def open( self ): self.menuOpen = True
    def close( self ): self.menuOpen = False
