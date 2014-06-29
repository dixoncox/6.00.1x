
import math
import random

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: number representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)
        #return (self.x, self.y)

class RectangularRoomTest(object):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

        self.roomStatus = {} #Without the "self." prefix these wouldn't work. Without it, it was just a local variable, with it it's an attribute?
        self.coords = () #Same as above

        for i in range(width):
            for j in range(height):
                self.coords = (i,j)
                self.roomStatus[self.coords] = 'Dirty'

        #print roomStatus

    def getNumTiles(self):
        #NumTiles = self.width * self.height #so when DO I use "self"?
        #return NumTiles
        #This also works. So when do I use 'self' and not use it?
        self.NumTiles = self.width * self.height #so when DO I use "self"? Maybe because using "self." makes in an attribute, otherwise it's just a local variable?
        return self.NumTiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        random_x = random.randint(0,self.width)
        random_y = random.randint(0,self.height)
        return Position(random_x, random_y)
        #raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        return (pos.getX() <= self.width) and (pos.getY() <= self.height) #This was giving me problems for the longest time because I didn't include the parens() in pos.getX() & pos.getY().
        #Since they are methods that require arguments, they needs parens. self.width and self.height don't since they're attributes.
        #This is a RectangularRoom object using a Position object as an argument.

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """

        #roomStatus = {}
        #coords = ()

        #for i in range(self.width):
            #for j in range(self.height):
                #coords = (i,j)
                #roomStatus[coords] = 'False'
     
        tileX = int(math.floor(pos.getX()))
        tileY = int(math.floor(pos.getY()))
        tile = (tileX, tileY)
        #print tile
        self.roomStatus[tile] = 'Clean'
        #print self.roomStatus
        #print self.roomStatus[(3,4)]
        #print type(self.roomStatus[(0,0)])
        #return 
        #raise NotImplementedError

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        return self.roomStatus[(m,n)] == 'Clean'
        
        raise NotImplementedError

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        cleanCount = 0
        for i in self.roomStatus:
            #print self.roomStatus[i]
            if self.roomStatus[i] == 'Clean':
                cleanCount += 1
        return cleanCount
        raise NotImplementedError
    
room = RectangularRoomTest(4,6) #instantiates an *OBJECT* of the RectangularRoomTest *CLASS*, and initializes it with (5,10) dimensions
print 'Dimensions of room: ',room.width, room.height #there are no getX & getY methods, so have to access directly, also since they're attributes no ()'s
print 'Random position in room =',room.getRandomPosition() #doesn't really make sense since it has no dependency on current room object. But hey, it's part of the class.
print 'Room Tiles =',room.getNumTiles() #straightforward, empty parentheses since room is explicity stated
testPosition = Position(3.5,4.5) #instantiating an *OBJECT* of the Position *CLASS* with arguments (3,4)
print 'Test Position =', testPosition.__str__() #testPosition object calling __str__ method
print 'Is Test Position in room?:',room.isPositionInRoom(testPosition)
#print room.cleanTileAtPosition(3.5, 4.5) <-- This didn't work because (3.5, 4.5) isn't a Position object, you just put numbers in there.
print room.cleanTileAtPosition(testPosition)
print 'Is Test Position tile clean?',room.isTileCleaned(3,4)
print 'Number of clean tiles:',room.getNumCleanedTiles()



        
