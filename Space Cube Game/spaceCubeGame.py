
# Importing Required Libraries
import pygame
import game
import store
import startMenu

# Intializing pygame and clock
pygame.init( )
clock = pygame.time.Clock()

# Setting the size of the window screen and the name
width = 1500
height = 900
screen = pygame.display.set_mode( ( width, height ) )
pygame.display.set_caption( "Space Cube" )

# Creating Game System, Store and Start Menu
gameStartMenu = startMenu.StartMenu( "Space Cube", width, height, True )
gameSystem = game.Game( width, height, False )
gameStore = store.Store( "Store", 50, 50, width-100, height-100, False )

gameSystem.money = 1000000

# While that runs the game  
while True:

    # Causes game to play 300 frames a second or less
    clock.tick(300)

    # Running Game System, Store and Start Menu
    gameSystem.run( screen )
    gameStore.run( screen, gameSystem )
    gameStartMenu.run( screen, gameSystem )

    # Checking for events
    for event in pygame.event.get( ):

        # If close button is pressed then closing program
        if event.type == pygame.QUIT:

            pygame.quit( )
            exit( )

        # Checking if mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:

            # Checking if start menu is open 
            if gameStartMenu.menuOpen:

                # Checking if pressed any of these start menu buttons
                if gameStartMenu.startButton.on: gameStartMenu.startButton.pressed = True
                elif gameStartMenu.endButton.on: gameStartMenu.endButton.pressed = True

            # Checking if store is open 
            if gameStore.menuOpen:

                # Checking if pressed any of these store buttons
                if gameStore.upgradesButton.on: gameStore.upgradesButton.pressed = True
                elif gameStore.addOnsButton.on: gameStore.addOnsButton.pressed = True
                elif gameStore.itemsButton.on: gameStore.itemsButton.pressed = True

                # Checking if upgrade store is open
                if gameStore.upgradesStore.menuOpen:

                    # Checking if pressed any of these uprades store buttons
                    if gameStore.upgradesStore.upgradeBulletSpeedButton.on: gameStore.upgradesStore.upgradeBulletSpeedButton.pressed = True
                    if gameStore.upgradesStore.upgradeBulletPowerButton.on: gameStore.upgradesStore.upgradeBulletPowerButton.pressed = True
                    if gameStore.upgradesStore.upgradePlayerSpeedButton.on: gameStore.upgradesStore.upgradePlayerSpeedButton.pressed = True

                    if gameStore.upgradesStore.upgradePlayerHpButton.on: gameStore.upgradesStore.upgradePlayerHpButton.pressed = True
                    if gameStore.upgradesStore.upgradeReloadTimeButton.on: gameStore.upgradesStore.upgradeReloadTimeButton.pressed = True

                # Checking if add-ons store is open
                elif gameStore.addOnsStore.menuOpen:

                    # Checking if pressed any of these add-ons store buttons
                    if gameStore.addOnsStore.addDoubleShooterButton.on: gameStore.addOnsStore.addDoubleShooterButton.pressed = True
                    if gameStore.addOnsStore.addTripleShooterButton.on: gameStore.addOnsStore.addTripleShooterButton.pressed = True

                # Checking if items store is open
                elif gameStore.itemsStore.menuOpen:

                    # Checking if pressed any of these items store buttons
                    if gameStore.itemsStore.bulletBombButton.on: gameStore.itemsStore.bulletBombButton.pressed = True
                    if gameStore.itemsStore.laserBulletButton.on: gameStore.itemsStore.laserBulletButton.pressed = True
                    
                    if gameStore.itemsStore.shieldButton.on: gameStore.itemsStore.shieldButton.pressed = True
                    if gameStore.itemsStore.healsButton.on: gameStore.itemsStore.healsButton.pressed = True

        # Checking if key is pressed
        if event.type == pygame.KEYDOWN:             

            # Toggling game and store when the key m is pressed
            if event.key == pygame.K_m and not gameStartMenu.menuOpen:

                if gameStore.menuOpen:  

                    gameSystem.open( )
                    gameStore.close( )
                         
                elif not gameStore.menuOpen:

                    gameSystem.close( )
                    gameStore.open( )

            if event.key == pygame.K_r and not gameStartMenu.menuOpen: gameSystem.playerObject.Hp = 0

    # Exiting Game if player hp is thess than or equal to 0
    if gameSystem.playerObject.Hp <= 0:

        gameStartMenu.open( )
        gameSystem.reset( )
        gameStore.close( )

        gameSystem.money = 1000000
    
    # Updating screen
    pygame.display.update( )
