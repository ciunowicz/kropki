import copy

T = {}
P = {}

a = 1
b = 2
o = 3
A = 4
B = 5
C = 6
S = 7
R = 8

DP = a

T1 = []
BA = {}

TR,T11,T2,T3,T4,T42,T5,T45,T63,T7,C4,C3,A4,A5,A3,A3TR,NTR,NT11,BT42,BD42,BR42,BL42,TRA1,TRA,SP,CR3,CR4,CR5,CB2= ([] for i in range(29))
#, CBR2

TR.append([[
    [R,S,R],
    [S,a,S],
    [C,o,C]],[1]])

TR.append([[
    [R,S,C],
    [S,a,B],
    [C,o,C]],[0.9]])
TR.append([[
    [R,S,C],
    [S,a,o],
    [C,B,C]],[0.9]])
TR.append([[
    [C,o,C],
    [B,a,S],
    [C,S,R]],[0.9]])
TR.append([[
    [C,B,C],
    [o,a,S],
    [C,S,R]],[0.9]])
TR.append([[
    [C,S,R],
    [B,a,S],
    [C,o,C]],[0.9]])
TR.append([[
    [C,S,R],
    [o,a,S],
    [C,B,C]],[0.9]])
TR.append([[
    [C,B,C],
    [S,a,o],
    [R,S,C]],[0.9]])
TR.append([[
    [C,o,C],
    [S,a,B],
    [R,S,C]],[0.9]])
TR.append([[[C,o,0],[0,a,S],[C,S,R]],[0.7]])
TR.append([[[C,S,R],[o,a,S],[C,0,C]],[0.7]])
TR.append([[[C,o,C],[S,a,0],[R,S,C]],[0.7]])
TR.append([[[R,S,C],[S,a,0],[C,o,C]],[0.7]])


T11.append([[[C,a,C],[b,o,b],[C,a,C]],[0.9]])
T11.append([[[a,C,B],[C,o,C],[B,C,a]],[0.05]])
T11.append([[[a,B,C],[b,o,B],[C,a,C]],[0.9]])
T11.append([[[C,b,C],[b,a,0],[C,o,C]],[0.2]])
T11.append([[[C,b,C],[B,a,o],[C,b,C]],[0.2]])
T11.append([[[C,a,C],[B,o,B],[C,a,C]],[0.05]])
T11.append([[[C,C,a],[B,o,B],[C,a,C]],[0.05]])
T11.append([[[C,a,C],[B,b,o],[C,a,C]],[0.1]])
T11.append([[[C,b,a],[C,o,b],[C,a,C]],[0.9]])
T11.append([[[a,b,C],[b,o,C],[C,C,a]],[0.1]])

T11.append([[[a,C,C],[B,o,B],[C,a,C]],[0.05]])
T11.append([[[a,b,C],[b,o,C],[C,a,C]],[0.8]])
T11.append([[[C,a,C],[a,b,o],[C,a,C]],[0.7]])
T11.append([[[C,b,C],[b,a,b],[C,o,C]],[0.7]])
T11.append([[[0,a,C],[o,b,b],[0,a,a]],[0.7]])
T11.append([[[0,a,C],[o,b,b],[a,b,a]],[0.6]])
T11.append([[[a,a,C],[o,b,b],[a,a,a]],[0.7]])
T11.append([[[C,a,a],[b,b,b],[a,o,a]],[0.5]])
T11.append([[[a,b,C],[o,b,a],[a,b,a]],[0.4]])
T11.append([[[a,b,a],[o,b,a],[a,b,C]],[0.4]])

T11.append([[[0,o,0],[0,a,0],[0,a,0]],[0.3]])
T11.append([[[o,0,C],[0,a,0],[C,0,a]],[0.3]])
T11.append([[[0,o,0],[0,a,0],[0,a,0]],[0.7]])
T11.append([[[b,o,b],[b,a,B],[b,0,b]],[0.8]])
T11.append([[[a,b,a],[b,b,o],[a,a,b]],[0.6]])
T11.append([[[a,b,a],[o,b,b],[a,a,b]],[0.6]])
T11.append([[
            [C,o,C],
            [b,a,b],
            [C,b,C]],[0.8]])

