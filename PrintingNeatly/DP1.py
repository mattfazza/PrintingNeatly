import sys
import math

sys.setrecursionlimit(1500)
M = 80
text = "Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this."
N = text.split()
n=len(N) - 1


extras = [[None for x in range(0, len(N))] for x in range(0, len(N))]
lc = [[None for x in range(0, len(N))] for x in range(0, len(N))]
l = [len(N[x]) for x in range (0, (len(N)))]
c = [0 for x in range (0, len(N))]
p = [0 for x in range (0, len(N))]
lines = ['' for x in range(0, n)]

#calculate extras
for i in range (0, n):
    extras[i][i] = M - l[i]
    for j in range(i+1, n):
        extras[i][j] = extras[i][j-1] - l[j] - 1

#calculate lc
for i in range(0, n):
    for j in range (i, n):
        if (extras[i][j] < 0):
            lc[i][j]= sys.maxsize
        elif(j == n and extras[i][j]>=0):
            lc[i][j] = 0
        else:
            lc[i][j]=math.pow(extras[i][j], 3)

#calculate c and p
c[0] = 0
for j in range(1, n):
    c[j] = sys.maxsize
    for i in range(1, j):
        if(c[i-1] != sys.maxsize and lc[i][j] != sys.maxsize and (c[i-1] + lc[i][j]) < c[j]):
            c[j] = c[i-1] + lc[i][j]
            p[j] = i



def GiveLines(J):

    i = p[J]
    if (i==0):
        k = 0
    else:
        k = GiveLines(i-1) + 1

    #diff = M - sum(map(len, N[:J+1]))
    #print()
    #print(diff)

    for z in range(i, J+1):
        if(z == J+1):
            lines[k] += N[z]
        else:
            lines[k] += (N[z] + ' ')


    print(k, i, J)
    return k

GiveLines(n-1)

for i in range(1, n-1):
    if(lines[i] != ''):
        print(lines[i])
        print(M-(len(lines[i]))+1)