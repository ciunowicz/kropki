import pygame, sys
from pygame.locals import *
import copy
import random
from template import T, A3, NTR, NT11, TR, TRA, TRA1, BA, ATR, CB2
#, CBR2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

Player1Color = BLUE
Player2Color = RED

WIDTH = 25
HEIGHT = 25

MARGIN = 15
LINEWIDTH = 2
LINECIRCWIDTH = 3
LINEHEIGHT = HEIGHT * 17 + MARGIN
DOT_CLK_AREA = 10

radius = 5

WINDOW_SIZE = [LINEHEIGHT + MARGIN, LINEHEIGHT + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)
screen.fill((230, 230, 230))

color = BLACK

COLS = 18
ROWS = 18
(TOP, RIGHT, DOWN, LEFT) = 1,2,3,4

grid, arr_tmp, tszn3, tsznr, tsztra, tsztra1, tszatr = ([] for i in range(7))
tszbl4G2, tszbr4G2, tszbt4G2, tszbd4G2, pointDoNotPut = ([] for i in range(5))
tszb2 = []
tszbr2 = []


tszdic = {'T3x3r': '3,3','T3x3': '3,3','T3x3_1': '3,3', 'T4x4': '4,4','T4x2': '4,2','T2x4': '2,4','T3x4': '3,4','T4x3': '4,3','T5x2': '5,2',
            'T2x5': '2,5','T4x5': '4,5','T5x4': '5,4','T5x3': '5,3','T5x3_2':'5,3','T5x3_1':'5,3','T3x5': '3,5','T3x5_2':'3,5','T3x5_1':'3,5','T6x3': '6,3','T3x6': '3,6','T7x3': '7,3','T3x7': '3,7'}

# 1 keopka gracz 1
# 2 kropka gracz 2
# 3 badane pole
# 4 kropka gracz 1 lub brak
# 5 kropka gracz 2 lub brak

a = 1
b = 2
o = 3
A = 4
B = 5
C = 6
S = 7
R = 8

DP = 3

board = [[0 for x in range(COLS)] for y in range(ROWS)]
arr_tmp = [[0 for x in range(COLS)] for y in range(ROWS)]

circuits, circuits_a, delepoints, ListCIPS, ListCPS, scorePoints, tsz, tszp = ({} for i in range(8))

points, ListAllPS, ListNoCPS, scorePointsNeg = ([] for i in range(4))


Player1 = 1
Player2 = 2
Player = Player1


def init():

    pygame.init()
    pygame.display.set_caption('Kropki')
   
    circuits[Player1] = []
    circuits[Player2] = []

    circuits_a[Player1] = []
    circuits_a[Player2] = []

    delepoints[Player1] = []
    delepoints[Player2] = []

    ListCPS[Player1] = []
    ListCPS[Player2] = []

    ListCIPS[Player1] = []
    ListCIPS[Player2] = []
   
    scorePoints[Player1] = []
    scorePoints[Player2] = []


    for row in range(ROWS):
        grid.append([])
        for column in range(COLS):
            grid[row].append([])

    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j].append(i*HEIGHT + MARGIN)
            grid[i][j].append(j*HEIGHT + MARGIN)
         

def delSepPoint(matrix, delePiontsArr, player):

    for i in range(ROWS):
        for j in range(COLS):
            point = 0
            if matrix[i][j] == player:
                if(i > 0 and matrix[i-1][j] == player): point+=1
                if(i < ROWS-1 and matrix[i+1][j] == player): point+=1
                if(j > 0 and matrix[i][j-1] == player): point+=1
                if(j < COLS-1 and matrix[i][j+1] == player): point+=1
# diagonal
                if(i > 0 and j > 0 and matrix[i-1][j-1] == player): point+=1
                if(i < ROWS-1 and j < COLS-1 and matrix[i+1][j+1] == player): point+=1
                if(i < ROWS-1 and j > 0 and matrix[i+1][j-1] == player): point+=1
                if(i > 0 and j < COLS-1 and matrix[i-1][j+1] == player): point+=1

                if point < 2:
                    matrix[i][j] = 0
                    delePiontsArr[player].append([i,j])
                    delSepPoint(matrix, delePiontsArr, player)
   


def noDots():

    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0 and [i,j] not in ListAllPS:
                return False

    return True


def delDuplicate(board):
        uniq = []

        for i in board:
            if not i in uniq:
                uniq.append(i)
       
        return uniq

def FloodFill(matrix,  x,y, lista, color, color2):
    #global arr_tmp
       
    if(x < 0 or x > ROWS-1 or y < 0 or y > COLS -1):
        return
    if matrix[x][y] != color:
        return
   
    matrix[x][y] = color2

    lista.append([x,y])
   
    FloodFill(matrix,x,y-1,lista, color, color2)
    FloodFill(matrix,x+1, y,lista, color, color2)
    FloodFill(matrix,x, y+1,lista, color, color2)
    FloodFill(matrix,x-1, y,lista, color, color2)


def setBound(dots, lista):
   
    listaRow = {}
    listaCol = {}
    listaRowMax = {}
    listaRowMin = {}
    listaColMax = {}
    listaColMin = {}
    listsRowCol = {}

   

    for i in lista:
     
        x = i[0]
        y = i[1]
       
        if x not in listaRow:
            listaRow[x] = []

        if y not in listaCol:
            listaCol[y] = []
     
    for i in lista:
         
         x = i[0]
         y = i[1]
         listaRow[x].append(i[1])
         listaCol[y].append(i[0])

    for i in listaRow:
        listaRowMax[i] =  max(listaRow[i])
        listaRowMin[i] =  min(listaRow[i])

    for i in listaCol:
        listaColMax[i] =  max(listaCol[i])
        listaColMin[i] =  min(listaCol[i])

    listsRowCol['rowmax'] =  listaRowMax
    listsRowCol['rowmin'] =  listaRowMin
    listsRowCol['colmax'] =  listaColMax
    listsRowCol['colmin'] =  listaColMin

    dots.append(listsRowCol)



def getScore(player):
    color1 = player
    color2 = Player1 if color1 == Player2 else Player2

    score = 0

    for mat in ListCIPS[player]:
        a1 = mat[0]
        b1 = mat[1]
        if board[a1][b1] == color2:
            score += 1
   
    return score
           


def canMove(x,y):

    all_points = ListCIPS[Player1] + ListCIPS[Player2]
   
    if(board[x][y] != 0):
        return False

    if [x, y] in all_points:
        return False
   

    return True


def isdotInside(lista, color):

    color2 = Player2 if color == Player1 else Player1

    for i in lista:
     
        x = i[0]
        y = i[1]

        if board[x][y] == color2:
            return True
   
    return False


def circleFill(a,b, player, matrix_point):
    listaKrop = []
    noBound = False
    global ListCIPS, ListAllPS
   
    if(arr_tmp[a][b] == player):
        return False
     
    delSepPoint(arr_tmp,delepoints, player)
   
    def delListCIPSP(player):
        tabd = []
        color1 = player
        color2 = Player1 if color1 == Player2 else Player2
       
        for pt in ListCIPS[color1]:
            if pt in ListCIPS[color2]:
                tabd.append(pt)
       
        for x in tabd:
            ListCIPS[color2].remove(x)

    col = Player1 if player == Player2 else Player2
    for i in range(ROWS):
        for j in range(COLS):
            if arr_tmp[i][j] == player and [i,j] in ListCIPS[col]:
                arr_tmp[i][j] = 0
            elif arr_tmp[i][j] != player:
                arr_tmp[i][j] = 0

    FloodFill(arr_tmp, a,b, listaKrop, 0,3)
     
    for i in listaKrop:
        if i[0] == 0 or i[1] == 0 or i[0] == ROWS-1 or i[1] == COLS-1:
            noBound = True
            break    
     

    if not noBound and isdotInside(listaKrop, player):

        matrix = [[0 for x in range(COLS)] for y in range(ROWS)]
        matrix2 = [[0 for x in range(COLS)] for y in range(ROWS)]
       
        for key in listaKrop:
            matrix[key[0]][key[1]] = player


        for i in range(ROWS):
            for j in range(COLS):
                if arr_tmp[i][j] == player:
                    matrix2[i][j] = player

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == player and not [i,j] in ListCIPS[player]:
                    matrix2[i][j] = player

        for i in range(ROWS):
            for j in range(COLS):
                if matrix2[i][j] == player:
                    if matrix[i][j] == player: continue
                    if i > 0 and matrix[i-1][j] == player: continue
                    if j > 0 and matrix[i][j-1] == player: continue
                    if i < ROWS - 1 and matrix[i+1][j] == player: continue
                    if j < COLS - 1 and matrix[i][j+1] == player: continue

                    matrix2[i][j] = 0                      


        kropczyny = []
        for i in range(ROWS):
            for j in range(COLS):
                if matrix2[i][j] == player:
                    kropczyny.append([i,j])
               
               
        setBound(points,kropczyny)
        setCircuits(points,player,ListAllPS,circuits,circuits_a)
           
        if listaKrop:
            Krop = delDuplicate(listaKrop)

            ListAllPS.extend(Krop)
            ListCPS[player].extend(Krop)
            ListCIPS[player].extend(Krop)
            ListCIPS[player] = delDuplicate(ListCIPS[player])
            delListCIPSP(player)

        return True
    else:
        matrix_point = copy.deepcopy(delDuplicate(listaKrop))
        return False



