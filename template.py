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

TR = []

TR.append([[[R,S,C],[S,a,b],[C,o,C]],[0.9]])
TR.append([[[R,S,C],[S,a,o],[C,b,C]],[0.9]])
TR.append([[[C,o,C],[b,a,S],[C,S,R]],[0.9]])
TR.append([[[C,b,C],[o,a,S],[C,S,R]],[0.9]])
TR.append([[[C,S,R],[b,a,S],[C,o,C]],[0.9]])
TR.append([[[C,S,R],[o,a,S],[C,b,C]],[0.9]])
TR.append([[[C,b,C],[S,a,o],[R,S,C]],[0.9]])
TR.append([[[C,o,C],[S,a,b],[R,S,C]],[0.9]])
TR.append([[[C,o,0],[0,a,S],[C,S,R]],[0.7]])
TR.append([[[C,S,R],[o,a,S],[C,0,C]],[0.7]])
TR.append([[[C,o,C],[S,a,0],[R,S,C]],[0.7]])
TR.append([[[R,S,C],[S,a,0],[C,o,C]],[0.7]])


T11 = []
#3x3
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
T11.append([[[C,b,C],[b,o,b],[C,C,C]],[-0.5]])
T11.append([[[C,C,C],[a,o,C],[a,a,C]],[-0.5]])
T11.append([[[C,C,C],[o,a,C],[a,a,C]],[-0.5]])
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


T2 = []
#4x4
T2.append([[[C,0,C,C],[b,a,o,C],[C,b,a,0],[C,C,b,C]],[0.9]])
T2.append([[[C,b,C,C],[0,0,a,C],[C,o,0,b],[C,C,0,C]],[0.8]])
T2.append([[[o,0,C,C],[0,a,0,C],[C,0,a,0],[C,C,0,a]],[0.7]])
T2.append([[[o,C,C,C],[C,a,C,C],[C,C,a,C],[C,C,C,a]],[0.6]])
T2.append([[[C,a,C,C],[o,b,a,C],[a,b,b,a],[C,a,b,C]],[0.75]])
T2.append([[[C,C,a,C],[C,a,b,o],[a,b,b,a],[C,b,a,C]],[0.75]])
T2.append([[[a,C,C,C],[C,a,C,C],[C,C,a,C],[C,C,C,o]],[0.7]])

T3 = []
#4x3 i 3x4
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


T4 = []

T4.append([[[C,a,C,0,0],[C,0,C,0,0],[B,o,B,0,0],[C,0,C,0,0],[C,a,C,0,0]],[0.05]])
T4.append([[[C,a,C,0,0],[C,0,C,0,0],[B,o,B,0,0],[A,0,C,0,0],[a,C,C,0,0]],[0.05]])
T4.append([[[C,a,C,0,0],[C,0,0,0,0],[B,b,o,0,0],[C,0,0,0,0],[C,a,C,0,0]],[0.1]])
T4.append([[[C,a,C,0,0],[C,0,0,0,0],[C,0,0,0,0],[B,b,o,0,0],[C,a,C,0,0]],[0.2]])
T4.append([[[C,a,C,0,0],[C,0,C,0,0],[B,o,B,0,0],[C,0,A,0,0],[C,C,a,0,0]],[0.05]])
T4.append([[[C,a,C,0,0],[0,0,C,0,0],[o,b,B,0,0],[0,0,C,0,0],[C,a,C,0,0]],[0.1]])
T4.append([[[C,a,C,0,0],[0,0,C,0,0],[0,0,C,0,0],[o,b,B,0,0],[C,a,C,0,0]],[0.2]])
T4.append([[[C,a,C,0,0],[C,a,C,0,0],[C,a,C,0,0],[C,a,C,0,0],[C,o,C,0,0]],[0.5]])
T4.append([[[C,o,C,0,0],[C,b,C,0,0],[C,b,a,0,0],[a,b,a,0,0],[C,a,C,0,0]],[0.3]])


T42 = []