T11.append([[
            [a,o,0],
            [0,b,a],
            [a,b,b]],[0.5]])

T11.append([[
            [C,a,C],
            [b,o,b],
            [C,a,C]],[0.5]])

T11.append([[
            [a,C,a],
            [b,b,o],
            [a,a,C]],[0.5]])


T2.append([[
            [C,0,C,C],
            [b,a,o,C],
            [C,b,a,0],
            [C,C,b,C]],[0.9]])
T2.append([[[C,b,C,C],[0,0,a,C],[C,o,0,b],[C,C,0,C]],[0.8]])
T2.append([[[o,0,C,C],[0,a,0,C],[C,0,a,0],[C,C,0,a]],[0.7]])
T2.append([[[o,C,C,C],[C,a,C,C],[C,C,a,C],[C,C,C,a]],[0.6]])
T2.append([[[C,a,C,C],[o,b,a,C],[a,b,b,a],[C,a,b,C]],[0.75]])
T2.append([[[C,C,a,C],[C,a,b,o],[a,b,b,a],[C,b,a,C]],[0.75]])
T2.append([[[a,C,C,C],[C,a,C,C],[C,C,a,C],[C,C,C,o]],[0.7]])
T3.append([[[C,b,C,0],[b,a,0,0],[B,o,B,0],[C,a,C,0]],[0.7]])
T3.append([[[B,B,o,0],[0,0,0,0],[B,a,B,0],[C,a,C,0]],[0.01]])
T3.append([[[C,B,C,0],[b,0,o,0],[B,a,0,0],[C,a,C,0]],[0.05]])
T3.append([[[C,a,C,0],[C,0,C,0],[B,o,B,0],[C,a,C,0]],[0.05]])
T3.append([[[C,a,C,0],[B,o,B,0],[A,0,C,0],[a,C,C,0]],[0.05]])
T3.append([[[C,a,C,0],[B,b,o,0],[C,0,0,0],[C,a,C,0]],[0.1]])
T3.append([[[C,b,C,0],[0,a,b,0],[B,o,B,0],[C,a,C,0]],[0.7]])  
T3.append([[[o,B,B,0],[0,0,0,0],[B,a,B,0],[C,a,C,0]],[0.01]])
T3.append([[[C,B,C,0],[o,0,b,0],[0,a,B,0],[C,a,C,0]],[0.05]])
T3.append([[[C,a,C,0],[B,o,B,0],[C,0,A,0],[C,C,a,0]],[0.05]])
T3.append([[[C,a,C,0],[o,b,B,0],[0,0,C,0],[C,a,C,0]],[0.1]])
T3.append([[[C,o,C,0],[C,a,C,0],[C,a,C,0],[C,a,C,0]],[0.6]])
T3.append([[[0,o,0,0],[0,a,0,0],[0,a,0,0],[0,a,0,0]],[0.8]])    
T3.append([[[a,b,a,0],[a,b,a,0],[a,b,o,0],[C,a,C,0]],[0.7]])
T3.append([[[C,a,C,0],[b,b,o,0],[a,b,a,0],[a,b,a,0]],[0.8]])
T3.append([[[0,o,0,0],[b,A,B,0],[b,A,b,0],[0,b,0,0]],[0.6]])
T3.append([[[0,o,0,0],[B,A,b,0],[b,A,b,0],[0,b,0,0]],[0.6]])
T4.append([[[C,a,C,0,0],[C,0,C,0,0],[B,o,B,0,0],[C,0,C,0,0],[C,a,C,0,0]],[0.05]])
T4.append([[[C,a,C,0,0],[C,0,C,0,0],[B,o,B,0,0],[A,0,C,0,0],[a,C,C,0,0]],[0.05]])
T4.append([[[C,a,C,0,0],[C,0,0,0,0],[B,b,o,0,0],[C,0,0,0,0],[C,a,C,0,0]],[0.1]])
T4.append([[[C,a,C,0,0],[C,0,0,0,0],[C,0,0,0,0],[B,b,o,0,0],[C,a,C,0,0]],[0.2]])
T4.append([[[C,a,C,0,0],[C,0,C,0,0],[B,o,B,0,0],[C,0,A,0,0],[C,C,a,0,0]],[0.05]])
T4.append([[[C,a,C,0,0],[0,0,C,0,0],[o,b,B,0,0],[0,0,C,0,0],[C,a,C,0,0]],[0.1]])
T4.append([[[C,a,C,0,0],[0,0,C,0,0],[0,0,C,0,0],[o,b,B,0,0],[C,a,C,0,0]],[0.2]])
T4.append([[[C,a,C,0,0],[C,a,C,0,0],[C,a,C,0,0],[C,a,C,0,0],[C,o,C,0,0]],[0.5]])
T4.append([[[C,o,C,0,0],[C,b,C,0,0],[C,b,a,0,0],[a,b,a,0,0],[C,a,C,0,0]],[0.3]])
T42.append([[[C,a,0,0],[B,0,0,0],[B,o,0,0],[a,C,0,0]],[0.05]])
T42.append([[[C,a,0,0],[C,0,0,0],[b,o,0,0],[a,C,0,0]],[0.1]])
T42.append([[[a,C,0,0],[0,C,0,0],[o,b,0,0],[C,a,0,0]],[0.1]])
T42.append([[[a,C,0,0],[a,C,0,0],[a,C,0,0],[o,C,0,0]],[0.6]])
T5.append([[[C,a,0,0,0],[C,0,0,0,0],[B,0,0,0,0],[B,o,0,0,0],[a,C,0,0,0]],[0.05]])
T5.append([[[a,C,0,0,0],[0,C,0,0,0],[0,B,0,0,0],[o,B,0,0,0],[C,a,0,0,0]],[0.05]])
T5.append([[[a,C,0,0,0],[a,C,0,0,0],[a,C,0,0,0],[a,C,0,0,0],[o,C,0,0,0]],[0.7]])
T45.append([[
            [C,a,C,C,0],
            [0,0,C,C,0],
            [0,0,b,C,0],
            [C,o,0,a,0],
            [C,C,0,C,0]],[0.1]])
