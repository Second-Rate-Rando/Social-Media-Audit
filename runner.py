import matplotlib.pyplot as np
import matplotlib.pyplot as plt
from main import *
import numpy as np
from scipy.interpolate import interp1d

def calAVG(nums): #calculates the average of all the numbers in a list
    avg = 0
    for i in nums :
        avg += i

    avg = avg / len(nums)
    return avg



def averageBarChart(data) : #takes a clean data set and makes a bar chart of the AVG number of likes based on category
    #N = 3
    #ind = np.arange(N)

    #barFigure = plt.figure()
    #ax = barFigure.add_axes([0,0,1,1])
    likes = [0,0,0] #index 0 is Generic, 1 is Announcement, 2 is Attack
    retweets = [0,0,0]
    catCount = [0,0,0]
    counter = 0
    for i in data:
        cat = data[counter][4].strip() #remove spaces on either side
        if cat == 'Generic':
            catCount[0] += 1
            likes[0] += int( data[counter][3] )
            retweets[0] += int(data[counter][2])
        elif cat == 'Announcement':
            catCount[1] += 1
            likes[1] += int( data[counter][3] )
            retweets[1] += int(data[counter][2])
        elif cat == 'Attack':
            catCount[2] += 1
            likes[2] += int( data[counter][3] )
            retweets[2] += int(data[counter][2])
        counter += 1
    counter = 0
    avgs = [0,0,0,0]
    print(catCount)
    print(likes)

    for x in likes:
       avgs[counter] =( likes[counter] + ( retweets[counter] * 1.25 )) / catCount[counter]
       #avgs[counter] = likes[counter] / catCount[counter]
       counter = counter + 1


    avgs[3] = sum(avgs) / 3
    print (avgs)
    lables = ["Generic", "Announcement", "Attack", "Total AVG"]


    #ax.set_xticks(ind, labels=[ 'Generic', 'Announcement', 'Attack'])
    # ax.set_ylabel('Average')
    plt.bar(lables,avgs, color = 'red')
    #plt.xticks(lables,avgs)
    plt.show()

def mostCommonWords(data): #makes graph of the most common words and their frequencies, format will be [word,4] as in the word 'word' was found 4 times
    wordList = []
    frequencyList = []
    counter = 0
    for i in data :
        if (counter != 0):
            wordList.append(data[counter][0])
        counter += 1
    #print("wordList:")
    #print(wordList)
    counter = 0

    for j in wordList :
        wordList[counter] = wordList[counter].split(" ")
        counter += 1
    print (wordList)
    counter = 0
    counter2 = 0
    tempList = []
    for x in wordList :
        counter2 = 0
        for y in wordList[counter] :
            tempList.append(wordList[counter][counter2])
            counter2 += 1
        counter += 1
    wordList = tempList
    print (wordList)

    wordList = removeChar(wordList)
    print(wordList)
    frequencyList = []
    counter = 0
#    counter2 = 0
    #for i in wordList :
    for q in wordList:
        frequencyList.append([wordList.count(q),q])
        for r in wordList :
            if (q == r):
                wordList.remove(r)

    #plt.bar(words, frequency, color='red')
    #plt.show()
    return frequencyList

def graphMostCommonWords(frequencyList,commonWords) :
    commonWords = commonWords.read()
    commonWords = commonWords.split('\n')
    counter = 0
    #for t in commonWords:
    #    commonWords[counter] = commonWords[counter].lower()
    #print(commonWords)
    frequency = []
    words = []
    counter = 0
    for i in frequencyList:
        frequency.append(frequencyList[counter][0])
        words.append(frequencyList[counter][1])
        counter += 1
    print('words')
    print(words)
    print('frequency')
    print(frequency)
    print("commonWords")
    print(commonWords)
    #for i in words :
    counter = 0
    #numRemoved = 0
    newWords = []
    newFrequency = []
    for j in words :
        if (j not in commonWords and frequency[counter] >= 5 and j != '') :
                newWords.append(words[counter])
                newFrequency.append(frequency[counter])
        #print(words[counter - numRemoved])
        counter += 1
        #print (len(words))
        #print(len(frequency))
    print('filtered words')
    print (newWords)

    plt.bar(newWords,newFrequency, color = 'red')
    #plt.set_figheight(20)
    #plt.set_figwidth(20)
    plt.show()
    return newWords

def removeChar(wordList):
    counter = 0
    for l in wordList:
        # if counter == 0 :
        special_characters = ['!', '#', '$', '%', '&', '@', '[', ']', ' ', ']', '_']
        word = wordList[counter]
        for i in special_characters:
            word = word.replace(i, '')
            word = word.lower()
            wordList[counter] = word
        counter = counter + 1
    print("wordList")
    print(wordList)
    return wordList