T42.append([[[C,a,0,0],[B,0,0,0],[B,o,0,0],[a,C,0,0]],[0.05]])
T42.append([[[C,a,0,0],[C,0,0,0],[b,o,0,0],[a,C,0,0]],[0.1]])
T42.append([[[a,C,0,0],[0,C,0,0],[o,b,0,0],[C,a,0,0]],[0.1]])
T42.append([[[a,C,0,0],[a,C,0,0],[a,C,0,0],[o,C,0,0]],[0.6]])

#5x2
T5 = []

T5.append([[[C,a,0,0,0],[C,0,0,0,0],[B,0,0,0,0],[B,o,0,0,0],[a,C,0,0,0]],[0.05]])
T5.append([[[a,C,0,0,0],[0,C,0,0,0],[0,B,0,0,0],[o,B,0,0,0],[C,a,0,0,0]],[0.05]])
T5.append([[[a,C,0,0,0],[a,C,0,0,0],[a,C,0,0,0],[a,C,0,0,0],[o,C,0,0,0]],[0.7]])

T45 = []

T45.append([[[C,a,C,C,0],[0,0,C,C,0],[0,0,b,C,0],[C,o,0,a,0],[C,C,0,C,0]],[0.8]])
T45.append([[[C,a,C,C,0],[0,0,b,C,0],[0,0,B,C,0],[C,o,0,a,0],[C,C,0,C,0]],[0.8]])
T45.append([[[C,C,0,C,0],[C,o,0,a,0],[0,0,b,C,0],[0,0,C,C,0],[C,a,C,C,0]],[0.8]])
T45.append([[[C,C,0,C,0],[C,o,0,a,0],[0,0,B,C,0],[0,0,b,C,0],[C,a,C,C,0]],[0.8]])

T63 = []

T63.append([[[C,a,C,0,0,0],[C,0,C,0,0,0],[B,o,B,0,0,0],[C,0,C,0,0,0],[C,0,C,0,0,0],[C,a,C,0,0,0]],[0.05]])
T63.append([[[C,a,C,0,0,0],[C,0,0,0,0,0],[C,0,0,0,0,0],[B,b,o,0,0,0],[C,0,0,0,0,0],[C,a,C,0,0,0]],[0.1]])
T63.append([[[C,a,C,0,0,0],[0,0,C,0,0,0],[0,0,C,0,0,0],[o,b,B,0,0,0],[0,0,C,0,0,0],[C,a,C,0,0,0]],[0.1]])


T7 = []

T7.append([[[C,a,C,0,0,0,0],[C,0,C,0,0,0,0],[C,0,C,0,0,0,0],[B,o,B,0,0,0,0],[C,0,C,0,0,0,0],[C,0,C,0,0,0,0],[C,a,C,0,0,0,0]],[0.05]])

C4 = []

C4.append([[[C,C,C,C],[a,o,o,a],[C,C,C,C],[C,C,C,C]],[0.9]])
C4.append([[[C,o,o,C],[a,b,B,a],[C,C,C,C],[C,C,C,C]],[0.9]])
C4.append([[[C,o,o,C],[a,B,b,a],[C,C,C,C],[C,C,C,C]],[0.9]])
C4.append([[[a,C,C,C],[C,o,C,C],[C,C,o,C],[C,C,C,a]],[0.9]])

C3 = []

C3.append([[[a,C,C],[C,o,C],[C,C,a]],[0.9]])
C3.append([[[C,C,C],[a,b,a],[C,o,C]],[0.9]])
C3.append([[[C,C,a],[C,C,o],[C,a,C]],[0.9]])
C3.append([[[a,C,C],[C,o,C],[C,a,C]],[0.9]])
C3.append([[[C,C,C],[a,o,a],[C,C,C]],[0.9]])


A4 = []

A4.append([[[C,C,C,C],
            [b,o,o,b],
            [C,C,C,C],
            [C,C,C,C]],[0.9]])
A4.append([[[C,C,C,C],
            [C,o,o,C],
            [b,C,C,b],
            [C,C,C,C]],[0.9]])
A4.append([[
            [b,C,C,C],
            [C,o,C,C],
            [C,C,o,C],
            [C,C,C,b]],[0.9]])

A5 = []

A5.append([[[C,C,C,C,C],
            [b,o,o,o,b],
            [C,C,C,C,C],
            [C,C,C,C,C],
            [C,C,C,C,C]],[0.75]])