def setCircuits(dots,player, allPs, circ, circa):
   
    rowmin = []
    rowmax = []
    colmin = []
    colmax = []
    dots_circ = []
   
   
    point_ord = [0]


    def setCircuitsPath(pcirc):

       
        neighbour = {}

        def dfs(visited, graph, node):
            if node not in visited:
                visited.append(node)
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour)

        def makeNeighbour():
            nonlocal neighbour
            neighbour = {}
            matrix = [[0 for x in range(COLS)] for y in range(ROWS)]

            for key in pcirc:
                matrix[key[0]] [key[1]] = 1

            for i in range(len(pcirc)):
                neighbour[str(i)] = []
                num =  pcirc[i]

                #skos g??ra lewo
                if num[0]-1 >=0 and num[1]-1 >=0:
                    if matrix[num[0]-1][num[1]-1] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0]-1 and pcirc[j][1] == num[1]-1:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))

                #skos g??ra prawo
                if num[0]-1 >= 0 and num[1]+1 < len(matrix):
                    if matrix[num[0]-1][num[1]+1] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0]-1 and pcirc[j][1] == num[1]+1:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))
           
                #skos d???? lewo
                if num[0]+1 < len(matrix) and num[1]-1 >= 0:
                    if matrix[num[0]+1][num[1]-1] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0]+1 and pcirc[j][1] == num[1]-1:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))
           
                #skos d???? prawo
                if num[0]+1 < len(matrix) and num[1]+1 < len(matrix):
                    if matrix[num[0]+1][num[1]+1] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0]+1 and pcirc[j][1] == num[1]+1:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))
           
                #g??ra
                if num[0]-1 >= 0:
                    if matrix[num[0]-1][num[1]] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0]-1 and pcirc[j][1] == num[1]:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))
           
                #d????
                if num[0]+1 <len(matrix):
                    if matrix[num[0]+1][num[1]] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0]+1 and pcirc[j][1] == num[1]:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))

                #lewo
                if num[1]-1 >= 0:
                    if matrix[num[0]][num[1]-1] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0] and pcirc[j][1] == num[1]-1:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))

                #prawo
                if num[1]+1 <len(matrix):
                    if matrix[num[0]][num[1]+1] == 1:
                        idx = -1
                        for j in range(len(pcirc)):
                            if pcirc[j][0] == num[0] and pcirc[j][1] == num[1]+1:
                                idx = j
                                break
                        if idx >=0:
                            neighbour[str(i)].append(str(idx))


        def deleteMinPoints():
            matrix = [[0 for x in range(COLS)] for y in range(ROWS)]

            for key in pcirc:
                matrix[key[0]] [key[1]] = 1
           
            maxiV, miniV, maxiH, miniH, tabx, taby = ({} for i in range(6))
            tabpHmax, tabpHmin, tabVpmin, tabVpmax, MaxiMini = ([] for i in range(5))
           
            for i in range(ROWS):
                for key in pcirc:
                    if key[0] == i:
                       
                        if not i in tabx:
                            tabx[i] = {}
                            tabx[i]['tab'] = []
                            tabx[i]['point'] = []

                        tabx[i]['tab'].append(key[1])
                        tabx[i]['point'].append(key)
                   
                    if key[1] == i:
                       
                        if not i in taby:
                            taby[i] = {}
                            taby[i]['tab'] = []
                            taby[i]['point'] = []

                        taby[i]['tab'].append(key[0])
                        taby[i]['point'].append(key)
               
               

            for i in tabx:
                mini = min(tabx[i]['tab'])
                miniV[i] = []
                miniV[i].append(mini)
                maxi = max(tabx[i]['tab'])
                maxiV[i] = []
                maxiV[i].append(maxi)
               

            for i in taby:
                mini = min(taby[i]['tab'])
                miniH[i] = []
                miniH[i].append(mini)
                maxi = max(taby[i]['tab'])
                maxiH[i] = []
                maxiH[i].append(maxi)

           

            for key in maxiH:
                a = maxiH[key][0]
                b = key
               
                tabpHmax.append([a,b])
           
            for key in miniH:
                a = miniH[key][0]
                b = key
               
                tabpHmin.append([a,b])
                   
            for key in miniV:
                b = miniV[key][0]
                a = key
               
                tabVpmin.append([a,b])  

            for key in maxiV:
                b = maxiV[key][0]
                a = key
               
                tabVpmax.append([a,b])


            MaxiMini.extend(tabpHmax)
            MaxiMini.extend(tabpHmin)
            MaxiMini.extend(tabVpmin)
            MaxiMini.extend(tabVpmax)
            MaxiMini = delDuplicate(MaxiMini)
       
           

            for pt in pcirc:

                if pt not in MaxiMini:
                    pcirc.remove(pt)

     
        tab = []
        path = []

        makeNeighbour()    
        deleteMinPoints()
       
        makeNeighbour()
        dfs(path,neighbour,'0')
       
        for i in range(len(path)):
            tab.append(pcirc[int(path[i])])
           
        return tab        


    for i in dots:
        rowmin = i['rowmin']
        rowmax = i['rowmax']
        colmin = i['colmin']
        colmax = i['colmax']
   
    for i in rowmin:
        point = []
        point.append(i)
        point.append(rowmin[i])
        dots_circ.append(point)
   
    for i in rowmax:
        point = []
        point.append(i)
        point.append(rowmax[i])
        dots_circ.append(point)
   
    for i in colmin:
        point = []
        point.append(colmin[i])
        point.append(i)
        dots_circ.append(point)
   
    for i in colmax:
        point = []
        point.append(colmax[i])
        point.append(i)
        dots_circ.append(point)
   

    if dots_circ:
        dots_circ = delDuplicate(dots_circ)
       
        size_o = len(dots_circ)
        punkty = [[0 for x in range(size_o)] for y in range(size_o)]
       
       
        sorted = []
        for i in range(len(point_ord)):
            sorted.append(dots_circ[point_ord[i]])
       
        path = setCircuitsPath(dots_circ)
        circ[player].append(path)
        circa[player].extend(path)
        allPs.extend(path)
        allPs = delDuplicate(allPs)

   

def showMatrix():
    global arr_tmp
    arr_tmp = copy.deepcopy(board)
    player1_arr = []
    player2_arr = []

    if Player1 in ListCIPS:
        player1_arr = ListCIPS[Player1]
   
    if Player2 in ListCIPS:
        player2_arr = ListCIPS[Player2]

    for i in player1_arr:
        arr_tmp[i[0]][i[1]] = 3
    for i in player2_arr:
        arr_tmp[i[0]][i[1]] = 4
   
    for i in delepoints[Player1]:
        arr_tmp[i[0]][i[1]] = Player1
   
    for i in delepoints[Player2]:
        arr_tmp[i[0]][i[1]] = Player2




def getTpointByID(matrix, index):
   
    if index < 0 or index > len(matrix):
        return False
       
    return matrix[index]

def getTszbByID(matrix, index):
   
    if index < 0 or index > len(matrix):
        return False
       
    return matrix[index]


def getSzablonScorebyIdx(matrix, index):

    if index < 0 or index > len(matrix):
        return False
       
    return matrix[index][1][1]      
     
def getTbyIdx(matrix, index):

    if index < 0 or index > len(matrix):
        return False
       
    return matrix[index][0]


def getTscorebyIdx(matrix, index):

    if index < 0 or index > len(matrix):
        return False
       
    return matrix[index][1]



def makeSzablon2(matrix, szablon):
    sizeT = len(matrix)

    for t in range(sizeT):
        szb = getTbyIdx(matrix, t)
        sc = getTscorebyIdx(matrix, t)
        matrix2 = copy.deepcopy(szb)
        mt = []
        if not szb:
            continue

        sizeszb = len(szb)
        dP = []
        dP2 = []

        for i in range(sizeszb):
            for j in range(len(szb[i])):
                if matrix2[i][j] == DP:
                    matrix2[i][j] = 0
                   
                    dP.append([i,j])


        if len(dP) > 1:
            dP2.append(dP)
            dP2.extend(sc)

       
        mt.append(matrix2)
        if len(dP) > 1:
            mt.append(dP2)
        else:
            dP.extend(sc)
            mt.append(dP)

        szablon.append(mt)


def compare_szab(mat1, mat2):
        mSize = len(mat1)
        #to do poprawy przy prostok??tnych szablonach
        szbCol = len(mat2[0])
        count = mSize * szbCol
        num = 0

        for i in range(mSize):
            for j in range(len(mat1[i])):
                if  mat1[i][j] == mat2[i][j]:
                    num+=1
                elif mat2[i][j] == C:
                    num+=1
                elif mat1[i][j] == 1 and mat2[i][j] == A or mat1[i][j] == 0 and mat2[i][j] == A:
                    num+=1
                elif mat1[i][j] == 2 and mat2[i][j] == B or mat1[i][j] == 0 and mat2[i][j] == B:
                    num+=1

        if count == num:
            return True
        else:
            return False




