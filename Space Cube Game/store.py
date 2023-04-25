
# Importing pygame
import pygame
import button

# Defining Colours
blue = ( 0, 150, 255 )
lightBlue = ( 0, 255, 255 )

purple = ( 153, 50, 204 )

# Defining method to draw text at the center of given locations
def TextBlitCenter( surface, text, xPos, yPos ):

    text_rect = text.get_rect( center = ( xPos, yPos ) )
    surface.blit( text, text_rect )

# Creating Store Class
class Store:

    # Defining inputs for object
    def __init__( self, text, xPos, yPos, width, height, menuOpen ):

        self.menuRect = pygame.Rect( xPos, yPos, width, height )
        self.menuOpen = menuOpen

        self.str = text
        font = pygame.font.SysFont( "arial", 35 )
        self.text = font.render( self.str, 1, ( 0, 0, 0 ) )

        # Creating Stores and buttons depending on type of store
        if self.str == "Store":

            self.upgradesButton = button.Button( "Upgrades", xPos+width*(1/7), yPos+50, width/7, 40, blue, lightBlue )
            self.addOnsButton = button.Button( "Add-Ons", xPos+width*(3/7), yPos+50, width/7, 40, blue, lightBlue )
            self.itemsButton = button.Button( "Items", xPos+width*(5/7), yPos+50, width/7, 40, blue, lightBlue )

            self.upgradesStore = Store( "Upgrades", xPos+50, yPos+100, width-100, height-150, True )
            self.addOnsStore = Store( "Add-Ons", xPos+50, yPos+100, width-100, height-150, False )
            self.itemsStore = Store( "Items", xPos+50, yPos+100, width-100, height-150, False )

        if self.str == "Upgrades":

            self.upgradeBulletSpeedButton = button.Button( "Upgrade Bullet Speed", xPos+width*(1/7), yPos+height/3, width/7, height/7, blue, lightBlue )
            self.upgradeBulletPowerButton = button.Button( "Upgrade Bullet Power", xPos+width*(3/7), yPos+height/3, width/7, height/7, blue, lightBlue )
            self.upgradeReloadTimeButton = button.Button( "Upgrade Reload Time", xPos+width*(5/7), yPos+height/3, width/7, height/7, blue, lightBlue )
            
            self.upgradePlayerHpButton = button.Button( "Upgrade Player Hp", xPos+width*(1/5), yPos+height*(2/3), width/5, height/7, blue, lightBlue )
            self.upgradePlayerSpeedButton = button.Button( "Upgrade Player Speed", xPos+width*(3/5), yPos+height*(2/3), width/5, height/7, blue, lightBlue )

        if self.str == "Add-Ons":
            
            self.addDoubleShooterButton = button.Button( "Add Double Shooter", xPos+width*(1/5), yPos+height/3, width/5, height/5, blue, lightBlue )
            self.addTripleShooterButton = button.Button( "Add Tripple Shooter", xPos+width*(3/5), yPos+height/3, width/5, height/5, blue, lightBlue )
            
        if self.str == "Items":

            self.bulletBombButton = button.Button( "Bullet Bomb", xPos+width*(1/5), yPos+height/3, width/5, height/7, blue, lightBlue )
            self.laserBulletButton = button.Button( "Laser Bullet", xPos+width*(3/5), yPos+height/3, width/5, height/7, blue, lightBlue )

            self.shieldButton = button.Button( "Shield", xPos+width*(1/5), yPos+height*(2/3), width/5, height/7, blue, lightBlue )
            self.healsButton = button.Button( "Heals", xPos+width*(3/5), yPos+height*(2/3), width/5, height/7, blue, lightBlue )

    # Running store
    def run( self, surface, gameSystem ):
        
        # If menu if toggled on Drawing menu
        if self.menuOpen:

            self.draw( surface, gameSystem )
            self.updateButtons( surface, gameSystem )

            # Some addition things to draw if it is the orginal store 
            if self.str == "Store":

                self.upgradesStore.run( surface, gameSystem )
                self.addOnsStore.run( surface, gameSystem )
                self.itemsStore.run( surface, gameSystem )
                
    # Drawing Store
    def draw( self, surface, gameSystem ):

        # Drawing the stores depending on what type of store they are along with the objects they have        
        if self.str == "Store": pygame.draw.rect( surface, purple, self.menuRect )
        
        elif self.str == "Upgrades":

            pygame.draw.rect( surface, lightBlue, self.menuRect )

            font = pygame.font.SysFont( "arial", 20 )
            
            tempText = font.render( f"Price: {gameSystem.playerObject.getBulletSpeedUpgradePrice( )}", 1, ( 0, 0, 0 ) )
            TextBlitCenter( surface, tempText, self.upgradeBulletSpeedButton.buttonRect.centerx, self.upgradeBulletSpeedButton.buttonRect.centery+self.upgradeBulletSpeedButton.buttonRect.h )

            tempText = font.render( f"Price: {gameSystem.playerObject.getPowerUpgradePrice( )}", 1, ( 0, 0, 0 ) )
            TextBlitCenter( surface, tempText, self.upgradeBulletPowerButton.buttonRect.centerx, self.upgradeBulletPowerButton.buttonRect.centery+self.upgradeBulletPowerButton.buttonRect.h )

            tempText = font.render( f"Price: {gameSystem.playerObject.getReloadTimeUpgradePrice( )}", 1, ( 0, 0, 0 ) )
            TextBlitCenter( surface, tempText, self.upgradeReloadTimeButton.buttonRect.centerx, self.upgradeReloadTimeButton.buttonRect.centery+self.upgradeReloadTimeButton.buttonRect.h )
                    
            tempText = font.render( f"Price: {gameSystem.playerObject.getHpUpgradePrice( )}", 1, ( 0, 0, 0 ) )
            TextBlitCenter( surface, tempText, self.upgradePlayerHpButton.buttonRect.centerx, self.upgradePlayerHpButton.buttonRect.centery+self.upgradePlayerHpButton.buttonRect.h )

            tempText = font.render( f"Price: {gameSystem.playerObject.getPlayerSpeedUpgradePrice( )}", 1, ( 0, 0, 0 ) )
            TextBlitCenter( surface, tempText, self.upgradePlayerSpeedButton.buttonRect.centerx, self.upgradePlayerSpeedButton.buttonRect.centery+self.upgradePlayerSpeedButton.buttonRect.h )
        
        elif self.str == "Add-Ons":

            pygame.draw.rect( surface, lightBlue, self.menuRect )

            font = pygame.font.SysFont( "arial", 20 )

            if gameSystem.playerObject.doubleShoot == False and gameSystem.playerObject.tripleShoot == False:
                tempText = font.render( f"Price: 50000", 1, ( 0, 0, 0 ) )
            else:
                tempText = font.render( f"Price: Max", 1, ( 0, 0, 0 ) )
                
            TextBlitCenter( surface, tempText, self.addDoubleShooterButton.buttonRect.centerx, self.addDoubleShooterButton.buttonRect.centery+self.addDoubleShooterButton.buttonRect.h )

            if gameSystem.playerObject.tripleShoot == False:
                tempText = font.render( f"Price: 100000", 1, ( 0, 0, 0 ) )
            else:
                tempText = font.render( f"Price: Max", 1, ( 0, 0, 0 ) )
            
            TextBlitCenter( surface, tempText, self.addTripleShooterButton.buttonRect.centerx, self.addTripleShooterButton.buttonRect.centery+self.addTripleShooterButton.buttonRect.h )
        
        elif self.str == "Items":

            pygame.draw.rect( surface, lightBlue, self.menuRect )

        TextBlitCenter( surface, self.text, self.menuRect.centerx, self.menuRect.y+25 )
        
        pygame.draw.line( surface, ( 255, 255, 255 ), self.menuRect.topleft, self.menuRect.bottomleft, 5 )
        pygame.draw.line( surface, ( 255, 255, 255 ), self.menuRect.bottomleft, self.menuRect.bottomright, 5 )
        pygame.draw.line( surface, ( 255, 255, 255 ), self.menuRect.bottomright, self.menuRect.topright, 5 )
        pygame.draw.line( surface, ( 255, 255, 255 ), self.menuRect.topright, self.menuRect.topleft, 5 )
        
    # Checking if any of the buttons for any of the buttons are pressed and proceedign accordingly
    def updateButtons( self, surface, gameSystem ):

        if self.str == "Store":

            self.upgradesButton.draw( surface )
            self.addOnsButton.draw( surface )
            self.itemsButton.draw( surface )
                
            if self.upgradesButton.pressed:
                    
                self.upgradesStore.open( )
                self.itemsStore.close( )
                self.addOnsStore.close( )
                self.upgradesButton.pressed = False

            if self.addOnsButton.pressed:
                    
                self.addOnsStore.open( )
                self.upgradesStore.close( )
                self.itemsStore.close( )
                self.addOnsButton.pressed = False

            if self.itemsButton.pressed:
                
                self.itemsStore.open( )
                self.upgradesStore.close( )
                self.addOnsStore.close( )
                self.itemsButton.pressed = False

        if self.str == "Upgrades":

            self.upgradeBulletSpeedButton.draw( surface )
            self.upgradeBulletPowerButton.draw( surface )
            self.upgradeReloadTimeButton.draw( surface )
            
            self.upgradePlayerSpeedButton.draw( surface )
            self.upgradePlayerHpButton.draw( surface )

            if self.upgradeBulletSpeedButton.pressed:

                gameSystem.playerObject.upgradeBulletSpeed( gameSystem )
                self.upgradeBulletSpeedButton.pressed = False

            if self.upgradeBulletPowerButton.pressed:

                gameSystem.playerObject.upgradePower( gameSystem )
                self.upgradeBulletPowerButton.pressed = False

            if self.upgradePlayerSpeedButton.pressed:

                gameSystem.playerObject.upgradePlayerSpeed( gameSystem )
                self.upgradePlayerSpeedButton.pressed = False

            if self.upgradePlayerHpButton.pressed:

                gameSystem.playerObject.upgradeHp( gameSystem )
                self.upgradePlayerHpButton.pressed = False

            if self.upgradeReloadTimeButton.pressed:

                gameSystem.playerObject.upgradeReloadTime( gameSystem )
                self.upgradeReloadTimeButton.pressed = False

        if self.str == "Add-Ons":
        
            self.addDoubleShooterButton.draw( surface )
            self.addTripleShooterButton.draw( surface )

            if self.addDoubleShooterButton.pressed and gameSystem.playerObject.doubleShoot == False and gameSystem.playerObject.tripleShoot == False:

                gameSystem.playerObject.singleShoot = False
                gameSystem.playerObject.doubleShoot = True
                self.addDoubleShooterButton.pressed = False
                
                gameSystem.money -= 50000

            if self.addTripleShooterButton.pressed and gameSystem.playerObject.tripleShoot == False:

                gameSystem.playerObject.singleShoot = False
                gameSystem.playerObject.doubleShoot = False
                gameSystem.playerObject.tripleShoot = True
                self.addTripleShooterButton.pressed = False

                gameSystem.money -= 100000

        if self.str == "Items":

            self.bulletBombButton.draw( surface )
            self.laserBulletButton.draw( surface )
            
            self.shieldButton.draw( surface )
            self.healsButton.draw( surface )

            
    
    # Toggling menu on and off
    def open( self ): self.menuOpen = True
    def close( self ): self.menuOpen = False
    
            
        

        
