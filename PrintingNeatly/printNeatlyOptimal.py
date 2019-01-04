# CS4349 - Advanced Algorithm Design
# This program was created by Mathews Fazza as the programming project for CS4349
#
# Python version - 3.6.x but any version above 3 should work
#
# there are three ways to run the program:
# 1 - No arguments: if the program is run without arguments the user will be prompted to enter a text to be justified
# 2 - 1 argument: The argument needs to be a valid filename.  The file will be output justified.
# 3 - 2 arguments: In this mode the user can specify both the file and the width of each line.  A negative width
#                 will change the extra spaces into plus signs
#
# The algorithm is described in the report.  Please, see the report for details on this implementation

import math
import sys

global Penalty
global M
M = 80
Penalty = 0

def Print_Neatly(words, n, M):

    extras = [[9999 for i in range(n + 1)] for j in range(n + 1)]
    global lc
    lc = [[9999 for i in range(n + 1)] for j in range(n + 1)]
    c = [sys.maxsize] * (n + 1)
    p = [9999] * (n + 1)

    #find the values of extras
    for i in range(1, n+1):
        extras[i][i] = M - len(words[i])
        for j in range(i+1, n+1):
            extras[i][j] = extras[i][j-1] - len(words[j]) - 1

    #find the values of lc
    for i in range(1, n+1):
        for j in range(1, n+1):
            if (extras[i][j] < 0 and extras[i][j]):
                lc[i][j] = sys.maxsize
            elif j == n and extras[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = math.pow((extras[i][j]), 3)

    #find c and p
    c[0] = 0
    for j in range(1, n+1):
        for i in range(1, j+1):
            if c[i-1] + lc[i][j] < c[j]:
                c[j] = c[i-1] + lc[i][j]
                p[j] = i

    return c, p



def Build_Line(text, j, P, increment):

    i = P[j]
    line = 1
    if i != 1:
        line = Build_Line(text, i - 1, P, increment) + 1

    #find the number of extra spaces needed for each line
    extra_spaces  = M - ( sum(map(len, text[i:(j+1)])) + len(text[i:(j+1)])) +1
    #another way to find out extra_spaces is written below.  They both work
    #extra_spaces  = int(lc[i][j])

    #in order to print the justified text, we need to consider two different cases:
    #the last line, and all the other lines

    #last line
    if(j==n):
        for x in range (i, j+1):
            if(x < j):
                print(text[x], end=' ')
            #last word of line
            else:
                print(text[x], end='')
            #all other words have a chance of having an extra space attached to them

    #all the other lines
    else:
        Penalties[increment] += int(lc[i][j])
        for x in range(i, j+1):
            #first word of line
            if(x == i):
                print(text[x], end=' ')
            #last word of line
            elif(x == j):
                print(text[x], end='')
            #all other words have a chance of having an extra space attached to them
            else:
                if(extra_spaces>0):
                    if(S==-1):
                        print(text[x], end='+ ')
                    else:
                        print(text[x], end='  ')
                    extra_spaces += -1
                else:
                    print(text[x], end=' ')

    print()
    return line


def main(argv):

    text = ''
    M = 80
    global S #switch to turn spaces into plus signs
    global Penalties
    S = 0

    if(len(argv)<1):
        text = input("Please enter the text to be justified.")
        M=80
    elif(len(argv)==1):
        try:
            textfile = open(sys.argv[1], 'r')
            text = textfile.read()
            M=80
        except FileNotFoundError:
            print("Please, try a valid file name next time.")
    elif(len(argv)==2):
        try:
            textfile = open(sys.argv[1], 'r')
            text = textfile.read()
        except FileNotFoundError:
            print("Please, try a valid file name next time.")
        try:
            M = int(sys.argv[2])
            if(M<0):
                M = abs(M)
                S = -1
        except ValueError:
            print("Please, enter a number as your second argument.")

    #the text needs to be split whenever there is a paragraph.
    paragraphs = text.split('\n\n')


    for h in range(0, len(paragraphs)):
        paragraphs[h] = paragraphs[h].replace('\n', '')


    Penalties = [0 for i in paragraphs]
    increment = 0

    for words in paragraphs:

        words = ['blank'] + words.split(' ')
        global n
        n = len(words) - 1
        C, P = Print_Neatly(words, n, M)
        Build_Line(words, n, P, increment)
        increment = increment + 1
        print()


    print(sum(Penalties), '\n')
    print("Additional details:")
    print("Number of paragraphs:", len(Penalties))
    print("Penalties of paragraphs: ", end='')
    for i in range(0, len(Penalties)):
        if(Penalties[i] != 0):
            print(Penalties[i], end=" ")
    print()

if __name__ == '__main__':
    main(sys.argv[1:])