def getcordDP(matrix, a, b):
        point = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i == a and j == b:
                    point.extend(matrix[i][j])
                    break
                if point:
                    break
        return point

def skipSzab(i,j):
        nast = False
        if [i,j] in ListCIPS[Player1] or [i,j] in ListCIPS[Player2]:
            nast = True
       
        return nast

def isCircuits(a,b, player):
        circ = circuits_a[player]
        if [a,b] in circ:
            return True
        else:
            return False

def isInCircuits(a,b, player):
    circ = ListCIPS[player]

    if [a,b] in circ:
        return True
    else:
        return False

def cutBoard(szb1, szb2, i,j,corn,szablon_size_row,szablon_size_col,game_player,board_player):

        tis  = False
        a = 0

        for k in range(i,i+szablon_size_row):            
                b = 0

                for l in range(j,j+szablon_size_col):
                   
                    if corn:
                        """ if isCircuits(k,l,Player1) or isCircuits(k,l,Player2):        
                            szb1[a][b] = S
                            tis = True
                        elif isInCircuits(k,l,Player1) or isInCircuits(k,l,Player2):
                            szb1[a][b] = R
                            tis2 = True """

                        if isCircuits(k,l,game_player):        
                            szb1[a][b] = S
                            tis = True
                        elif isInCircuits(k,l,game_player):
                            szb1[a][b] = R
                            tis = True
                        else:
                            szb1[a][b] = board_player[k][l]
                    else:
                        szb1[a][b] = board_player[k][l]
                        if skipSzab(k,l):
                            return False
                   
                    szb2[a][b].extend([k,l])

                    if not corn and [k,l] in ListNoCPS:
                        tis = True
                    b +=1
                a +=1
       
        if not corn:
            return tis
        else:
            if tis:
                return True
           
        return False


def addScore(szb1, szb2, poi, matrix):
       
        for z in range(len(matrix)):
            tab2 = getTszbByID(matrix,z)
           
           
            if compare_szab(szb1, tab2[0]):
                t2_point = tab2[len(tab2)-1]
               
               
               
                dtpoints = t2_point[0]
                dtscore = t2_point[1]
                p1 = dtpoints[0]
                p2 = dtpoints[1]
                matrixP = []
                point = []
               
                if isinstance(p1, int):
                    matrixP =  getcordDP(szb2, p1, p2)
                    point.append(matrixP)
               
                elif isinstance(p1, list):
                   
                    pointlist = []

                   

                    for i in range(len(dtpoints)):
                        tp = dtpoints[i]
                       

                        p1 = tp[0]
                        p2 = tp[1]
                        matrixP = getcordDP(szb2, p1, p2)
                       
                        pointlist.append(matrixP)


                    point.append(pointlist)
                   
               
                point.extend([dtscore])
                point.append(szb1)
                poi.append(point)


def skipSzabLessPoint(szab, rogi):
        licz = 0
        count = 2

        if rogi:
            count = 3

        for i in range(len(szab)):
            for j in range(len(szab[i])):
                if szab[i][j] > 0:
                    licz+=1
               
        if licz < count:
            return True
        else:
            return
           

def delDuplop(points, scPoints):
    skip = []
    # del duplcate points
    for  i in range(len(points)):
        cord = points[i][0]
        num = []  
        suma = points[i][1]
       
        if i in skip:
            continue

        for j in range(len(points)):
            cord2 = points[j][0]
            if j != i:
                if cord == cord2:
                    if suma <= points[j][1]:
                        suma = points[j][1]
                        skip.append(j)
                        num = []
                        num.extend(points[j])
        if num:
            scPoints.append(num)
        else:
            scPoints.append(points[i])


def doBoardSzab(board_player, szablon_size_row, szablon_size_col, matrix,scPoints, corner = False, spec = False, lessPoint = False):

    points = []
   
    game_player = Player2 if spec == False else Player1



    for i in range(ROWS-szablon_size_row + 1):
        for j in range(COLS-szablon_size_col + 1):

            if not corner and skipSzab(i,j):
                continue
           
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:  
                if not lessPoint and not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)
                elif lessPoint:
                    addScore(tszb, tab_b, points, matrix)


    if ROWS % szablon_size_row  != 0:
        i = ROWS - szablon_size_row
        for j in range(COLS - szablon_size_col + 1):
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:            
                if not lessPoint and not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)
                elif lessPoint:
                    addScore(tszb, tab_b, points, matrix)

    if COLS % szablon_size_col  != 0:
        j = COLS - szablon_size_col
        for i in range(ROWS - szablon_size_row + 1):
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:            
                if not lessPoint and not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)
                elif lessPoint:
                    addScore(tszb, tab_b, points, matrix)

    delDuplop(points, scPoints)

   

def doBoardSzabBand(board_player, szablon_size_row, szablon_size_col, matrix, scPoints, direction, corner = False, spec = False):

    points = []
    game_player = Player2 if spec == False else Player1

   
    # g??ra
    if direction == TOP:
        i = 0
        for j in range(COLS - szablon_size_col + 1):
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:            
                if not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)


    if direction == DOWN:
        i = ROWS - szablon_size_row
        for j in range(COLS - szablon_size_col + 1):
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:            
                if not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)


 
    #lewo
    if direction == LEFT:
        j  = 0
        for i in range(ROWS - szablon_size_row + 1):
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:            
                if not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)


   
    #prawo
    if direction == RIGHT:
        j = COLS - szablon_size_col
        for i in range(ROWS - szablon_size_row + 1):
            tszb = [[0 for x in range(szablon_size_col)] for y in range(szablon_size_row)]        
            tab_b = [[[] for x in range(szablon_size_col)] for y in range(szablon_size_row)]
 
            isek = cutBoard(tszb,tab_b,i,j,corner,szablon_size_row,szablon_size_col,game_player,board_player)
           
            if isek:            
                if not skipSzabLessPoint(tszb, corner):
                    addScore(tszb, tab_b, points, matrix)

    delDuplop(points, scPoints)
 


def makeMove(player,x,y):
    dotList = []
    ldot = False
    circ = False
    global arr_tmp, ListNoCPS
   
    for i in range(8):
        arr_tmp = copy.deepcopy(board)
        if ldot == True:
            circ = True
            break

        for dot in ListCIPS[player]:
            if arr_tmp[dot[0]][dot[1]] == player:
                arr_tmp[dot[0]][dot[1]] = 0
       
        if i == 0:
            if x > 1:
                if [x-1,y] not in dotList:
                    ldot = circleFill(x-1,y, player,dotList)
                    if ldot == True:
                        continue
        if i == 1:
            if x < ROWS - 2:
                if [x+1,y] not in dotList:
                    ldot = circleFill(x+1,y, player,dotList)
                    if ldot == True:
                        continue
        if i == 2:
            if y > 1:
                if [x,y-1] not in dotList:
                    ldot = circleFill(x,y-1, player,dotList)
                    if ldot == True:
                        continue
        if i == 3:
            if y < COLS - 2:
                if [x,y+1] not in dotList:
                    ldot = circleFill(x,y+1, player,dotList)
                    if ldot == True:
                        continue
        if i == 4:
            if x > 1 and y > 1:
                if [x-1,y-1] not in dotList:
                    ldot = circleFill(x-1,y-1, player,dotList)
                    if ldot == True:
                        continue
        if i == 5:
            if x > 1 and y < COLS - 2:
                if [x-1,y+1] not in dotList:
                    ldot = circleFill(x-1,y+1, player,dotList)
                    if ldot == True:
                        continue
        if i == 6:
            if x < ROWS - 2 and y > 1:
                if [x+1,y-1] not in dotList:
                    ldot = circleFill(x+1,y-1, player,dotList)
                    if ldot == True:
                        continue
        if i == 7:
            if x < ROWS - 2 and y < COLS - 2:
                if [x+1,y+1] not in dotList:
                    ldot = circleFill(x+1,y+1, player,dotList)
                    if ldot == True:
                        circ = True
                        continue
   
   
    if not circ:
        dotList = []
        arr_tmp = copy.deepcopy(board)
        player2 = Player2 if player == Player1 else Player1
        circleFill(x,y, player2,dotList)
   
    #Zliczanie kopek nie otoczonych i nie okr????onych

    ListNoCPS = []
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == Player1 or board[i][j] == Player2:
                if [i,j] not in ListAllPS:
                    ListNoCPS.append([i,j])

   
   


def circleFillBot(array_b, a,b, player, matrix_p):
    listaKrop = []
    noBound = False
   
    dpoints = {}
    dpoints[Player1] = []
    dpoints[Player2] = []


    def isdotInside2(lista, color, arr_cpy):
        global board
        color2 = Player2 if color == Player1 else Player1

        for i in lista:
       
            x = i[0]
            y = i[1]
           
            if board[x][y] == color2:
               
                return True
               
        return False
   

    if(array_b[a][b] == player):
        return False
     
    delSepPoint(array_b,dpoints, player)
   


    col = Player1 if player == Player2 else Player2
    for i in range(ROWS):
        for j in range(COLS):
            if array_b[i][j] == player and [i,j] in ListCIPS[col]:
                array_b[i][j] = 0
            elif array_b[i][j] != player:
                array_b[i][j] = 0

    FloodFill(array_b, a,b, listaKrop, 0,3)
     
    for i in listaKrop:
        if i[0] == 0 or i[1] == 0 or i[0] == ROWS-1 or i[1] == COLS-1:
            noBound = True
            break    
   
   

    if not noBound:

        matrix_p = copy.deepcopy(delDuplicate(listaKrop))
       
        if listaKrop and isdotInside2(listaKrop, player, board):
           
            return listaKrop
    else:
        return False


