# Paste your code into this box 
count = 0
s=raw_input('Enter a string: ')
for i in range(0,(len(s))):
    if (s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        count = count+1
print 'Number of vowels:',count