T45.append([[[C,a,C,C,0],
            [0,0,b,C,0],
            [0,0,B,C,0],
            [C,o,0,a,0],
            [C,C,0,C,0]],[0.1]])
T45.append([[
            [C,C,0,C,0],
            [C,o,0,a,0],
            [0,0,b,C,0],
            [0,0,C,C,0],
            [C,a,C,C,0]],[0.1]])
T45.append([[
            [C,C,0,C,0]
            ,[C,o,0,a,0],
            [0,0,B,C,0],
            [0,0,b,C,0],
            [C,a,C,C,0]],[0.1]])
T63.append([[
    [C,a,C,0,0,0],
    [C,0,C,0,0,0],
    [B,o,B,0,0,0],
    [C,0,C,0,0,0],
    [C,0,C,0,0,0],
    [C,a,C,0,0,0]],[0.05]])
T63.append([[[C,a,C,0,0,0],[C,0,0,0,0,0],[C,0,0,0,0,0],[B,b,o,0,0,0],[C,0,0,0,0,0],[C,a,C,0,0,0]],[0.1]])
T63.append([[[C,a,C,0,0,0],[0,0,C,0,0,0],[0,0,C,0,0,0],[o,b,B,0,0,0],[0,0,C,0,0,0],[C,a,C,0,0,0]],[0.1]])
T7.append([[[C,a,C,0,0,0,0],[C,0,C,0,0,0,0],[C,0,C,0,0,0,0],[B,o,B,0,0,0,0],[C,0,C,0,0,0,0],[C,0,C,0,0,0,0],[C,a,C,0,0,0,0]],[0.05]])

