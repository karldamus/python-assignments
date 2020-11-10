rooms = ['bathroom', 'gameroom', 'kitchen', 'breakroom', 'closet']

def main():
    # read_motion("ravensnest")
    # read_emf("ravensnest")
    read_temp("ravensnest")


def read_motion(location_name):
    # set up list for rooms with "motion detected", set filename and open file
    roomMotion = []
    filename = "data/" + location_name + ".motion.txt"
    with open(filename, "r") as f:
        # loop through each line in motion file 
        # (strip away unecesarry spaces and create a list for current line)
        for line in f:
            line = line.strip()
            currentLine = line.split(",")
            # go through list of rooms
            for room in rooms:
                if(currentLine[0] == str(room)):
                    if "detected" in currentLine:
                        # print(room)
                        if room in roomMotion:
                            continue
                        else:
                            roomMotion.append(room)
    print(roomMotion)

def read_emf(location_name):
    highEMF = []
    filename = "data/" + location_name + ".emf.txt"

    with open(filename, "r") as f:
        counter = 0
        roomSum = 0
        for line in f:

            line = line.strip()
            # current line is a number, so add to existing 'sum tally' if it exists
            if line.isnumeric():
                roomSum = roomSum + int(line)
                counter += 1
            # current line is not a number, reset the loop parameters
            else:
                try:
                    roomSum
                    # check if room sum is > zero; calculate ave and append current room to highEMF if ave > 3
                    if(roomSum > 0):
                        roomAverage = (roomSum / counter)
                        if roomAverage > 3:
                            highEMF.append(str(currentRoom))
                except NameError:
                    roomSum = 0

                # reset counter, roomSum, roomAverage, and currentRoom variables for the next room
                currentRoom = line
                roomSum = 0
                counter = 0
                roomAverage = 0
        
        # end of file does not have another string of 'text' at the end so this accounts for the last room in the house
        else:
            if(roomSum > 0):
                roomAverage = (roomSum / counter)
                if roomAverage > 3:
                    highEMF.append(str(currentRoom))

    print(highEMF)

def read_temp(location_name):
    lowTemp = []
    filename = "data/" + location_name + ".temp.txt"

    with open(filename, "r") as f:
        consecutiveCounter = 0
        coldRoom = 0
        currentRoom = ""
        for line in f:
            line = line.strip()
            if (is_valid_temp(line) == True):
                if(consecutiveCounter >= 5):
                    if currentRoom in lowTemp:
                        continue
                    else:
                        lowTemp.append(currentRoom)
                        consecutiveCounter = 0
                elif(float(line) < 0):
                    consecutiveCounter += 1
                elif(float(line) >= 0):
                    consecutiveCounter = 0
                 
            else:
                currentRoom = str(line)
                consecutiveCounter = 0
    print(lowTemp)

def is_valid_temp(val):
    absoluteVal = val.strip("-") 
    splitVal = absoluteVal.split(".")
    
    if(splitVal[0].isdigit()):
        return True
    else:
        return False


if __name__ == "__main__": 
    main()