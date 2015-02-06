#s = 'azcbobobegghakl'
s = 'abcbcd'
#Longest substring in alphabetical order is: beggh
currentString = s[0]
longestString = s[0]
for i in range(1,len(s)):
    if s[i] >= s[i-1]:
        currentString += s[i]
    else:
        currentString = s[i]
    if len(currentString) > len(longestString):
        longestString = currentString
print 'Longest substring in alphabetical order is:',longestString
        