T53 = []

T53.append([[
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0]],[0.05]])

T53.append([[
    [b,C,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0]],[0.05]])

T53.append([[
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0],
    [C,o,C,0,0],
    [b,C,C,0,0]],[0.05]])

T53.append([[
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,C,b,0,0]],[0.05]])

T53.append([[
    [C,C,b,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0],
    [C,o,C,0,0],
    [C,b,C,0,0]],[0.05]])

T35 = []

T35.append([[
    [C,C,C,C,C],
    [b,o,b,o,b],
    [C,C,C,C,C],
    [0,0,0,0,0],
    [0,0,0,0,0]],[0.05]])

T35.append([[
    [C,C,C,C,C],
    [C,o,b,o,b],
    [b,C,C,C,C],
    [0,0,0,0,0],
    [0,0,0,0,0]],[0.05]])

T35.append([[
    [b,C,C,C,C],
    [C,o,b,o,b],
    [C,C,C,C,C],
    [0,0,0,0,0],
    [0,0,0,0,0]],[0.05]])

T35.append([[
    [C,C,C,C,b],
    [b,o,b,o,C],
    [C,C,C,C,C],
    [0,0,0,0,0],
    [0,0,0,0,0]],[0.05]])

T35.append([[
    [C,C,C,C,C],
    [b,o,b,o,C],
    [C,C,C,C,b],
    [0,0,0,0,0],
    [0,0,0,0,0]],[0.05]])



""" T45x2 = []

T45x2.append([[
    [b,C,C,C,b],
    [C,o,b,o,C],
    [C,C,o,C,C],
    [C,C,b,C,C],
    [0,0,0,0,0]],[0.05]]) """


A3TR.append([[[R,S,C],[S,o,C],[C,C,b]],[0.4]])
A3TR.append([[[R,S,C],[S,o,b],[C,C,C]],[0.4]])
A3TR.append([[[S,C,C],[S,o,b],[S,C,C]],[0.4]])
A3TR.append([[[S,o,b],[S,C,C],[S,C,C]],[0.4]])
A3TR.append([[[S,C,C],[S,C,C],[S,o,b]],[0.4]])
NTR.append([
    [[R,S,C],
    [S,o,C],
    [C,C,C]],[0]])
NTR.append([[[S,S,S],[C,o,C],[C,C,C]],[0]])
NTR.append([[[R,S,R],[S,o,S],[C,C,C]],[0]])
NTR.append([[[C,a,C],[a,o,a],[C,a,C]],[0]])
NT11.append([[[C,C,C],[b,o,B],[b,b,B]],[0]])
NT11.append([[[C,b,C],[b,o,b],[C,b,C]],[0]])
BT42.append([
    [[C,b,C,C],
    [a,o,a,a],
    [C,C,C,C],
    [C,C,C,C]],[0.7]])
