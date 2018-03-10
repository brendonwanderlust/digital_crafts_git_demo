#Functions Exercises
# 1
       '''Before''' ''' 
string = "My name is Brendon"
reverseList = []
newString = ''
for x in range(len(string)-1, -1, -1):
    reverseList.append(string[x])
for index in range(len(reverseList)):
    newString = newString + reverseList[index]
print newString'''

        #After
def reverseString(str):
    reverseList = []
    newString = ''
    for x in range(len(string)-1, -1, -1):
        reverseList.append(str[x])
    for index in range(len(reverseList)):
        newString = newString + reverseList[index]
    print newString

reverseString("Hello, how are you?")

# 2
        '''Before''' '''
#Postive Numbers
x = [8744, -5324, -3246, 2543, 3454, 3421, -3256, 1321, 3225 , -8937, 7323, -3232]
for index in x:
    if index > 0:
        print index
'''
        #AFTER
def onlyPositiveNums(x):
    for index in x:
        if index > 0:
            print index
