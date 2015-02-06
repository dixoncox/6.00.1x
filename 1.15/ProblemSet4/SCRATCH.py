#import random
#import string
#import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    letterTotal = 0
    for i in word:
        letterTotal += SCRABBLE_LETTER_VALUES[i]
    if len(word) == n:
        wordTotal = (letterTotal*n)+50
    else:
        wordTotal = letterTotal*len(word)
    return wordTotal
    

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    handCopy = hand.copy()
    for i in word:
        handCopy[i] -= 1
    return handCopy


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handCopy = hand.copy()
    charInHand = True
    inWordList = word in wordList
    for i in word:
        if i in handCopy and handCopy[i] > 0:
            inHand = True
            handCopy[i] -= 1
        else:
            inHand = False
        charInHand = charInHand and inHand
    isWordValid = charInHand and inWordList
    return isWordValid

def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    #print                               # print an empty line
    
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    handTotal = 0
    for i in hand:
        handTotal += hand[i]
    return handTotal
    
            
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    updatedHand = hand.copy()
    totalScore = 0
    wordScore = 0
    while calculateHandlen(updatedHand) > 0:
        print 'Current hand:', 
        displayHand(updatedHand)
        userInput = raw_input('Enter word or a "." to indicate that you are finished: ')
        if userInput == '.':
            break
        elif isValidWord(userInput, updatedHand, wordList) == False:
            print 'Invalid word, please try again.'
        else:
            wordScore = getWordScore(userInput, n)
            updatedHand = updateHand(updatedHand, userInput)
            totalScore += wordScore
            print '"'+userInput+'" earned',wordScore,'points. Total:',totalScore,'points'
        print
    if calculateHandlen(updatedHand) == 0:
        print 'Run out of letters.',
    else:
        print 'Goodbye!',
    print 'Total score:', totalScore,'points'
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:
    
        # Display the hand
        
        # Ask user for input
        
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score


#word = 'appear'
#hand = {'a': 3, 'e': 1, 'p': 2, 'r': 1, 'u': 1, 't': 1}
#wordList = ['appear','tau']
#wordList = ['him','cam']
#wordList = ['fast','tow']
wordList = ['inertia']
#n = 7


#playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
#playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
#playHand(hand, wordList, n)