A5.append([[[C,C,C,C,C],
            [C,o,o,o,C],
            [b,C,C,C,b],
            [C,C,C,C,C],
            [C,C,C,C,C]],[0.75]])

A5.append([[[b,C,C,C,C],
            [C,o,C,C,C],
            [C,C,o,C,C],
            [C,C,C,o,C],
            [C,C,C,C,b]],[0.75]])

A5.append([[[C,C,b,C,C],
            [C,C,o,C,C],
            [C,C,o,C,C],
            [C,C,o,C,C],
            [C,C,C,b,C]],[0.75]])

A5.append([[[C,C,b,C,C],
            [C,C,o,C,C],
            [C,C,o,C,C],
            [C,C,o,C,C],
            [C,b,C,C,C]],[0.75]])


A3 = []

A3.append([[[b,C,C],
            [C,o,C],
            [C,C,b]],[1]])
A3.append([[[C,C,C],
            [b,o,b],
            [C,C,C]],[1]])
A3.append([[[C,C,C],
            [b,a,b],
            [C,o,C]],[1]])
A3.append([[[C,C,b],
            [C,C,o],
            [C,b,C]],[1]])
A3.append([[[C,C,b],
            [b,o,C],
            [C,C,C]],[1]])
A3.append([[[b,C,C],
            [C,o,b],
            [C,C,C]],[1]])

A3.append([[[b,C,C],
            [o,C,C],
            [C,b,C]],[1]])

A3.append([[[C,C,b],
            [C,C,o],
            [C,b,C]],[1]])

NTR = []

NTR.append([[[R,S,C],
            [S,o,C],
            [C,C,C]],
            [-0.6]])

NTR.append([[[C,C,C],
            [C,o,S],
            [C,S,R]],
            [-0.6]])

NTR.append([[[C,S,R],
            [C,o,S],
            [C,C,C]],
            [-0.6]])

NTR.append([[[C,C,C],
            [S,o,C],
            [R,S,C]],
            [-0.6]])

NTR.append([[[S,S,S],
            [C,o,C],
            [C,C,C]]
            ,[-0.6]])

NT11 = []

NT11.append([[[C,C,C],[b,o,B],[b,b,B]],[-0.5]])

NT11.append([[[C,b,C],[b,o,b],[C,b,C]],[-0.5]])

BT42 = []

BT42.append([[[C,a,0,0],[b,a,0,0],[b,o,0,0],[C,a,0,0]],[0.7]])
BT42.append([[[C,a,0,0],[b,o,0,0],[b,a,0,0],[C,a,0,0]],[0.7]])
BT42.append([[[C,a,0,0],[C,o,0,0],[C,a,0,0],[C,a,0,0]],[0.2]])
BT42.append([[[C,a,0,0],[C,a,0,0],[C,o,0,0],[C,a,0,0]],[0.2]])
BT42.append([[[a,C,0,0],[a,C,0,0],[a,C,0,0],[o,C,0,0]],[0.6]])

BD42 = []

BD42.append([[[a,C,0,0],[a,b,0,0],[o,b,0,0],[a,C,0,0]],[0.7]])
BD42.append([[[a,C,0,0],[o,b,0,0],[a,b,0,0],[a,C,0,0]],[0.7]])
BD42.append([[[a,C,0,0],[o,C,0,0],[a,C,0,0],[a,C,0,0]],[0.2]])
BD42.append([[[a,C,0,0],[a,C,0,0],[o,C,0,0],[a,C,0,0]],[0.2]])
BD42.append([[[a,C,0,0],[a,C,0,0],[a,C,0,0],[o,C,0,0]],[0.6]])


BR42 = []

BR42.append([[[C,a,0,0],[b,a,0,0],[b,o,0,0],[C,a,0,0]],[0.7]])
BR42.append([[[C,a,0,0],[b,o,0,0],[b,a,0,0],[C,a,0,0]],[0.7]])
BR42.append([[[C,a,0,0],[C,o,0,0],[C,a,0,0],[C,a,0,0]],[0.2]])
BR42.append([[[C,a,0,0],[C,a,0,0],[C,o,0,0],[C,a,0,0]],[0.2]])
BR42.append([[[C,a,0,0],[C,a,0,0],[C,a,0,0],[C,o,0,0]],[0.6]])

