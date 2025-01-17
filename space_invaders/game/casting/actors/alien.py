#import necessary classes
from constants import *
from space_invaders.game.casting.actors.actor import Actor #import Actor class for use as parent class
from game.casting.point import Point


class Alien(Actor):
    """A solid, creature object that moves down the screen and left to right. It can fire bullets and is destroyed when it is hit by a bullet from the ship."""

    def __init__(self, body, image, hitPoints, points, debug = False):
        """Constructs a new Alien.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug) #inherits the init of actor class
        self._body = body #assigns body arg to an attribute - the body is the solid part of the alien used to detect collisions -- aka the alien's hit box
        self._image = image #assigns animation arg to an attribute - any movements in the image of an alien
        self._hitPoints = hitPoints 
        self._points = points #assigns point arg to an attribute - how many points an alien is worth when destroyed
        
    def get_image(self):
        """Gets the alien's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_hitPoints(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._hitPoints

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points

    #moves the aliens from left to right
    def move_opposite(self):
        """Moves the aliens left to right"""
        velocity = self._body.get_velocity()
        vx = velocity.get_x() * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def move_down(self):
        """Moves the alien down."""
        velocity = self._body.get_velocity()
        vx = velocity.get_x()
        vy = ALIEN_VELOCITY_Y
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    #stops the alien from moving down
    def stop_y(self):
        """Returns the y velocity to zero."""
        velocity = self._body.get_velocity()
        #rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = 0 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    #moves the alien group to the right at the start
    def release(self):
        """Release the ball in a random direction."""
        vx = ALIEN_VELOCITY_X
        vy = 0
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)