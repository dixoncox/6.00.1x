#s = 'azcbobobegghakl'
vowels = ['a','e','i','o','u']
numVowels = 0
for i in s:
    if i in vowels:
        numVowels += 1
print 'Number of vowels: ', numVowels
