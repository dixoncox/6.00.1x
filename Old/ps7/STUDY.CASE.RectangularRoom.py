# Enter your code for RectangularRoom in this box
class RectangularRoom(object):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

        self.roomStatus = {}
        # Without the "self." prefix these wouldn't work. Without it, it was
        # just a local variable, with it it's an attribute?

        self.coords = ()
        # Same as above

        for i in range(width):
            for j in range(height):
                self.coords = (i,j)
                self.roomStatus[self.coords] = 'Dirty'

        #print roomStatus

    def getNumTiles(self):
        #NumTiles = self.width * self.height #so when DO I use "self"?
        #return NumTiles
        # This also works. So when do I use 'self' and not use it?

        self.NumTiles = self.width * self.height
        # so when DO I use "self"? Maybe because using "self." makes in an
        # attribute, otherwise it's just a local variable?
        return self.NumTiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        random_x = random.random() * self.width
        random_y = random.random() * self.height
        return Position(random_x, random_y)
        #raise NotImplementedError

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if ((pos.getX() < self.width) and (pos.getY() < self.height)) and pos.getX() >= 0 and pos.getY() >= 0:
            return True
        return False        
        
        # This was giving me problems for the longest time because I didn't
        # include the parens() in pos.getX() & pos.getY().
        # Since they are methods that require arguments, they needs parens.
        # self.width and self.height don't since they're attributes.
        # This is a RectangularRoom object using a Position object as an
        # argument.

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
        
        #raise NotImplementedError

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
        #raise NotImplementedError
