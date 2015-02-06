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
    print result
    return result


isWordGuessed('apple',['a','p','l','e'])

