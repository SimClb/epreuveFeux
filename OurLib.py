#let's recreate basics functions ;)
import colors 

def lenCounter(myVar):
    count = 0
    for i in myVar:
        count += 1
    return count


def isNumericHomeMade(myVar):
    try:
        int(myVar)
        isNumeric = True
        return isNumeric
    except ValueError:
        isNumeric = False
        return isNumeric

def exponent(number, exponent):
    result = 1
    for i in range(exponent):
        result *= number
    print(f'the result is: {result}')

def maxHomeMade(myList): 
    #counter of elements of list 
    numberOfElement = 0
    for x in myList:
        numberOfElement += 1   
    
    score = 0
    # take one number and compare to the other
    for i in myList:
        for m in myList[1:]:
            if i > m:            
                score += 1
            else:
                continue

            if score == (numberOfElement - 1):
                print(i)

def minHomeMade(myList):
    #counter of elements of list 
    numberOfElement = 0
    for x in myList:
        numberOfElement += 1   
    
    score = 0
    # take one number and compare to the other
    for i in myList:
        for m in myList[1:]:
            if i < m:            
                score += 1
            else:
                continue

            if score == (numberOfElement - 1):
                print(i)


def double(myList):
    memory = 0
    for i in myList:
        for m in myList:
            if i == m:
                memory = m

    myList.remove(memory)
    print(myList, memory)



def reverseStr(var):

    N = lenCounter(var)
    chars = ''

    for i in range(N -1, -1, -1):
        chars += str(var[i])

    return chars

def duplicatorScanner(var):

    counterI = 0
    counterJ = 0

    for i in var:
        #print(colors.bcolors.OKBLUE, counterI, "qui est l'index de:", i, colors.bcolors.ENDC)

        for j in var:
            #print(colors.bcolors.OKGREEN, counterJ, "qui est l'index de:", j,  colors.bcolors.ENDC)
            if i == j and counterI != counterJ:
                #print(f'{i} ayant pour index {counterI} est égal à {j} ayant pour index {counterJ}')
                return True
                

            counterJ += 1

        counterI += 1
        counterJ = 0
            
def isSorter(list):

    members = (lenCounter(list) - 1) 
    counter = 0

    for (i, j) in zip(list, list[1:]):

        if i < j:
            counter += 1

    if counter == members:
        return True
    else:
        return False

def isSorterASCII(list):

    members = (lenCounter(list) - 1) 
    counter = 0

    for (i, j) in zip(list, list[1:]):

        if ord(i[0]) < ord(j[0]):
            counter += 1
        elif ord(i[0]) == ord(j[0]):
            if ord(i[1]) < ord(j[1]):
                counter += 1
                
    if counter == members:
        return True
    else:
        return False

def finMin(varList):
    m = int(varList[0])

    for i in varList[1:]:

        if i < m:
            m = int(i)

    return m 

def bubbleSort(myList):

    notDouble = []

    for i in myList:
        if i not in notDouble:
            notDouble.append(i) # like that we are working in a simple list !

    while not isSorter(notDouble):

        for (i, j) in zip(notDouble, notDouble[1:]):
            if i > j: 
                notDouble.remove(i)
                notDouble.insert((notDouble.index(j) + 1), i)
            elif i < j:
                continue
                
    for i in notDouble:
        print(i, end=' ')


# faire un check len avec un paramètre de manière à ce que la fonction 
# d'error management soit modulaire