BT42.append([[[C,C,b,C],[a,a,o,a],[C,C,C,C],[C,C,C,C]],[0.7]])
BT42.append([[[a,o,a,a],[C,C,C,C],[C,C,C,C],[C,C,C,C]],[0.2]])
BT42.append([[[a,a,o,a],[C,C,C,C],[C,C,C,C],[C,C,C,C]],[0.2]])
BT42.append([[[a,a,a,o],[C,C,C,C],[C,C,C,C],[C,C,C,C]],[0.6]])
BT42.append([[[o,a,a,a],[C,C,C,C],[C,C,C,C],[C,C,C,C]],[0.6]])
BD42.append([[[C,C,C,C],[C,C,C,C],[C,C,b,C],[a,a,o,a]],[0.7]])
BD42.append([[[C,C,C,C],[C,C,C,C],[C,b,C,C],[a,o,a,a]],[0.7]])
BD42.append([[[C,C,C,C],[C,C,C,C],[C,C,C,C],[a,o,a,a]],[0.2]])
BD42.append([[[C,C,C,C],[C,C,C,C],[C,C,C,C],[a,a,o,a]],[0.2]])
BD42.append([[[C,C,C,C],[C,C,C,C],[C,C,C,C],[o,a,a,a]],[0.6]])
BD42.append([[[C,C,C,C],[C,C,C,C],[C,C,C,C],[a,a,a,o]],[0.6]])
BR42.append([[[C,C,C,a],[C,C,C,a],[C,C,b,o],[C,C,C,a]],[0.7]])
BR42.append([[[C,C,C,a],[C,C,b,o],[C,C,C,a],[C,C,C,a]],[0.7]])
BR42.append([[[C,C,C,a],[C,C,C,o],[C,C,C,a],[C,C,C,a]],[0.2]])
BR42.append([[[C,C,C,a],[C,C,C,a],[C,C,C,o],[C,C,C,a]],[0.2]])
BR42.append([[[C,C,C,a],[C,C,C,a],[C,C,C,a],[C,C,C,o]],[0.6]])
BR42.append([[[C,C,C,o],[C,C,C,a],[C,C,C,a],[C,C,C,a]],[0.6]])
BL42.append([[[a,C,C,C],[a,b,C,C],[o,b,C,C],[a,C,C,C]],[0.7]])
BL42.append([[[a,C,C,C],[o,b,C,C],[a,b,C,C],[a,C,C,C]],[0.7]])
BL42.append([[[a,C,C,C],[o,C,C,C],[a,C,C,C],[a,C,C,C]],[0.2]])
BL42.append([[[a,C,C,C],[a,C,C,C],[o,C,C,C],[a,C,C,C]],[0.2]])
BL42.append([[[a,C,C,C],[a,C,C,C],[a,C,C,C],[o,C,C,C]],[0.6]])
BL42.append([[[o,C,C,C],[a,C,C,C],[a,C,C,C],[a,C,C,C]],[0.6]])
TRA1.append([[[0,0,0,0],[0,0,b,0],[0,o,0,0],[0,0,0,0]],[0.1]])
TRA.append([[[0,B,0],[o,0,b],[0,b,0]],[0.2]])
TRA.append([[[0,o,0],[B,0,b],[0,b,0]],[0.2]])
TRA.append([[[0,o,0],[b,0,b],[0,b,0]],[0.3]])

""" SP.append([[[C,S,R],[o,b,S],[C,a,C]],[0]])
SP.append([[[C,S,R],[a,b,S],[C,o,C]],[0]])
SP.append([[[C,S,C],[S,o,S],[C,S,C]],[0.0]])
SP.append([[[R,S,R],[S,o,S],[C,S,C]],[0.0]])
SP.append([[[C,a,C],[a,o,a],[C,a,C]],[0.0]]) """




CB2.append([[[b,o,b],
            [o,C,C],
            [b,C,C]]
            ,[0.001]])


""" CBR2.append([[
    [b,o,S],
    [o,C,C],
    [b,C,C]],[1]]) """


SRight = 0
STop = 1
SLeft = 2
SDown = 3

def makeOposP(arr_tmp):
    tszab = []

    for x in range(len(arr_tmp)):
        tab = copy.deepcopy(arr_tmp[x])
        matt = tab[0]
        scc = tab[1]
        for i in range(len(matt)):
            for j in range(len(matt[i])):
                if matt[i][j] == a:
                    matt[i][j] = b
                elif matt[i][j] == b:
                    matt[i][j] = a
                elif matt[i][j] == B:
                    matt[i][j] = A
                elif matt[i][j] == A:
                    matt[i][j] = B
        tmp = []
        tmp.append(matt)
        tmp.append(scc)
        tszab.append(tmp)
   
    return tszab

