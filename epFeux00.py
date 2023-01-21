import OurLib
import colors
import sys
# echauffement 

# function 

def rectangle(width, floor):

    topBot = []
    floors = []
    finishRectangle = []

    # let's generate our top and bottom 

    for i in range(2):
        adTB = 'o'
        for x in range(width -2):
            adTB += '-'
        adTB += 'o'
        topBot.append(adTB)


    # let's generate our floors 

    for i in range(floor - 2):
        adFloor = '|'
        for i in range(width-2):
            adFloor += ' '
        adFloor += '|'
        floors.append(adFloor)

    finishRectangle.append(topBot[0])
    for i in floors:
        finishRectangle.append(i)
    finishRectangle.append(topBot[1])

    return finishRectangle

# error management 

if OurLib.lenCounter(sys.argv) != 3:
    print('error.')
    exit()

for i in sys.argv[1:]:
    if not OurLib.isNumericHomeMade(i):
        print('error.')
        exit()

# exe 


for i in rectangle(int(sys.argv[1]), int(sys.argv[2])):
    print(i)