def setTemplateScore(boardPlayer,player):
    global scorePoints
   
    #scorePoints[player] = []
   

    for key in tszdic:
        #horn = False
        szbsize = tszdic[key].split(',')
        a1 = int(szbsize[0])
        b1 = int(szbsize[1])

        if player == Player2:
            if key == 'T3x3r':
                doBoardSzab(boardPlayer, a1, b1, tsz[key],scorePoints[player],True)
            else:
                doBoardSzab(boardPlayer, a1, b1, tsz[key],scorePoints[player])
       
    if player == Player2:
        doBoardSzabBand(boardPlayer, 4, 4, tszbl4G2,scorePoints[player], LEFT)
        doBoardSzabBand(boardPlayer, 4, 4, tszbr4G2,scorePoints[player], RIGHT)
        doBoardSzabBand(boardPlayer, 4, 4, tszbt4G2,scorePoints[player], TOP)
        doBoardSzabBand(boardPlayer, 4, 4, tszbd4G2,scorePoints[player], DOWN)

        doBoardSzab(boardPlayer, 3, 3, tszb2,scorePoints[player])
        #doBoardSzab(boardPlayer, 3, 3, tszbr2,scorePoints[player],True)

    else:
        doBoardSzab(boardPlayer, 3, 3, tszatr,scorePoints[player],True)

   
   


def BotCircuits(player,cpy_board,x,y):
    dotList = []
    ldot = []
    circ = False
    arr_b = []
   

    for i in range(8):
        arr_b = copy.deepcopy(cpy_board)
        if ldot:
            circ = True
            break


        col = Player1 if player == Player2 else Player2
     
       
       
        if i == 0:
            if x > 1:
                if [x-1,y] not in dotList:
                    ldot = circleFillBot(arr_b,x-1,y, player, dotList)
                    if ldot:
                        continue
        if i == 1:
            if x < ROWS - 2:
                if [x+1,y] not in dotList:
                    ldot = circleFillBot(arr_b,x+1,y, player, dotList)
                    if ldot:
                        continue
        if i == 2:
            if y > 1:
                if [x,y-1] not in dotList:
                    ldot = circleFillBot(arr_b,x,y-1, player, dotList)
                    if ldot:
                        continue
        if i == 3:
            if y < COLS - 2:
                if [x,y+1] not in dotList:
                    ldot = circleFillBot(arr_b,x,y+1, player, dotList)
                    if ldot:
                        continue
        if i == 4:
            if x > 1 and y > 1:
                if [x-1,y-1] not in dotList:
                    ldot = circleFillBot(arr_b,x-1,y-1, player, dotList)
                    if ldot:
                        continue
        if i == 5:
            if x > 1 and y < COLS - 2:
                if [x-1,y+1] not in dotList:
                    ldot = circleFillBot(arr_b,x-1,y+1, player, dotList)
                    if ldot:
                        continue
        if i == 6:
            if x < ROWS - 2 and y > 1:
                if [x+1,y-1] not in dotList:
                    ldot = circleFillBot(arr_b,x+1,y-1, player, dotList)
                    if ldot:
                        continue
        if i == 7:
            if x < ROWS - 2 and y < COLS - 2:
                if [x+1,y+1] not in dotList:
                    ldot = circleFillBot(arr_b, x+1,y+1, player, dotList)
                    if ldot:
                        circ = True
                        continue
   
   
    if not circ:
        return False
    else:
        return ldot
       
def maxScore(score):

        suma = -100000.0
        scx = -1
        scy = -1
        templ = []

        for j in range(len(score)):

            if suma < score[j][1] and score[j][1] > 0:
                suma = score[j][1]
                tb = score[j][0]
               
                scx = tb[0]
                scy = tb[1]
                if isinstance(scx, list):
                    scx = tb[0][0]
                if isinstance(scy, list):
                    scy = tb[0][1]
                   
                templ = copy.deepcopy(score[j][2])
           
        return [scx,scy,suma, templ]

def setZeroScore(score,ni,nj):
       
        for j in range(len(score)):
            tb = score[j][0]
            if ni == tb[0] and nj == tb[1]:
                score[j][1] = 0

def setLessScore(score,ni,nj, val):
       
        for j in range(len(score)):
            tb = score[j][0]
            if ni == tb[0] and nj == tb[1]:
                score[j][1] = val
       
def getmaxScoreWs(arr_cpy, player):
   
   
    tem = []
    sc = scorePoints[player]

   
    (x,y, maxsc,tem) = maxScore(sc)
   

    if x >= 0 and y >=0:
        return [x,y,maxsc,tem]
    else:
        return [-1,-1,-1,-1]

def randomWs(pla=Player2):

    freePoints = []
    farfreePoints = []

    op = Player2 if pla == Player1 else Player1
    (row, column) = -1,-1

    farfreePoints = sepPointsR(board, op)
    print("random len: ", len(farfreePoints))
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0 and canMove(i,j):
                freePoints.append([i,j])
           
    if len(freePoints) == 0:    
        return [row, column]
   
    n, column, row = (0,0,0)
   
    if len(farfreePoints) > 2:
        print("Jest")
        n = random.randint(0,len(farfreePoints)-1)
        column = farfreePoints[n][1]
        row = farfreePoints[n][0]
    else:

        n = random.randint(0,len(freePoints)-1)
        column = freePoints[n][1]
        row = freePoints[n][0]

    return [row, column]




def setZeroScoreNeg(score, scoreneg, val):
       
        for j in range(len(score)):
            tb = score[j][0]
            suma = score[j][1]
            if [tb[0],tb[1]] in scoreneg and suma < val:
                score[j][1] = 0



#do zmiany

def sepPointsR(matt, pla):

    all_points = ListCIPS[Player1] + ListCIPS[Player2]
    points1P = []
    points2P = []
    apointP = []
    availpointP = []
   
    def SepPoint1(matrix, player):
       
        pList = []

        for i in range(ROWS):
            for j in range(COLS):
                if [i,j] in all_points: continue

                if matrix[i][j] == 0:
                    if(i > 0 and matrix[i-1][j] == player): pList.append([i,j])
                    if(i < ROWS-1 and matrix[i+1][j] == player): pList.append([i,j])
                    if(j > 0 and matrix[i][j-1] == player): pList.append([i,j])
                    if(j < COLS-1 and matrix[i][j+1] == player): pList.append([i,j])
    # diagonal
                    if(i > 0 and j > 0 and matrix[i-1][j-1] == player): pList.append([i,j])
                    if(i < ROWS-1 and j < COLS-1 and matrix[i+1][j+1] == player): pList.append([i,j])
                    if(i < ROWS-1 and j > 0 and matrix[i+1][j-1] == player): pList.append([i,j])
                    if(i > 0 and j < COLS-1 and matrix[i-1][j+1] == player): pList.append([i,j])
       
        return pList


    def SepPoint2(matrix, player):
       
        pList = []

        for i in range(ROWS):
            for j in range(COLS):
                if [i,j] in all_points: continue

                if matrix[i][j] == 0:
                    if(i > 1 and matrix[i-2][j] == player): pList.append([i,j])
                    if(i < ROWS-2 and matrix[i+2][j] == player): pList.append([i,j])
                    if(j > 1 and matrix[i][j-2] == player): pList.append([i,j])
                    if(j < COLS-2 and matrix[i][j+2] == player): pList.append([i,j])
    # diagonal
                    if(i > 1 and j > 1 and matrix[i-2][j-2] == player): pList.append([i,j])
                    if(i < ROWS-2 and j < COLS-2 and matrix[i+2][j+2] == player): pList.append([i,j])
                    if(i < ROWS-2 and j > 1 and matrix[i+2][j-2] == player): pList.append([i,j])
                    if(i > 1 and j < COLS-2 and matrix[i-2][j+2] == player): pList.append([i,j])
       
        return pList
   
    points1P = delDuplicate(SepPoint1(matt, pla))
    points2P = delDuplicate(SepPoint2(matt, pla))

    apointP = delDuplicate(points1P + points2P)

   
    for i in range(ROWS):
            for j in range(COLS):
                if [i,j] in apointP or [i,j] in all_points: continue
                if matt[i][j] == 0:
                    availpointP.append([i,j])

   
    return availpointP


                   

