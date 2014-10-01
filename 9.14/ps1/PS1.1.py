# Counting Vowels (10 points possible)
# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
# Number of vowels: 5
#
# LOGIC: Using a for loop to go down string s, check each char i with a,e,i,o,u
# If a vowel, add 1 to count

s = 'azcbobobegghakl'
count = 0
#for i in range(len(s)):
for i in s:
    #print i
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
#    if i == 'a' or 'e' or 'i' or 'o' or 'u':
#    if 'a':    
#        print count
        count = count + 1
print "Number of vowels:", count