BL42 = []

BL42.append([[[a,C,0,0],[a,b,0,0],[o,b,0,0],[a,C,0,0]],[0.7]])
BL42.append([[[a,C,0,0],[o,b,0,0],[a,b,0,0],[a,C,0,0]],[0.7]])
BL42.append([[[a,C,0,0],[o,C,0,0],[a,C,0,0],[a,C,0,0]],[0.2]])
BL42.append([[[a,C,0,0],[a,C,0,0],[o,C,0,0],[a,C,0,0]],[0.2]])
BL42.append([[[a,C,0,0],[a,C,0,0],[a,C,0,0],[o,C,0,0]],[0.6]])

TRA1 = []

TRA1.append([[[0,0,0,0],[0,0,b,0],[0,o,0,0],[0,0,0,0]],[0.1]])

TRA = []

TRA.append([[[0,B,0],[o,0,b],[0,b,0]],[0.2]])
TRA.append([[[0,o,0],[B,0,b],[0,b,0]],[0.2]])
TRA.append([[[0,o,0],[b,0,b],[0,b,0]],[0.3]])


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

def arr_c4(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[3]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))

def arr_c3(matrix):

    matrix.append(rotateMatrix(matrix[0]))
       
    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[3]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[4]))
   

def arr_a4(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[2]))


def arr_a5(matrix):

    matrix.append(rotateMatrix(matrix[0]))
    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[3]))
    matrix.append(rotateMatrix(matrix[4]))
   

def arr_a3(matrix):

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

    matrix.append(rotateMatrix(matrix[5]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[6]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

    matrix.append(rotateMatrix(matrix[7]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))


def arr_ntr3(matrix):

    

    matrix.append(rotateMatrix(matrix[4]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

def arr_nt11(matrix):

    matrix.append(rotateMatrix(matrix[0]))

    matrix.append(rotateMatrix(matrix[len(matrix)-1]))
    matrix.append(rotateMatrix(matrix[len(matrix)-1]))

def arrbt_42(matrix):

    matrix.append(rotateMatrix(matrix[0]))
    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[2]))

def arr_tra1(matrix):

    matrix.append(rotateMatrix(matrix[0]))
   

def arr_tra(matrix):
    matrix.append(rotateMatrix(matrix[1]))
    matrix.append(rotateMatrix(matrix[2]))
    matrix.append(rotateMatrix(matrix[3]))



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

Temp73 = do4x4Matrix(T7,"73")

T['T7x3'] = []
T['T3x7'] = []

for i in range(len(Temp73)):
    if len(Temp73[i][0]) == 7:
        T['T7x3'].append(Temp73[i])
    elif len(Temp73[i][0]) == 3:
        T['T3x7'].append(Temp73[i])


arr_c4(C4)
arr_c3(C3)

arr_a4(A4)
arr_a5(A5)
arr_a3(A3)

arr_ntr3(NTR)
arr_nt11(NT11)

arrbt_42(BT42)
arrbt_42(BD42)

arrbt_42(BL42)
arrbt_42(BR42)

arr_tra(TRA)
arr_tra1(TRA1)

BA['TBT4x2'] = []
Bemp42 = do4x4Matrix(BT42,"42")

for i in range(len(Bemp42)):
    if len(Bemp42[i][0]) == 2:
        BA['TBT4x2'].append(Bemp42[i])

BA['TBD4x2'] = []

Bemp42 = do4x4Matrix(BD42,"42")

for i in range(len(Bemp42)):
    if len(Bemp42[i][0]) == 2:
        BA['TBD4x2'].append(Bemp42[i])

BA['TBL4x2'] = []

Bemp42 = do4x4Matrix(BL42,"42")

for i in range(len(Bemp42)):
    if len(Bemp42[i][0]) == 4:
        BA['TBL4x2'].append(Bemp42[i])

#printDataM(BA['TBL4x2'])

BA['TBR4x2'] = []

Bemp42 = do4x4Matrix(BR42,"42")

for i in range(len(Bemp42)):
    if len(Bemp42[i][0]) == 4:
        BA['TBR4x2'].append(Bemp42[i])