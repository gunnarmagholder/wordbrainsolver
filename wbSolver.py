
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
            foundFirstChar = self.getScannedCoordsForChar(word[0])
            if foundFirstChar == []:
                return False
            else:
                for foundCoord in foundFirstChar:
                    thisPath = []
                    thisPath.append(foundCoord)
                    returnArr.append(self.scanWord(word[1:], thisPath))
        else:
            if(len(word)==0):
                return True
            lastCoord = pathArr[len(pathArr)-1]
            foundFirstChar = self.getCharAtAdjacentRect(lastCoord[0],lastCoord[1],word[0])
            if foundFirstChar == []:
                return False
            for foundCoord in foundFirstChar:
                thisPath = []
                thisPath.append(foundCoord)
                return thisPath.append(self.scanWord(word[1:], thisPath))
        return returnArr

    def getFoundWord(self,word):
        returnArr = []
        coordArr = wb.scanWord('lüge', [])
        for wordSequence in coordArr:
            if (wordSequence):
                result = wordSequence[len(wordSequence)-1]
                if (result == True):
                    returnArr.append(wordSequence[0:len(wordSequence)-2])
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

    def flatten(self,lists):
        if lists == []:
            return lists
        if isinstance(lists[0],list):
            return self.flatten(lists[0]) + self.flatten(lists[1:])
        return lists[:1] + self.flatten(lists[1:])

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
    # print(wb.scanWord('lüge', []))
    print(wb.getFoundWord('lüge'))