def highFrequencyEngagement(newWords, data):
    counter = 0
    wordWithEngagment = []
    for i in data:
        #cat = data[counter][4].strip()
        temp = data[counter][0].lower()
        for j in newWords:
            #likes = 0
            #retweets = 0
            # print (j)
            # print(data[0][counter])
            if (j in temp):
                #likes = likes + int ( data[counter][3] )
                #retweets = retweets + int (data[counter][2])
                wordWithEngagment.append( [ j, int ( data[counter][3] ), int ( data[counter][2]) ] )


        counter = counter + 1

    #print('wordWithEngagment')
    #print(wordWithEngagment)
    combined = []
    totals = []
    counter2 = 0
    #ping = 0
    #print ('hi')
    for i in newWords :
        counter = 0
        ping = 0
        for j in wordWithEngagment :
            if( i == wordWithEngagment[counter][0] and ping == 0):
                combined.append(j)
                totals.append(1)
                ping = ping + 1
            elif i == wordWithEngagment[counter][0]:
                if ( combined[counter2][0] == wordWithEngagment[counter][0]) :
                    combined[counter2][1] = combined[counter2][1] + wordWithEngagment[counter][1]
                    combined[counter2][2] = combined[counter2][2] + wordWithEngagment[counter][2]
                    totals[counter2] = totals[counter2] + 1
            counter = counter + 1
        counter2 = counter2 + 1

    #print('combined')
    #print(totals)
    #print(combined)
    avgs = []
    lables = []
    counter = 0
    #print(len(totals))
    #print( len( wordWithEngagment) )
    for x in combined:
        #f = totals[counter]
        avgs.append(  (combined[counter][1] + (combined[counter][2] * 1.25) ) / totals[counter]  )
        lables.append( combined[counter][0])
       #avgs[counter] = likes[counter] / catCount[counter]
        counter = counter + 1
    counter = 0

    lables.append("Total AVG")
    avgs.append(82)

    print(lables)
    print(avgs)
    plt.bar(lables, avgs, color='red')
    plt.show()

def wordAndCatagory(newWords,data):
    #print (newWords)
    counter = 0
    wordWithCat = []

    for i in data :
        cat = data[counter][4].strip()
        temp = data[counter][0].lower()
        for j in newWords:
           # print (j)
            #print(data[0][counter])
            if (j in temp) :
                wordWithCat.append([j,cat,1])
        counter = counter + 1
    catagories =  ["Generic", "Announcement", "Attack"]
    print ("word with catagory : ")
    print (wordWithCat)
    counter = 0
    counter2 = 0
    ping = 0
    combined = []
    for i in newWords :
        counter = 0
        ping = 0
        for j in wordWithCat :
            if( i == wordWithCat[counter][0] and ping == 0):
                combined.append(j)
                ping = ping + 1
            elif i == wordWithCat[counter][0]:
                if ( combined[counter2][1] == wordWithCat[counter][1]) :
                    combined[counter2][2] =  ( combined[counter2][2] ) + 1
                else :
                    combined.append(j)

            # (counter == len(wordWithCat) ) :
            #   combined.append(j)
            counter = counter + 1
        counter2 = counter2 + 1

    print(combined)
    xlabel = []
    ylabel = []
    counter = 0

    for i in combined :
        xlabel.append(combined[counter][0][0:5]  + ":" + combined[counter][1][0:3])
        ylabel.append(combined[counter][2])
        counter = counter + 1
    print(xlabel)
    print(ylabel)
    plt.bar(xlabel, ylabel, color='red')
    plt.show()

def postSedg(data):
    numberOfPosts = []
    date = []
    counter = 0
    counter2 = -1
    gaming = 0
    for i in data :

        if data[counter][1] in date :
             numberOfPosts[counter2] = numberOfPosts[counter2] + 1
        elif( counter != 0 and counter + 1 < len(data)) :
            date.append(data[counter][1])
            numberOfPosts.append(1)
            counter2 = counter2 + 1
            #gaming = gaming + 1

            #gaming = gaming + 1
            x = int ( data[counter][1][3:] )

            y = int ( data[ ( counter + 1 ) ][1][3:] )
            print("#############################")
            print("x and y :")
            print(x)
            print(y)
            #if x == y :
            #    numberOfPosts[counter2] = numberOfPosts[counter2] + 1
            #if (x != y and x + 1 != y  ) :
            #        print ('Yo mr white I added the thing!')
            #        temp = 1
            #        #date.append("PWP")
            #        #numberOfPosts.append(0)
                    #counter2 = counter2 + 1

            #        if x < y and y == 1 :
            #            y = 31
            #        while x != y and x + 1 != y and x < y :
            #            #gaming = gaming + 1
            #            print(x)
            #            print(y)
            #            temp = temp + 1
            #            x = x + 1

            #        gaming = gaming + 1
            #        date.append("NPP:"+  str(temp) + " Strikes:" + str(gaming) )
            #        numberOfPosts.append(0)
            #        counter2 = counter2 + 1
        counter = counter + 1
            #    x =int (  (data[counter][1][3:]) )
            #    y =int( (data[counter - 1][1][3:]) )
            #    temp = 1
            #    while (y != x - 1):
            #        print(x)
            #        print(y)
            #        date.append("DWP : " + str(temp))
            #        numberOfPosts.append(0)
            #        y = y + 1
            #        temp = temp + 1
            #       counter2 == counter2 + 1



    print("#################################################")
    print("Date Graph Data : ")
    print(numberOfPosts)
    print(date)
    print(sum(numberOfPosts))
    print(len(numberOfPosts))
    print(len(date))
    #cubic_interploation_model = interp1d(x, y, kind="cubic")

    print(date)
    plt.plot ( date ,numberOfPosts)
    plt.title('Post Frequency')
    plt.show()






test = DataStructure(dataFile)

#print(test.getData())
temp = test.clean(7)
test.setData(temp)
#print('hello')
averageBarChart(temp)
#print (mostCommonWords(temp))

newWords = graphMostCommonWords(mostCommonWords(temp),commonWords)

wordAndCatagory(newWords,temp)
highFrequencyEngagement(newWords,temp)

postSedg(temp)