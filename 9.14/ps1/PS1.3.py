s = 'azcbobobegghakl'
#s = 'abcbcd'
currentString = s[0] #make this the start of currentString
longestString = ' ' #initializing longestString
#starting at s[1], test each character s[i]
for i in range(1, len(s) - 1):
    if s[i] >= s[i-1]: #if current char >= previous char
        currentString = currentString + s[i] #append current char s[i] to currentString
        if len(currentString) > len(longestString): #if its longest, store in longestString
            longestString = currentString
    else:
        currentString = s[i] #initializes currentString to current character
print longestString