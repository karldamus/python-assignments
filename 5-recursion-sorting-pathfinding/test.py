def main():
    newList = testListReturn()
    print(newList)

def testListReturn():
    testList = [(1,8),(2,3)]
    return testList

def cocktailSort(unsortedList): 
    sortedList = []
    length = len(unsortedList) 
    swapped = True
    start = 0
    end = length-1
    
    while swapped == True: 
        swapped = False

        for i in range(start, end): 
            if unsortedList[i] > unsortedList[i+1] : 
                unsortedList[i], unsortedList[i+1]= unsortedList[i+1], unsortedList[i] 
                swapped=True

        if swapped==False: 
            break

        swapped = False
        end = end-1

        for i in range(end-1, start-1,-1): 
            if unsortedList[i] > unsortedList[i+1]: 
                unsortedList[i], unsortedList[i+1] = unsortedList[i+1], unsortedList[i] 
                swapped = True
        start = start+1
    
    sortedList = unsortedList

    return sortedList

def calculate():
    unsortedList = [5,1,4,2,8,0] 
    print(cocktailSort(unsortedList))

if __name__ == '__main__':
    main()