def neighbourPoints4P(matrix, player, score):

    point2 = []
    arr_cpy = copy.deepcopy(matrix)

    all_points = ListCIPS[Player1] + ListCIPS[Player2]



    for i in range(ROWS):
        for j in range(COLS):
            if [i,j] in all_points:
                continue

            if arr_cpy[i][j] == player:
               
                if(i > 5 and arr_cpy[i-1][j] == 0 and arr_cpy[i-2][j] == 0 and arr_cpy[i-3][j] == 0 and arr_cpy[i-4][j] == 0 and arr_cpy[i-5][j] == player):
                    if [i-1,j] not in all_points and [i-2,j] not in all_points  and [i-3,j] not in all_points and [i-4,j] not in all_points:
                        point2.append([[i-1,j],[i-2,j],[i-3,j],[i-4,j]])

                if(j > 5 and arr_cpy[i][j-1] == 0 and arr_cpy[i][j-2] == 0 and arr_cpy[i][j-3] == 0 and arr_cpy[i][j-4] == 0 and arr_cpy[i][j-5] == player):
                    if [i,j-1] not in all_points and [i,j-2] not in all_points  and [i,j-3] not in all_points and [i,j-4] not in all_points:
                        point2.append([[i,j-1],[i,j-2],[i,j-3],[i,j-4]])

               
   
    #point3 = delDuplicate3(point2)
   

    for key in point2:
        arr_cpy = copy.deepcopy(matrix)
        circle = []
        tab = []

        i = key[0]
        j = key[1]
        k = key[2]
        l = key[3]
        x = arr_cpy[i[0]][i[1]]
        y = arr_cpy[j[0]][j[1]]
        z = arr_cpy[k[0]][k[1]]
        v = arr_cpy[l[0]][l[1]]

        arr_cpy[i[0]][i[1]] = player
        arr_cpy[j[0]][j[1]] = player
        arr_cpy[k[0]][k[1]] = player
        arr_cpy[l[0]][l[1]] = player

        circle = BotCircuits(player,arr_cpy,i[0],i[1])

        if circle:
            for key in circle:
                if key in all_points:
                    circle = []

        if circle:  
            sc =  0.70
            szb = [4]
            tab.append([i[0],i[1]])
            tab.extend([sc])
            tab.append(szb)
            score.append(tab)

        arr_cpy[i[0]][i[1]] = x
        arr_cpy[j[0]][j[1]] = y
        arr_cpy[k[0]][k[1]] = z
        arr_cpy[l[0]][l[1]] = v



#zmiana na 3
def neighbourPoints3P(matrix, player, score):

    point2 = []
    arr_cpy = copy.deepcopy(matrix)

    all_points = ListCIPS[Player1] + ListCIPS[Player2]

    def delDuplicate3(board):
        uniq = []

        for i in board:
            j = []
            j.extend([i[2],i[1],i[0]])
            if not i in uniq and j not in uniq:
                uniq.append(i)
       
        return uniq

    for i in range(ROWS):
        for j in range(COLS):
            if [i,j] in all_points:
                continue

            if arr_cpy[i][j] == player:
               
#ok
                if(i > 4 and j > 0 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-1] == 0 and arr_cpy[i-3][j-1] == 0 and (arr_cpy[i-4][j] == player or arr_cpy[i-4][j-1] == player or (j-2 >= 0 and arr_cpy[i-4][j-2] == player))):
                    if [i-1,j-1] not in all_points and [i-2,j-1] not in all_points  and [i-3,j-1] not in all_points:
                        point2.append([[i-1,j-1],[i-2,j-1],[i-3,j-1]])  
#ok
                if(i < ROWS-4 and arr_cpy[i+1][j-1] == 0 and arr_cpy[i+2][j-1] == 0 and arr_cpy[i+3][j-1] == 0 and (arr_cpy[i+4][j-1] == player or j-2 >=0 and arr_cpy[i+4][j-2] == player)):
                    if [i+1,j-1] not in all_points and [i+2,j-1] not in all_points and [i+3,j-1] not in all_points:
                        point2.append([[i+1,j-1],[i+2,j-1],[i+3,j-1]])
#ok                  
                if(i < ROWS-4 and arr_cpy[i+1][j] == 0 and arr_cpy[i+2][j] == 0 and arr_cpy[i+3][j] == 0 and (arr_cpy[i+4][j] == player or ((j > 0 and arr_cpy[i+4][j-1] == player) or (j < COLS-1 and arr_cpy[i+4][j+1] == player)))):
                    if [i+1,j] not in all_points and [i+2,j] not in all_points and [i+3,j] not in all_points:
                        point2.append([[i+1,j],[i+2,j],[i+3,j]])
#ok
                if(i > 4 and arr_cpy[i-1][j] == 0 and arr_cpy[i-2][j] == 0 and arr_cpy[i-3][j] == 0 and ((j > 0 and arr_cpy[i-4][j-1] == player) or (j < COLS -1 and arr_cpy[i-4][j+1] == player))):
                    if [i-1,j] not in all_points and [i-2,j] not in all_points  and [i-3,j] not in all_points:
                        point2.append([[i-1,j],[i-2,j],[i-3,j]])
#ok
                if(i < ROWS-4 and j < COLS-1 and arr_cpy[i+1][j+1] == 0 and arr_cpy[i+2][j+1] == 0 and arr_cpy[i+3][j+1] == 0 and ((arr_cpy[i+4][j] == player) or (j < COLS -1 and arr_cpy[i+4][j+1] == player) or (j > 0 and arr_cpy[i+4][j-1] == player))):
                    if [i+1,j+1] not in all_points and [i+2,j+1] not in all_points and [i+3,j+1] not in all_points:
                        point2.append([[i+1,j+1],[i+2,j+1],[i+3,j+1]])

#ok
                if(i >= 4 and j >= 1 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-1] == 0 and arr_cpy[i-3][j-1] == 0 and ((arr_cpy[i-4][j-1] == player) or (j >= 2 and arr_cpy[i-4][j-2] == player))):
                    if [i-1,j-1] not in all_points and [i-2,j-1] not in all_points and [i-3,j-1] not in all_points:
                        point2.append([[i-1,j-1],[i-2,j-1],[i-3,j-1]])

                 
                if(j > 4 and arr_cpy[i][j-1] == 0 and arr_cpy[i][j-2] == 0 and arr_cpy[i][j-3] == 0 and arr_cpy[i][j-4] == player):
                    if [i,j-1] not in all_points and [i,j-2] not in all_points and [i,j-3] not in all_points:
                        point2.append([[i,j-1],[i,j-2],[i,j-3]])

                if(j > 4 and i > 0 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-1][j-2] == 0 and arr_cpy[i-1][j-3] == 0 and arr_cpy[i][j-4] == player):
                    if [i-1,j-1] not in all_points and [i-1,j-2] not in all_points and [i-1,j-3] not in all_points:
                        point2.append([[i-1,j-1],[i-1,j-2],[i-1,j-3]])

                if(j > 4 and i < ROWS-1 and arr_cpy[i+1][j-1] == 0 and arr_cpy[i+1][j-2] == 0 and arr_cpy[i+1][j-3] == 0 and arr_cpy[i][j-4] == player):
                    if [i+1,j-1] not in all_points and [i+1,j-2] not in all_points and [i+1,j-3] not in all_points:
                        point2.append([[i+1,j-1],[i+1,j-2],[i+1,j-3]])              
               # diadonal
                if(i > 4 and j > 4 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-2] == 0 and arr_cpy[i-3][j-3] == 0 and (arr_cpy[i-4][j-4] == player or arr_cpy[i-4][j-3] == player)):
                    if [i-1,j-1] not in all_points and [i-2,j-2] not in all_points and [i-3,j-3] not in all_points:
                        point2.append([[i-1,j-1],[i-2,j-2],[i-3,j-3]])

                if(i < ROWS-4 and j < COLS-4 and arr_cpy[i+1][j+1] == 0 and arr_cpy[i+2][j+2] == 0 and arr_cpy[i+3][j+3] == 0 and (arr_cpy[i+4][j+4] == player or arr_cpy[i+4][j+3] == player)):
                    if [i+1,j+1] not in all_points and [i+2,j+2] not in all_points and [i+3,j+3] not in all_points:
                        point2.append([[i+1,j+1],[i+2,j+2],[i+3,j+3]])

               
   
    point3 = delDuplicate3(point2)
   

    for key in point3:
        arr_cpy = copy.deepcopy(matrix)
        circle = []
        tab = []

        i = key[0]
        j = key[1]
        k = key[2]
        x = arr_cpy[i[0]][i[1]]
        y = arr_cpy[j[0]][j[1]]
        z = arr_cpy[k[0]][k[1]]

        arr_cpy[i[0]][i[1]] = player
        arr_cpy[j[0]][j[1]] = player
        arr_cpy[k[0]][k[1]] = player

        circle = BotCircuits(player,arr_cpy,i[0],i[1])

        if circle:
            for key in circle:
                if key in all_points:
                    circle = []

        if circle:  
            #sc = float(len(circle)) + 0.65
            sc =  0.75
            szb = [3]
            tab.append([i[0],i[1]])
            tab.extend([sc])
            tab.append(szb)
            score.append(tab)


        arr_cpy[i[0]][i[1]] = x
        arr_cpy[j[0]][j[1]] = y
        arr_cpy[k[0]][k[1]] = z





