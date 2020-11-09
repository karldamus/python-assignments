rooms = ['bathroom', 'gameroom', 'kitchen', 'breakroom', 'closet']

def main():
    # read_motion("ravensnest")
    read_emf("ravensnest")


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
        for line in f:
            line = line.strip()
            # current line is a number add to current 'sum tally'
            if line.isnumeric():
                try:
                    roomSum = roomSum + int(line)
                    print("Tried 'roomSum' variable")
                    counter += 1
                except NameError:
                    roomSum = int(line)
                    print("set 'roomSum variable")
                    counter += 1
            # current line is not a number, reset the loop parameters
            else:
                print("This line is not a number.")
                currentRoom = line
                try:
                    roomSum
                    if(roomSum >= 0):
                        roomAverage = (roomSum / counter)
                        print("Tried to average")
                except NameError:
                    roomSum = 0
                
                # reset counter for next room
                counter = 0
    print("Sum: " + str(roomSum))
    print("Ave: " + str(roomAverage))
    # try: 
    #     print("Ave: " + str(roomAverage))
    # except NameError:
    #     print("")
            
            

if __name__ == "__main__": 
    main()