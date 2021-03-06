import math
# n'th triangle number = sum(1,n) x
# Thought about using recursion for triangle, but the numbers here could
# get rather large and I didn't want to hit Python limits
def triangle(n):
    total=0
    for x in range(1,n):
        total+=x
    return total

# Count the number of factors of n
def numfactors(n):
    count=0
    x=1
    while x<math.sqrt(n):
        if n%x==0:
            count+=2
        x+=1
    return count

# Generate triangle numbers and count their factors.
# Stop when a triangle number has more than NF factors
NF=500
t=0
f=0
maxf=0
n = 1
while maxf<NF:
    t=triangle(n)
    f = numfactors(t)
    if maxf<f:
        maxf=f
        print "Triangle %d has %d factors" % (t,maxf)
    n+=1
