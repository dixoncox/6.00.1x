def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = True
    for i in secretWord:
        if i in lettersGuessed:
            inList = True
        else:
            inList = False
        result = result and inList
        print i,result
    return result
S1='carrot'
L1=['z', 'x', 'q', 'c', 'a', 'r', 'r', 'o', 't']
print isWordGuessed(S1,L1)        