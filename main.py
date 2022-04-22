
#SM and Polo Final
#This

dataFile = open('The Twitter data.csv', encoding="utf8")
commonWords = open('commonWords', 'r+')
#print(dataFile.read()) # tester
#print(commonWords.read()) # tester

class DataStructure :

    def __init__(self,data): #constructor
        self.data = data.read() # data should be a text file

    def getData(self): #getters / setters
        return self.data

    def setData(self,data):
        self.data = data
        self.data = data

    def toString(self): #formats CLEAN DATA!!! CLEAN DATA ONLY!!!!!
        dataList = self.data
        str = ''
        counter = 0
        #while counter != len(dataList):
        #   counter2 = 0
        #   str += '\n'
        #   for j in dataList[counter] :
        #        str += dataList[counter][counter2]
        #        counter2 = counter2 + 1
        #        counter = counter + 1
        return dataList

    def prepQuantext(self): # DATA must be clean
        tempList = []
        counter = 0
        for i in self.data :
            x = self.data[counter][0]
            x = x.split(" ")
            tempList.append(x)
            counter = counter + 1

        return tempList

    def frequanText(self, preppedText):
        counter = 0
        wordList = []# will contain a list of lists, first word than the frequency of the word IE the value [then,5] means 5 'then' were found
        tempList = []
        for i in preppedText :
            counter = counter + 1
            for j in preppedText[counter] :
                tempList.append(preppedText[counter])
        index = 0
        for x in tempList:
            index = index + 1
            counter = 0
            for y in tempList :
                if x == y :
                    counter = counter + 1
                    wordList.append([tempList[index],counter])
        return wordList


    def clean(self,numOfRows): #cleans the data so that it can be analyzed,
        tempData = self.data  # should be used with setData() as it does not change the data variable automaticly or manipulate the text file itself.
        tempData = tempData.replace('\n',',')
        print(tempData)
        tempData = tempData.split(",")
        #tempData = tempData.remove(None)
        cleanData = []

        print("temp data : ")
        print(tempData)
        counter = 0
        cols = 0
        while counter < len(tempData) -1 :
            tempList = []
            #print(len(tempData) -1)
            #print (counter)
            rowCounter = 0
            while ( numOfRows != rowCounter ):

                #print("THIS IS THE DEBUG STEP")
                #print(tempData[counter])

                #forDebug = tempData[counter]

                tempList.append(tempData[counter])
                counter = counter + 1
                rowCounter = rowCounter + 1

            cleanData.append([])
            cleanData[cols] = tempList
            cols = cols + 1

        #print("clean Data:")
        #print (cleanData)
        return cleanData





