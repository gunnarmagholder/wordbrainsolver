
# col = spalten
# row = zeilen
# Bei Adressierung immer col, row

class wbSolver:
    def __init__(self, fieldArr, wordArr):
        self.field = fieldArr
        self.words = wordArr
        self.childenArr = []
        self.foundWordPaths = {}

    def __str__(self):
        returnString = ""
        for rowrunner in self.field:
            returnString = returnString + ','.join(rowrunner)
            returnString = returnString + '\n\r'
        return returnString

    def addChild(self,fieldArr,wordArr):
        wbChild = wbSolver(fieldArr,wordArr)
        self.childenArr.append(wbChild)

    def scanWord(self,word, pathArr):
        returnArr = []
        if len(pathArr) == 0:
            # erster Durchlauf
            # Suche nach dem Anfangsbuchstaben im gesamten Feld
            foundFirstChar = self.getScannedCoordsForChar(word[0])
            if foundFirstChar == []:
                returnArr = []
            else:
                for foundCoord in foundFirstChar:
                    thisPath = []
                    thisPath.append(foundCoord)
                    thisPath.append(self.scanWord(word[1:], thisPath))
                    returnArr.append(thisPath)
        else:
            if(len(word)==0):
                return
            lastCoord = pathArr(len(pathArr)-1)
            foundFirstChar = self.getCharAtAdjacentRect(lastCoord[0],lastCoord[1],word[0])
            if foundFirstChar == []:
                return False
            for foundCoord in foundFirstChar:
                thisPath = []
                thisPath.append(foundCoord)
                thisPath.append(self.scanWord(word[1:], thisPath))
                returnArr.append(thisPath)
            # nicht erster Durchlauf
            # Suche nach dem nächsten Buchstaben im angrenzenden Bereich

        return returnArr
    def getCharAtPos(self,col, row):
        thisRow = self.getRow(row)
        return self.getChar(thisRow,col)

    def getRow(self,row):
        cols = len(self.field[0])
        emptyArr = [' '] * cols
        if (row < 0) or (row >= len(self.field)):
            return emptyArr
        return self.field[row]

    def getChar(self,row,col):
        if(col < 0) or (col >= len(row)):
            return ' '
        return row[col]

    def getScannedCoordsForChar(self,char):
        returnArr = []
        for rowrunner in range(len(self.field)):
            row = self.getRow(rowrunner)
            for colrunner in range(len(row)):
                if self.getCharAtPos(colrunner,rowrunner) == char:
                    returnArr.append([colrunner, rowrunner])
        return returnArr

    def strikeOutChar(self,col,row):
        for rowrunner in range(row,-1,-1):
            if(rowrunner == 0):
                self.field[rowrunner][col] = ' '
            else:
                self.field[rowrunner][col] = self.getCharAtPos(col, row-1)

    def getCharAtAdjacentRect(self,col, row, char):
        returnArr = []
        if (self.getCharAtPos(col-1,row-1)) == char:
            returnArr.append([col-1, row-1])
        if (self.getCharAtPos(col, row - 1)) == char:
            returnArr.append([col, row - 1])
        if (self.getCharAtPos(col + 1, row - 1)) == char:
            returnArr.append([col + 1, row - 1])
        if (self.getCharAtPos(col-1,row)) == char:
            returnArr.append([col-1, row])
        if (self.getCharAtPos(col + 1, row)) == char:
            returnArr.append([col + 1, row])
        if (self.getCharAtPos(col-1,row+1)) == char:
            returnArr.append([col-1, row+1])
        if (self.getCharAtPos(col, row + 1)) == char:
            returnArr.append([col, row + 1])
        if (self.getCharAtPos(col + 1, row + 1)) == char:
            returnArr.append([col + 1, row + 1])
        return returnArr


if __name__ == '__main__':
    fieldArr = [['d', 'd', 't', 'e', 'z', 'e', 'u'],
                      ['i', 'e', 'g', 'n', 'e', 'r', 'b'],
                      ['e', 'h', 'c', 'u', 'n', 'e', 'v'],
                      ['l', 'u', 'r', 'd', 'u', 't', 'i'],
                      ['t', 'e', 'r', 'e', 'w', 't', 't'],
                      ['i', 'k', 'c', 'g', 't', 'w', 'o'],
                      ['m', 'a', 'l', 'ü', 's', 'ü', 'm'],
                     ]
    wordArr = ['mitleid',
                      'motiv',
                      'butter',
                      'wüste',
                      'wunde',
                      'geruch',
                      'zucker',
                      'lüge',
                      'daten']
    wb = wbSolver(fieldArr, wordArr)
    print(wb)
    print(wb.scanWord('motiv', []))






    #print(wb.getCharAtPos(0,1))
    #print(wb.getRow(0))
    #print(wb.getChar(wb.getRow(0),1))
    #print("Scanning for non existent char")
    #print(wb.getScannedCoordsForChar('f'))
    #print("This should be an empty line")
    #print(wb.getRow(-1))
    #print("And this should also be a an empty line")
    #print(wb.getRow(3))
    #print("This is an empty char")
    #print(wb.getCharAtPos(-1, -1))
    #print(wb.getCharAtPos(3,3))
    #print("Adjacent Char not existent")
    #print(wb.getCharAtAdjacentRect(1,1,'f'))
    #print(wb)
    #print(wb.getCharAtAdjacentRect(0,1,'e'))
    #wb.strikeOutChar(1,1)
    #print(wb)