def neighbourPoints2P(matrix, player, score):

    point2 = []
    arr_cpy = copy.deepcopy(matrix)

    all_points = ListCIPS[Player1] + ListCIPS[Player2]


    def delDuplicate2(board):
        uniq = []

        for i in board:
            j = []
            j.extend([i[1],i[0]])
            if not i in uniq and j not in uniq:
                uniq.append(i)
       
        return uniq

    for i in range(ROWS):
        for j in range(COLS):
            if [i,j] in all_points:
                continue

            if arr_cpy[i][j] == player:
                if(i > 2 and arr_cpy[i-1][j] == 0 and arr_cpy[i-2][j] == 0 and arr_cpy[i-3][j] == player):
                    if [i-1,j] not in all_points and [i-2,j] not in all_points:
                        point2.append([[i-1,j],[i-2,j]])
                    #tu
                    if i > 1 and j > 0 and [i-1,j-1] not in all_points and [i-2,j-1] not in all_points:
                        if arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-1] == 0:
                            point2.append([[i-1,j-1],[i-2,j-1]])
                    if i > 1 and j < COLS-2 and [i-1,j+1] not in all_points and [i-2,j+1] not in all_points:
                        if arr_cpy[i-1][j+1] == 0 and arr_cpy[i-2][j+1] == 0:
                            point2.append([[i-1,j+1],[i-2,j+1]])
                   
                """ if(i < ROWS-3 and arr_cpy[i+1][j] == 0 and arr_cpy[i+2][j] == 0 and arr_cpy[i+3][j] == player):
                    if [i+1,j] not in all_points and [i+2,j] not in all_points:
                        point2.append([[i+1,j],[i+2,j]]) """
                 
                if(j > 2 and arr_cpy[i][j-1] == 0 and arr_cpy[i][j-2] == 0 and arr_cpy[i][j-3] == player):
                    if [i,j-1] not in all_points and [i,j-2] not in all_points:
                        point2.append([[i,j-1],[i,j-2]])
                    #tu
                    if i > 0 and j > 1 and [i-1,j-1] not in all_points and [i-1,j-2] not in all_points:
                        if arr_cpy[i-1][j-1] == 0 and arr_cpy[i-1][j-2] == 0:
                            point2.append([[i-1,j-1],[i-1,j-2]])
                    if i < ROWS-1 and j > 1 and [i+1,j-1] not in all_points and [i+1,j-2] not in all_points:
                        if arr_cpy[i+1][j-1] == 0 and arr_cpy[i+1][j-2] == 0:
                            point2.append([[i+1,j-1],[i+1,j-2]])

               
                """ if(j < COLS-3 and arr_cpy[i][j+1] == 0 and arr_cpy[i][j+2] == 0 and arr_cpy[i][j+3] == player):
                    if [i,j+1] not in all_points and [i,j+2] not in all_points:
                        point2.append([[i,j+1],[i,j+2]]) """
               
#tu rebie
                if(i > 1 and j > 1 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-1][j-2] == 0 and arr_cpy[i][j-3] == player):
                    if [i-1,j-1] not in all_points and [i-i,j-2] not in all_points:
                        point2.append([[i-1,j-1],[i-1,j-2]])

                if(i < ROWS -1 and j > 1 and arr_cpy[i+1][j-1] == 0 and arr_cpy[i+1][j-2] == 0 and arr_cpy[i][j-3] == player):
                    if [i+1,j-1] not in all_points and [i+i,j-2] not in all_points:
                        point2.append([[i+1,j-1],[i+1,j-2]])

                 
                if(i > 1 and j > 1 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-2] == 0 and ((i > 2 and j > 2 and arr_cpy[i-3][j-3] == player) or (i > 2 and arr_cpy[i-3][j-2] == player))):
                    if [i-1,j-1] not in all_points and [i-2,j-2] not in all_points:
                        point2.append([[i-1,j-1],[i-2,j-2]])
               
                if(i < ROWS-2 and j < COLS-2 and arr_cpy[i+1][j+1] == 0 and arr_cpy[i+2][j+2] == 0 and ((i < ROWS-3 and j < COLS-3 and arr_cpy[i+3][j+3] == player) or (i < ROWS-3 and arr_cpy[i+3][j+2] == player))):
                    if [i+1,j+1] not in all_points and [i+2,j+2] not in all_points:
                        point2.append([[i+1,j+1],[i+2,j+2]])
                #dot??d
                   
                if(i < ROWS-3 and j > 3 and arr_cpy[i+1][j-1] == 0 and arr_cpy[i+2][j-2] == 0 and arr_cpy[i+3][j-3] == player):
                    if [i+1,j-1] not in all_points and [i+2,j-2] not in all_points:
                        point2.append([[i+1,j-1],[i+2,j-2]])
                   
                if(i > 3 and j < COLS-3 and arr_cpy[i-1][j+1] == 0 and arr_cpy[i-2][j+2] == 0 and arr_cpy[i-3][j+3] == player):
                    if [i-1,j+1] not in all_points and [i-2,j+2] not in all_points:
                        point2.append([[i-1,j+1],[i-2,j+2]])

               
                if(i < ROWS-3 and j > 0 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-1] == 0 and arr_cpy[i-3][j-1] == player):
                    if [i-1,j-1] not in all_points and [i-2,j-1] not in all_points:
                        point2.append([[i-1,j-1],[i-2,j-1]])
                 
                if(i < ROWS-3 and j < COLS-2 and arr_cpy[i-1][j+1] == 0 and arr_cpy[i-2][j+1] == 0 and arr_cpy[i-3][j+1] == player):
                    if [i-1,j+1] not in all_points and [i-2,j+1] not in all_points:
                        point2.append([[i-1,j+1],[i-2,j+1]])
               
                if(i < ROWS-2 and arr_cpy[i-1][j] == 0 and arr_cpy[i-2][j] == 0 and ((i < ROWS-3 and j > 0 and arr_cpy[i-3][j-1] == player) or (i < ROWS-3 and j < COLS-1 and arr_cpy[i-3][j+1] == player))):
                    if [i-1,j] not in all_points and [i-2,j] not in all_points:
                        point2.append([[i-1,j],[i-2,j]])


                if((j < COLS-2 and i > 0 and arr_cpy[i-1][j+1] == 0 and arr_cpy[i-1][j+2] == 0) and ((j < COLS-3 and arr_cpy[i-1][j+3] == player) or (j < COLS-3 and i > 1 and arr_cpy[i-2][j+3] == player))):
                    if [i-1,j+1] not in all_points and [i-1,j+2] not in all_points:
                        point2.append([[i-1,j+1],[i-1,j+2]])

                if(i < ROWS-1 and j < COLS-2 and arr_cpy[i+1][j+1] == 0 and arr_cpy[i+1][j+2] == 0 and ((j < COLS-3 and arr_cpy[i+1][j+3] == player) or (i < ROWS-2 and j < COLS-3 and arr_cpy[i+2][j+3] == player))):
                    if [i+1,j+1] not in all_points and [i+1,j+2] not in all_points:
                        point2.append([[i+1,j+1],[i+1,j+2]])
               
                if(j < COLS-2 and arr_cpy[i][j+1] == 0 and arr_cpy[i][j+2] == 0 and ((i > 0  and j < COLS-3 and arr_cpy[i-1][j+3] == player) or (i < ROWS-1 and j < COLS-3 and arr_cpy[i+1][j+3] == player))):
                    if [i,j+1] not in all_points and [i,j+2] not in all_points:
                        point2.append([[i,j+1],[i,j+2]])
               
                if(i > 1 and j > 0 and arr_cpy[i-1][j-1] == 0 and arr_cpy[i-2][j-1] == 0 and ((i > 2 and arr_cpy[i-3][j-1] == player) or ( i > 2 and j > 1 and arr_cpy[i-3][j-2] == player))):
                    if [i-1,j-1] not in all_points and [i-2,j-1] not in all_points:
                        point2.append([[i-1,j-1],[i-2,j-1]])

                if(i > 1 and arr_cpy[i-1][j] == 0 and arr_cpy[i-2][j] == 0 and ((i > 2 and j > 0 and arr_cpy[i-3][j-1] == player) or (i > 2 and j < COLS-1 and arr_cpy[i-3][j+1] == player))):
                    if [i-1,j] not in all_points and [i-2,j] not in all_points:
                        point2.append([[i-1,j],[i-2,j]])

                if(i > 1 and j < COLS-1 and arr_cpy[i-1][j+1] == 0 and arr_cpy[i-2][j+1] == 0 and ((i > 2 and arr_cpy[i-3][j+1] == player) or (i > 2 and j < COLS-2 and arr_cpy[i-3][j+2] == player))):
                    if [i-1,j+1] not in all_points and [i-2,j+1] not in all_points:
                        point2.append([[i-1,j+1],[i-2,j+1]])
                   
                   

   
    point2 = delDuplicate2(point2)
   
    for key in point2:
        arr_cpy = copy.deepcopy(matrix)
        circle = []
        tab = []

        i = key[0]
        j = key[1]
        x = arr_cpy[i[0]][i[1]]
        y = arr_cpy[j[0]][j[1]]

        arr_cpy[i[0]][i[1]] = player
        arr_cpy[j[0]][j[1]] = player

        circle = BotCircuits(player,arr_cpy,i[0],i[1])

        if circle:
            for key in circle:
                if key in all_points:
                    circle = []
                    break

        if circle:  
            #sc = float(len(circle)) + 0.75
            sc = 0.8
            szb = [2]
            tab.append([i[0],i[1]])
            tab.extend([sc])
            tab.append(szb)
            score.append(tab)


        arr_cpy[i[0]][i[1]] = x
        arr_cpy[j[0]][j[1]] = y