def printDataM(matrix):

    for i in range(len(matrix)):
        tab = matrix[i][0]

        for j in range(len(tab)):
            for k in range(len(tab[j])):
                print(tab[j][k], ' ', end='')
            print()
        print("--------------")

def rotateMatrix(mat):
   
    matrix = []
    matrix2 = []
    mt2 = copy.deepcopy(mat)
    score = mt2[len(mt2)-1]
    matrix = mt2[0]
   
    if not matrix or not matrix[0]:
            return []
           
    for row in matrix:
        row.reverse()
   
    n = len(matrix)
   
    for i in range(n):
        for j in range(i):          
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   
    matrix2.append(matrix)
    matrix2.append(score)

    return matrix2



def shrinkMatrix(row, col, colhrink, matt, count0):
   
    mt2 = copy.deepcopy(matt)
    score = mt2[len(mt2)-1]
    matrix = mt2[0]

   

    tszb = [[0 for x in range(col)] for y in range(row)]
    Tszb = []

    if colhrink == SRight:
        for i in range(row):
            for j in range(col):
                tszb[i][j] = matrix[i][j]
       
        Tszb.append(tszb)
        Tszb.append(score)
        return Tszb
   
    elif colhrink == STop:
        for i in range(count0,row+count0):
            for j in range(col):
                tszb[i-count0][j] = matrix[i][j]
       
        Tszb.append(tszb)
        Tszb.append(score)
        return Tszb

    elif colhrink == SLeft:
        for i in range(row):
            for j in range(count0, col+count0):
                tszb[i][j-count0] = matrix[i][j]
   
        Tszb.append(tszb)
        Tszb.append(score)
        return Tszb
 
    elif colhrink == SDown:
        for i in range(row):
            for j in range(col):
                tszb[i][j] = matrix[i][j]
       
        Tszb.append(tszb)
        Tszb.append(score)
        return Tszb
   
    else:
        print("cosik nie tek")


