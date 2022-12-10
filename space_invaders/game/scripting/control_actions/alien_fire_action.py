import random

from constants import *

from space_invaders.game.scripting.action import Action
from space_invaders.game.casting.point import Point
from space_invaders.game.casting.body import Body
from space_invaders.game.casting.image import Image
from space_invaders.game.casting.actors.bullet import Bullet
from space_invaders.game.casting.actors.ship import Ship
from space_invaders.game.casting.actors.alien import Alien
from space_invaders.game.casting.sound import Sound

#from Greg maybe we can rename this ShipBulletAction
#I will create AlienBulletAction to handle alien firings
class AlienBulletAction(Action):
    """creates a bullet from an origin (ship or alien) object.
    
    Arguments:
        origin: an instance of a ship or an alien with a position
        sound: an instance of a sound
    """

    def __init__(self, origin):
        super().__init__()
        self._origin = origin 
        #self._sound = sound

    def execute(self, cast, script, callback):
        #fires every 80, 160, 240, 320, 400, 480 cycle of the while loop in director
        if callback._counter in [80, 160, 240, 320, 400, 480]:
            #this is my attempt to make sure that only 
            #alien ships with no alien ships in front
            #of them will has the ability to fire a bullet

            #get all the aliens positions
            aliens_pos = []
            #get all the aliens
            aliens = cast.get_actors(BRICK_GROUP)
            for a in aliens:
                x = a._body._position._x
                y = a._body._position._y
                #append alien positions in string format
                #store in an array
                aliens_pos.append(f'{x}{y}')

            #create a list of aliens with no aliens in front
            alien_shooters = []
            for al in aliens:
                w = al._body._position._x
                b = al._body._position._y + 48

                al_pos = (f'{w}{b}')

                if al_pos not in aliens_pos:
                    alien_shooters.append(al)

            #get a random alien based on the new list
            ran_index = random.randint(0, len(alien_shooters) - 1)

            alien_body = alien_shooters[ran_index].get_body()
            position = alien_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, 6) #I figured 6 should be fast enough for bullet travel
            abody = Body(position, size, velocity)
            image = Image(BULLET_IMAGE)
            bullet = Bullet(abody, image, True)
            cast.add_actor(ALIEN_BULLET_GROUP, bullet)           



            """
            This is the code where every alien regardless of it's 
            position will fire a bullet

            #get a random brick/alien
            alien = cast.get_actors(ALIEN_GROUP)
            ran_index = random.randint(0, len(alien) - 1)

            alien_body = alien[ran_index].get_body()
            position = alien_body.get_position()
            size = Point(BULLET_WIDTH, BULLET_HEIGHT)
            velocity = Point(0, 6) #I figured 6 should be fast enough for bullet travel
            abody = Body(position, size, velocity)
            image = Image(BULLET_IMAGE)
            bullet = Bullet(abody, image, True)
            cast.add_actor(ALIEN_BULLET_GROUP, bullet)
            """


        #optional is we can also make a move alien bullet here 
        #this is what I did with my code

        """
        #move the bullet
        bullets = cast.get_actors(BULLET_GROUP)
        for bullet in bullets:
            body = bullet.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
        """