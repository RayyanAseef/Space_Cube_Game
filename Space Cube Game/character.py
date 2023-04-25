
# importing abstract
from abc import ABC, abstractmethod

# Creating character abstract class
class Character(ABC):

    # Making child classes define draw method
    @abstractmethod
    def draw( self ):
        pass

    # Making child classes define shoot method
    @abstractmethod
    def shoot( self ):
        pass

    # Making child classes define takeDamage method
    @abstractmethod
    def takeDamage( self ):
        pass

    
