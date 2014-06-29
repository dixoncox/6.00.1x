class RectangularRoomTest(object):
    def __init__(self, width, height):
        self.width  = width
        self.height = height

    def getNumTiles(self):
<<<<<<< HEAD
        #NumTiles = self.width * self.height #so when DO I use "self"?
        #return NumTiles
        #This also works. So when do I use 'self' and not use it?
        self.NumTiles = self.width * self.height #so when DO I use "self"?
        return self.NumTiles
=======
        NumTiles = self.width * self.height #so when DO I use "self"?
        return NumTiles
        #This also works. So when do I use 'self' and not use it?
        #self.NumTiles = self.width * self.height #so when DO I use "self"?
        #return self.NumTiles
>>>>>>> 2ec294a649486f56b093ccfca5f5193f4be59a9e
    
room = RectangularRoomTest(2,3)
print room.getNumTiles()

        