def neighbourPoints(matrix, player, score):

    nei = []
    chkPoints = []
    arr_cpy = copy.deepcopy(matrix)
    all_points = []
    circle = []
    all_points = circuits_a[Player1] + circuits_a[Player2] + ListCIPS[Player1] + ListCIPS[Player2]

    for i in range(ROWS):
        for j in range(COLS):
            point = 0
            if [i,j] in all_points:
                continue

            if arr_cpy[i][j] == player:
                if(i > 0 and arr_cpy[i-1][j] == player): point+=1
                if(i < ROWS-1 and arr_cpy[i+1][j] == player): point+=1
                if(j > 0 and arr_cpy[i][j-1] == player): point+=1
                if(j < COLS-1 and arr_cpy[i][j+1] == player): point+=1
                if(i > 0 and j > 0 and arr_cpy[i-1][j-1] == player): point+=1
                if(i < ROWS-1 and j < COLS-1 and arr_cpy[i+1][j+1] == player): point+=1
                if(i < ROWS-1 and j > 0 and arr_cpy[i+1][j-1] == player): point+=1
                if(i > 0 and j < COLS-1 and arr_cpy[i-1][j+1] == player): point+=1

                if point <= 4 and point > 0:
                    nei.append([i,j])
 

    for key in nei:

        i = key[0]
        j = key[1]

        if [i,j] in all_points:
                continue

        if(i > 0 and arr_cpy[i-1][j] == 0 and [i-1,j] not in all_points): chkPoints.append([i-1,j])
        if(i < ROWS-1 and arr_cpy[i+1][j] == 0 and [i+1,j] not in all_points): chkPoints.append([i+1,j])
        if(j > 0 and arr_cpy[i][j-1] == 0 and [i,j-1] not in all_points): chkPoints.append([i,j-1])
        if(j < COLS-1 and arr_cpy[i][j+1] == 0) and [i,j+1] not in all_points: chkPoints.append([i,j+1])
        if(i > 0 and j > 0 and arr_cpy[i-1][j-1] == 0 and [i-1,j-1] not in all_points): chkPoints.append([i-1,j-1])
        if(i < ROWS-1 and j < COLS-1 and arr_cpy[i+1][j+1] == 0 and [i+1,j+1] not in all_points): chkPoints.append([i+1,j+1])
        if(i < ROWS-1 and j > 0 and arr_cpy[i+1][j-1] == 0 and [i+1,j-1] not in all_points): chkPoints.append([i+1,j-1])
        if(i > 0 and j < COLS-1 and arr_cpy[i-1][j+1] == 0 and [i-1,j+1] not in all_points): chkPoints.append([i-1,j+1])


    chkPoints = delDuplicate(chkPoints)
       
    for key in chkPoints:
        arr_cpy = copy.deepcopy(matrix)
        circle = []
        i = key[0]
        j = key[1]
        arr_cpy[i][j] = player
        circle = BotCircuits(player,arr_cpy,i,j)
        arr_cpy[i][j] = 0
        dois = False
        tab = []

        if circle:
           
            if isinstance(circle[0], int):

                circ = []
                circ.append(copy.deepcopy(circle))
                circle = circ

            for key in circle:
                if key in all_points:
                    circle = []
                    break
       
       
            if player == Player2:

                sc = len(circle) + 0.2
                szb = [0]
                tab.append([i,j])
                tab.extend([sc])
                tab.append(szb)
                score.append(tab)
                continue

       
            if player == Player1:

                circle2 = []
                if(i > 0 and [i-1,j] in chkPoints):
                    arr_cpy[i-1][j] = 1
                    circle2 = BotCircuits(player,arr_cpy,i-1,j)

                    if circle2:
                        for key in circle2:
                            if key in all_points:
                                circle2 = []

                    if circle2:
                        dois = True
                        setZeroScore(score,i,j)
                        setZeroScore(score,i-1,j)
                    arr_cpy[i-1][j] = 0

                elif(i < ROWS-1 and [i+1,j] in chkPoints):
                    arr_cpy[i+1][j] = 1
                    circle2 = BotCircuits(player,arr_cpy,i+1,j)

                    if circle2:
                        for key in circle2:
                            if key in all_points:
                                circle2 = []

                    if circle2:
                        dois = True
                        setZeroScore(score,i,j)
                        setZeroScore(score,i+1,j)
                    arr_cpy[i+1][j] = 0

                elif(j > 0 and [i,j-1] in chkPoints):
                    arr_cpy[i][j-1] = 1
                    circle2 = BotCircuits(player,arr_cpy,i,j-1)
                       
                    if circle2:
                        for key in circle2:
                            if key in all_points:
                                circle2 = []
                    if circle2:
                        dois = True
                        setZeroScore(score,i,j)
                        setZeroScore(score,i,j-1)
                    arr_cpy[i][j-1] = 0
                   
                elif(j < COLS-1 and [i,j+1] in chkPoints):
                    arr_cpy[i][j+1] = 1
                    circle2 = BotCircuits(player,arr_cpy,i,j+1)
                   
                    if circle2:
                        for key in circle2:
                            if key in all_points:
                                circle2 = []

                    if circle2:
                        dois = True
                        setZeroScore(score,i,j)
                        setZeroScore(score,i,j+1)
                    arr_cpy[i][j+1] = 0
       
       
        tab = []
       
        if circle and player == Player1 and dois:
           
            setZeroScore(score,i,j)

        elif circle and player == Player1 and not dois:

            sc = len(circle) + 0.1
            szb = [0]
            tab.append([i,j])
            tab.extend([sc])
            tab.append(szb)
            score.append(tab)
           


def addNegScore(arr_cpy):
    score = []
    scPoints = []

    doBoardSzab(arr_cpy, 3, 3, tszn3, score)
    doBoardSzab(arr_cpy, 3, 3, tsznr, score, True, True, True)

    for key in score:
        scPoints.append(key[0])
   
    return scPoints


def findCirc(arr_cpy,player, scorep):
   
    score = []
    cpy_a = copy.deepcopy(arr_cpy)

    all_points = circuits_a[Player1] + circuits_a[Player2] + ListCIPS[Player1] + ListCIPS[Player2]
   
    def checkCircle(arr_points, i,j):
        isRound = False
        arr_points[i][j] = 0

        if(not isRound and i > 0 and arr_points[i-1][j] == 0 and [i-1,j] not in all_points):
            arr_points[i-1][j] = Player1
            circle2 = BotCircuits(player,arr_points,i-1,j)
            arr_points[i-1][j] = 0
                               
            if circle2:
                isRound = True
                for key in circle2:
                    if key in all_points:
                        circle2 = []
                        isRound = False
                   
                if isRound:
                    arr_points = copy.deepcopy(cpy_a)
                    return True


        if(not isRound and i < ROWS-1 and arr_points[i+1][j] == 0 and [i+1,j] not in all_points):
            arr_points[i+1][j] = Player1
            circle2 = BotCircuits(player,arr_points,i+1,j)
            arr_points[i+1][j] = 0
                               
            if circle2:
                isRound = True
                for key in circle2:
                    if key in all_points:
                        circle2 = []
                        isRound = False
               
                if isRound:
                    arr_points = copy.deepcopy(cpy_a)
                    return True


        if(not isRound and j > 0 and arr_points[i][j-1] == 0 and [i,j-1] not in all_points):
            arr_points[i][j-1] = Player1
            circle2 = BotCircuits(player,arr_points,i,j-1)
            arr_points[i][j-1] = 0
                               
            if circle2:
                isRound = True
                for key in circle2:
                    if key in all_points:
                        circle2 = []
                        isRound = False
               
                if isRound:
                    arr_points = copy.deepcopy(cpy_a)
                    return True

                           
        if(not isRound and j < COLS-1 and arr_points[i][j+1] == 0 and [i,j+1] not in all_points):
            arr_points[i][j+1] = Player1
            circle2 = BotCircuits(player,arr_points,i,j+1)
            arr_points[i][j+1] = 0
                               
            if circle2:
                isRound = True
                for key in circle2:
                    if key in all_points:
                        circle2 = []
                        isRound = False
               
                if isRound:
                    arr_points = copy.deepcopy(cpy_a)
                    return True

        arr_points = copy.deepcopy(cpy_a)
        return False

    def addToScore(player,score):
       

        if score:
            for pt in score:
               
                if isinstance(pt[0][0], list) and len(pt[0]) == 2:

                    if player == Player1 and pt[1] == 0.0001 or player == Player2 and pt[1] != 0.0001:
                        tab = []
                        tmpx = pt[0][0]
                        tmpx2 = pt[0][1]
                        x1 = tmpx[0]
                        y1 = tmpx[1]
                        x2 = tmpx2[0]
                        y2 = tmpx2[1]
                        x = arr_cpy[x1][y1]
                        y = arr_cpy[x2][y2]
                        arr_cpy[x1][y1] = player
                        arr_cpy[x2][y2] = player

                        circle = BotCircuits(player,arr_cpy,x2,y2)

                       
                   

                        if circle:
                            for key in circle:
                                if key in all_points:
                                    circle = []
                                    break

                            if not circle:
                                return

                            if player == Player2:
                               
                                sc = len(circle)
                                #to jest szablon
                                szb = pt[2]
           
                                if player == Player2:
                                    pt[1] = 0.9

                                n = random.randint(0,1)
                       
                                num = pt[0][n]
                                tab.append(num)
                                tab.extend([sc])
                                tab.append(szb)
                                scorep.append(tab)

                                                     
                            #tutaj zerowa?? zrobic jako funkcj?? if circle

                            is_circle = checkCircle(arr_cpy,x1,y1)
                            if is_circle:

                                sc = 0
                                #to jest szablon
                                szb = pt[2]
                                num = [x1,y1]
                                tab.append(num)
                                tab.extend([sc])
                                tab.append(szb)
                                scorep.append(tab)

                                is_circle2 = checkCircle(arr_cpy,x2,y2)
                                if is_circle2:
                                    sc = 0
                                    #to jest szablon
                                    szb = pt[2]
                                    num = [x2,y2]
                                    tab.append(num)
                                    tab.extend([sc])
                                    tab.append(szb)
                                    scorep.append(tab)

                                else:
                                    sc = len(circle)
                                    #to jest szablon
                                    szb = pt[2]          
                                    num = [x2,y2]
                                    tab.append(num)
                                    tab.extend([sc])
                                    tab.append(szb)
                                    scorep.append(tab)

                            else:
                                sc = len(circle)
                                #to jest szablon
                                szb = pt[2]
                       
                                num = [x1,y1]
                                tab.append(num)
                                tab.extend([sc])
                                tab.append(szb)
                                scorep.append(tab)



                        arr_cpy[x1][y1] = x
                        arr_cpy[x2][y2] = y

                   
           
    addToScore(player,scorep)
    arr_cpy = copy.deepcopy(cpy_a)
    neighbourPoints4P(arr_cpy, player, scorep)
    neighbourPoints3P(arr_cpy, player, scorep)
    neighbourPoints2P(arr_cpy, player, scorep)
    neighbourPoints(arr_cpy, player, scorep)
   




