testDict = {}
t1 = ()
#i = 3
#j = 4
#testTuple = (i,j)
#print testTuple

for i in range(4):
    for j in range(5):
        t1 = (i,j)
        testDict[t1] = 'FALSE'

print testDict
        
