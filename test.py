from main import * # imports main


print('hello world')
test = DataStructure(dataFile)

#print(test.getData())
temp = test.clean(7)
test.setData(temp)

x = test.prepQuantext()
print ('x:')
print (x)
print("Print the Object")
print ( test.toString() )