def do4x4Matrix(tab, tabLen):

    Tabl = []
    count = 0

    if tabLen =="43" or tabLen =="42":
        count = 4
    elif tabLen =="53" or tabLen =="52" or tabLen =="45":
        count = 5
    elif tabLen =="35":
        count = 5
    elif tabLen =="63":
        count = 6
    elif tabLen =="73":
        count = 7

   
    for j in range(len(tab)):
        i = -1
        a,b = (0,0)
        tab2 = tab[j][0]
       

        for k in range(4):
            lycz = 0
            for l in range(len(tab2)):
                if k == SRight:
                    if tab2[l][len(tab2)-1] == 0: lycz+=1
                elif k == STop:
                    if tab2[0][l] == 0: lycz+=1
                elif k == SLeft:
                    if tab2[l][0] == 0: lycz+=1
                elif k == SDown:
                    if tab2[len(tab2)-1][l] == 0: lycz+=1
           
            if lycz == count:
                i = k
                break    
           
        if i < 0: continue

        if i == SRight and tabLen =="42":
            a = 4
            b = 2

        elif i == STop and tabLen =="42":
            a = 2
            b = 4
       
        elif i == SLeft and tabLen =="42":
            a = 4
            b = 2
       
        elif i == SDown and tabLen =="42":
            a = 2
            b = 4      

        elif i == SRight and tabLen =="43":
            a = 4
            b = 3

        elif i == STop and tabLen =="43":
            a = 3
            b = 4
           
       
        elif i == SLeft and tabLen =="43":
            a = 4
            b = 3
       
        elif i == SDown and tabLen =="43":
            a = 3
            b = 4
       
        elif i == SRight and tabLen =="53":
            a = 5
            b = 3

        elif i == STop and tabLen =="53":
            a = 3
            b = 5
       
        elif i == SLeft and tabLen =="53":
            a = 5
            b = 3
       
        elif i == SDown and tabLen =="53":
            a = 3
            b = 5
       #tu coś
        elif i == SDown and tabLen =="35":
            a = 3
            b = 5
     
        elif i == SRight and tabLen =="52":
            a = 5
            b = 2

        elif i == STop and tabLen =="52":
            a = 2
            b = 5
       
        elif i == SLeft and tabLen =="52":
            a = 5
            b = 2
       
        elif i == SDown and tabLen =="52":
            a = 2
            b = 5

        elif i == SRight and tabLen =="45":
            a = 5
            b = 4

        elif i == STop and tabLen =="45":
            a = 4
            b = 5
       
        elif i == SLeft and tabLen =="45":
            a = 5
            b = 4
       
        elif i == SDown and tabLen =="45":
            a = 4
            b = 5

        elif i == SRight and tabLen =="63":
            a = 6
            b = 3

        elif i == STop and tabLen =="63":
            a = 3
            b = 6
       
        elif i == SLeft and tabLen =="63":
            a = 6
            b = 3
       
        elif i == SDown and tabLen =="63":
            a = 3
            b = 6

        elif i == SRight and tabLen =="73":
            a = 7
            b = 3

        elif i == STop and tabLen =="73":
            a = 3
            b = 7
       
        elif i == SLeft and tabLen =="73":
            a = 7
            b = 3
       
        elif i == SDown and tabLen =="73":
            a = 3
            b = 7
       

        if(tabLen =="43"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],1))
        elif(tabLen =="42"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],2))
        elif(tabLen =="35"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],3))
        elif(tabLen =="53"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],2))
        elif(tabLen =="45"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],1))
        elif(tabLen =="52"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],3))
        elif(tabLen =="63"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],3))
        elif(tabLen =="73"):
            Tabl.append(shrinkMatrix(a,b,i, tab[j],4))
        else:
            Tabl.append(shrinkMatrix(a,b,i, tab[j],1))
           
        i+=1
        if i > SDown: i = 0

    return Tabl


def arr_11(matrix):
    matrix.append(rotateMatrix(matrix[0]))
    matrix.append(rotateMatrix(matrix[1]))

    matrix.append(rotateMatrix(matrix[2]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[5]))

    matrix.append(rotateMatrix(matrix[6]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[7]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[8]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[9]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

   

    matrix.append(rotateMatrix(matrix[10]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[11]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[12]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[13]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[14]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[15]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[16]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[17]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[18]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[19]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[20]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[21]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[22]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[23]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[24]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[25]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[26]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[27]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[29]))

    matrix.append(rotateMatrix(matrix[30]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   




def arr_ntr(matrix):
    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))


def arr_2(matrix):
    matrix.append(rotateMatrix(matrix[0]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[2]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))
    matrix.append(rotateMatrix(matrix[5]))
    matrix.append(rotateMatrix(matrix[6]))

def arr_CB2(matrix):
    matrix.append(rotateMatrix(matrix[0]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

def arr_3(matrix):

    matrix.append(rotateMatrix(matrix[0]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[5]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[6]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[7]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[8]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[9]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[10]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[11]))

    matrix.append(rotateMatrix(matrix[12]))

    matrix.append(rotateMatrix(matrix[15]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[16]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))



def arr_4(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[1]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[5]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[6]))
    for i in range(2):
        matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[7]))

    matrix.append(rotateMatrix(matrix[8]))
   
   

def arr_42(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[3]))



def arr_5(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))



def arr_45(matrix):

    matrix.append(rotateMatrix(matrix[0]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))



def arr_63(matrix):

    matrix.append(rotateMatrix(matrix[0]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))


def arr_7(matrix):

    matrix.append(rotateMatrix(T7[0]))



def arr_a3tr(matrix):

    matrix.append(rotateMatrix(matrix[0]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))