def findTra(br):
    global scoreTra
    scoreTra = []
   
    doBoardSzab(br, 4, 4, tsztra1, scoreTra,False,False,True)
    doBoardSzab(br, 3, 3, tsztra, scoreTra,False,False,True)
   

    (x,y, maxsc, tb) = maxScore(scoreTra)
   
    if x >= 0:
        return [x,y,maxsc]
    else:
        return [-1,-1,-1]



def moveBot(player):
   
    scoreNeg = []
   
    arr_tmp = copy.deepcopy(board)
    sc = scorePoints[player]

    scoreNeg = addNegScore(arr_tmp)
   
    setZeroScoreNeg(sc, scoreNeg, 0.9)

    def trap_or_rand(scNeg):

        def getxy():

            (x1,y1,sum1) = findTra(arr_tmp)
            if x1 >= 0:
                (r, c) = x1, y1
            else:
                (r, c) = randomWs(player)
           
            return [r,c]


        (row, column) = randomWs(player)
        if [row,column] in scNeg:
            xy = getxy()
            row = xy[0]
            column = xy[1]
           
        else:
            xy = getxy()
            row = xy[0]
            column = xy[1]

       
        return [row, column]


    scWs = getmaxScoreWs(arr_tmp,player)
    column = scWs[1]
    row = scWs[0]
    #suma = float(scWs[2])
    #templatek = scWs[3]

    if row < 0 or column < 0 or not canMove(row,column):
                               
        # je??li nie ma na szablonach losowo

        (row, column) = trap_or_rand(scoreNeg)

               
    return [row,column]



init()


for key in tszdic:
    tsz[key] = []
    tszp[key] = []
    makeSzablon2(T[key],tsz[key])


makeSzablon2(NT11,tszn3)
makeSzablon2(NTR,tsznr)

makeSzablon2(ATR,tszatr)

makeSzablon2(CB2,tszb2)

#makeSzablon2(CBR2,tszbr2)

#szablony do spr. przy bandzie
makeSzablon2(BA['TBL4x2'],tszbl4G2)
makeSzablon2(BA['TBR4x2'],tszbr4G2)
makeSzablon2(BA['TBT4x2'],tszbt4G2)
makeSzablon2(BA['TBD4x2'],tszbd4G2)


makeSzablon2(TRA,tsztra)
makeSzablon2(TRA1,tsztra1)

 
while True: # main loop

    for i in range(ROWS):
        if( i == 0):
            pygame.draw.line(screen, color, (MARGIN,MARGIN), (LINEHEIGHT,i*HEIGHT + MARGIN), LINEWIDTH)
        else:
            pygame.draw.line(screen, color, (MARGIN,i*HEIGHT + MARGIN ), (LINEHEIGHT,i*HEIGHT + MARGIN), LINEWIDTH)
           
       
    for i in range(COLS):
        if i == 0:
            pygame.draw.line(screen, color, (MARGIN , MARGIN   ) , (MARGIN, LINEHEIGHT), LINEWIDTH)  
        else:  
            pygame.draw.line(screen, color, (i*WIDTH + MARGIN , MARGIN) , (i*WIDTH + MARGIN  , LINEHEIGHT), LINEWIDTH)
   
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] != 0:
                y = grid[i][j][0]
                x = grid[i][j][1]
                if board[i][j] == Player1:
                    pygame.draw.circle(screen, Player1Color, (x,y),radius)
                else:
                    pygame.draw.circle(screen, Player2Color, (x,y),radius)


    for player in range(1,3):
        Color = Player1Color if player == Player1 else Player2Color
        for  player1Circ in circuits[player]:
            for i in range(len(player1Circ)-1):
                x1 = grid[player1Circ[i][0]]   [player1Circ[i][1]] [1]
                y1 = grid[player1Circ[i][0]]   [player1Circ[i][1]] [0]
                x2 = grid[player1Circ[i+1][0]] [player1Circ[i+1][1]][1]
                y2 = grid[player1Circ[i+1][0]] [player1Circ[i+1][1]][0]
                pygame.draw.line(screen, Color, [x1, y1],[x2,y2],LINECIRCWIDTH)

                if i == len(player1Circ)-2:
                    x1 = grid[player1Circ[0][0]]   [player1Circ[0][1]] [1]
                    y1 = grid[player1Circ[0][0]]   [player1Circ[0][1]] [0]
                    x2 = grid[player1Circ[len(player1Circ)-1][0]] [player1Circ[len(player1Circ)-1][1]][1]
                    y2 = grid[player1Circ[len(player1Circ)-1][0]] [player1Circ[len(player1Circ)-1][1]][0]
                    pygame.draw.line(screen, Color, [x1, y1],[x2,y2],LINECIRCWIDTH)


    for event in pygame.event.get():
        # draws the arc
             
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if noDots():
                print("Brok kropczyn koniec gry")
            else:                                
                pos = pygame.mouse.get_pos()
                column = pos[0] // (WIDTH)
                row = pos[1] // (HEIGHT)

                if row > ROWS - 1 or column > COLS - 1: continue
       
                y = grid[row][column][0]
                x = grid[row][column][1]

               
           
                if x >= pos[0] - DOT_CLK_AREA  and  x <= pos[0] + DOT_CLK_AREA and y <= pos[1] + DOT_CLK_AREA and y >= pos[1] - DOT_CLK_AREA:


                    if canMove(row,column):
                        board[row][column] = Player
                   
                    else: continue

                    scorePoints[Player1] = []
                    scorePoints[Player2] = []

                    """ setTemplateScore(board,Player2)
                    findCirc(board,Player, scorePoints[Player2])
                    makeMove(Player,row,column)

                    Player = Player2 if Player == Player1 else Player1 """
                   
                    makeMove(Player,row,column)
                    #findCirc(board,Player, scorePoints[Player2])
                    arr_tmp = copy.deepcopy(board)
                    setTemplateScore(arr_tmp,Player2)
                    arr_tmp = copy.deepcopy(board)
                    findCirc(arr_tmp,Player, scorePoints[Player2])

                    Player = Player2
                    arr_tmp = copy.deepcopy(board)
                    findCirc(arr_tmp,Player, scorePoints[Player2])
                    bX = moveBot(Player)
                    row = bX[0]
                    column = bX[1]

                    if row >=0:
                        board[row][column] = Player
                    else:
                        Player = Player1
                        continue                  
                   
               #bot
                    makeMove(Player,row,column)
                    arr_tmp = copy.deepcopy(board)
                    Player = Player1
 
                    #Player = Player2 if Player == Player1 else Player1
   
                    #all_points = ListCIPS[Player1] + ListCIPS[Player2]
                    #print("list: ", all_points)
                   


    pygame.display.update()