def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    notGuessed = ''
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            notGuessed = notGuessed + i
    return notGuessed
    
lettersGuessed = ['a','e','i','o','u']
print getAvailableLetters(lettersGuessed)