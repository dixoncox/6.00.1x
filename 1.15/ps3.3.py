def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
 
    guessed = ''
    for i in secretWord:
        if i in lettersGuessed:
            guessed += i
        else:
            guessed += '_'
    return guessed
    
print getGuessedWord('apple',['e', 'i', 'k', 'p', 'r', 's'])
