# Space_Cube_Game

Note: Game is still under development

After taking a break from programming, I decided to enhance my skills in Object Oriented Programming. Now that I have returned, I started a new project and have incorporated several classes in it. I have been diligent in commenting my code and focusing on small details to ensure the code is clean and efficient.

By understanding classes as objects, I was able to create several objects such as Player, Enemy, Bullet, Button, Game, StartMenu, and Store.

Furthermore, I have implemented abstract classes for objects like players and enemies, which I have named Character, to demonstrate my understanding of how they work.

Game Description:

Game Start Menu: 

Title: Space Cube Game

Button Start: Starts the game console
Button Quit: Shuts the program down

Highscore( Not implemented yet ): Tracks the best score ever taken in the game.

Occurance: Start of the game and when player Dies

Player Mechanics:

Movement: A player, which is a blob, can move in any directions as long as they are on there side of the border.
Attacking: The player can attack using the space ke, which shoots at a bullet.

Health: There blob colour represents there Hp which transitions from green to yellow to red smoothly depending on the percentage of HP left. Damage is taken when body collides with a bullet.
Death: After HP goes below 0 the game ends.

Enemy Mechanics: 

Types: Easy, Medium, Hard, Very Hard, Impossible

Spawning( Not implemented yet ): Random spawn from within their side. Type spawning is random and the likeness of each type varies on how long the game is been going on for and how many kills the player has.

Movement: Enemies are stationary after spawing
Attacking: Shoot at a rate dependent on type

Health: There blob colour represents there Hp which transitions from green to yellow to red smoothly depending on the percentage of HP left. Damage is taken when body collides with a bullet.
Death: If there type is Easy they dissapear after HP goes below 0, but if there are any other type in there place a one stage weaker enemy is spawned.

Money System:

Earned: It is given when a enemy dies and the amount is determined via enemy type.
Spent: Used to buy upgrades, add-ons and items via store.

Store:

Opened: Using the key "m"

Upgrades:

Bullet Speed: Increase Bullet Speed
Bullet Power: Increase Bullet Damage
Relaod Time: Gives a smaller interval between shooting times
Player HP: Gives a higher health value to player. The current player hp after upgraded is dependent on the percentage it had prior to buying upgrade.
Player Speed: Upgrade player movement speed

Add-ons:

Double Shoot: Shoots 2 bullets at a time
Triple Shoot: Shoots 3 bullets at a time

Items( Not implemented yet ):

Bullet Bomb: After contact with enemy damages enemies with a certain radius. Damage value depends on plater damage stat.
Laser Bullet: A insta kill for all enemies in its path
Shield: A shield is spawned in front of player which has its own HP and also despawns over time. Hp is demonstared via colour.
Heals: only way to get Back HP once damaged

