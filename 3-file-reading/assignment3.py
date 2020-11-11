rooms = ['bathroom', 'gameroom', 'kitchen', 'breakroom', 'closet']
roomMotion = []
highEMF = []
lowTemp = []

def main():
    read_motion("ravensnest")
    read_emf("ravensnest")
    read_temp("ravensnest")
    generate_report("ravensnest", roomMotion, highEMF, lowTemp)

def read_motion(location_name):
    # set filename and open file
    
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
                        if room in roomMotion:
                            continue
                        else:
                            roomMotion.append(room)

def read_emf(location_name):
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

def is_valid_temp(val):
    absoluteVal = val.strip("-") 
    splitVal = absoluteVal.split(".")
    
    if(splitVal[0].isdigit()):
        return True
    else:
        return False

def read_temp(location_name):
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

def generate_report(location, motion, emf, temp):
    ghostReport = []
    filename = "data/ghost_report." + location + ".txt"
    with open(filename, "w") as f:
        for m in motion:
            whatGhost(m)
            if(whatGhost(m) != ""):
                if((whatGhost(m) + " in " + m) not in ghostReport):
                    ghostReport.append(whatGhost(m) + " in " + m)
        for e in emf:
            whatGhost(e)
            if(whatGhost(e) != ""):
                if((whatGhost(e) + " in " + e) not in ghostReport):
                    ghostReport.append(whatGhost(e) + " in " + e)                
        for t in temp:
            whatGhost(t)
            if(whatGhost(t) != ""):
                if((whatGhost(t) + " in " + t) not in ghostReport):
                    ghostReport.append(whatGhost(t) + " in " + t)                

        # create ghost report
        f.write("== Raven Ghost Hunting Society Haunting Report ==")
        f.write("\nLocation: " + location)
        for x in ghostReport:
            f.write("\n" + x)

def whatGhost(item):
    if(item in roomMotion) and (item in highEMF) and (item in lowTemp):
        ghost = "Poltergeist"
    elif(item in roomMotion) and (item in highEMF) and (item not in lowTemp):
        ghost = "Oni"
    elif(item in roomMotion) and (item not in highEMF) and (item in lowTemp):
        ghost = "Banshee"
    elif(item not in roomMotion) and (item in highEMF) and (item in lowTemp):
        ghost = "Phantom"
    else:
        ghost = ""
    return ghost

if __name__ == "__main__": 
    main()