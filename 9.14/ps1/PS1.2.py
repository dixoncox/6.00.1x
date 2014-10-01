# Counting bobs (15 points possible)
# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2

# LOGIC: Use string indexes to iterate over 

s = 'azcbobobegghakl'
count = 0
for i in range(len(s)):
    if (s[i] == 'b' and s[i+1] == 'o' and s[i+2] == 'b'):
        count += 1
print 'Number of times bob occurs is:',count
 