def arr_ntr3(matrix):
 

    matrix.append(rotateMatrix(matrix[4]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
   
    matrix.append(rotateMatrix(matrix[5]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[6]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[7]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))




def arr_nt11(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))


def arr_tra1(matrix):

    matrix.append(rotateMatrix(matrix[0]))
   

def arr_tra(matrix):
    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[3]))


""" def arr_sp(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[1]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1])) """

ATR = makeOposP(TR)



TR.append(rotateMatrix(TR[0]))
TR.append(rotateMatrix(TR[len(TR)-1]))
TR.append(rotateMatrix(TR[len(TR)-1]))

T['T3x3r'] = []

for i in range(len(TR)):
    T['T3x3r'].append(TR[i])

arr_11(T11)

T['T3x3'] = []
T['T3x3'].extend(T11)

arr_2(T2)

T['T4x4'] = []
T['T4x4'].extend(T2)


arr_3(T3)

Temp44 = do4x4Matrix(T3,"43")

T['T4x3'] = []
T['T3x4'] = []

for i in range(len(Temp44)):
    if len(Temp44[i][0]) == 4:
        T['T4x3'].append(Temp44[i])
    elif len(Temp44[i][0]) == 3:
        T['T3x4'].append(Temp44[i])


arr_4(T4)

Temp55 = do4x4Matrix(T4,"53")

T['T3x5'] = []
T['T5x3'] = []

for i in range(len(Temp55)):
    if len(Temp55[i][0]) == 5:
        T['T5x3'].append(Temp55[i])
    elif len(Temp55[i][0]) == 3:
        T['T3x5'].append(Temp55[i])

Temp5x3 = do4x4Matrix(T53,"53")
for i in range(len(Temp5x3)):
    if len(Temp5x3[i][0]) == 5:
        T['T5x3'].append(Temp5x3[i])
Temp3x5 = do4x4Matrix(T35,"35")
for i in range(len(Temp3x5)):
    if len(Temp3x5[i][0]) == 5:
        T['T3x5'].append(Temp3x5[i])
#printDataM(T3x5)


arr_42(T42)

Temp42 = do4x4Matrix(T42,"42")

T['T4x2'] = []
T['T2x4'] = []

for i in range(len(Temp42)):
    if len(Temp42[i][0]) == 4:
        T['T4x2'].append(Temp42[i])
    elif len(Temp42[i][0]) == 2:
        T['T2x4'].append(Temp42[i])


arr_5(T5)

Temp52 = do4x4Matrix(T5,"52")

T['T5x2'] = []
T['T2x5'] = []

arr_45(T45)

Temp45 = do4x4Matrix(T45,"45")

T['T4x5'] = []
T['T5x4'] = []

for i in range(len(Temp45)):
    if len(Temp45[i][0]) == 5:
        T['T5x4'].append(Temp45[i])
    elif len(Temp45[i][0]) == 4:
        T['T4x5'].append(Temp45[i])


arr_63(T63)


Temp63 = do4x4Matrix(T63,"63")

T['T6x3'] = []
T['T3x6'] = []

arr_7(T7)



#printDataM(Temp5x3)



""" Temp4x5 = do4x4Matrix(T45x2,"45")

printDataM(Temp4x5) """

Temp73 = do4x4Matrix(T7,"73")

T['T7x3'] = []
T['T3x7'] = []

for i in range(len(Temp73)):
    if len(Temp73[i][0]) == 7:
        T['T7x3'].append(Temp73[i])
    elif len(Temp73[i][0]) == 3:
        T['T3x7'].append(Temp73[i])



arr_ntr(NTR)

arr_a3tr(A3TR)

arr_ntr3(NTR)

arr_nt11(NT11)

arr_tra(TRA)
arr_tra1(TRA1)

arr_CB2(CB2)
#arr_CB2(CBR2)

#arr_sp(SP)

BA['TBT4x2'] = BT42
BA['TBD4x2'] = BD42
BA['TBL4x2'] = BL42
BA['TBR4x2'] = BR42
