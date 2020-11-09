rooms = ['bathroom', 'gameroom', 'kitchen', 'breakroom', 'closet']

def main():
    read_motion("ravensnest")
    # read_emf("ravensnest")


def read_motion(location_name):
    # set up list for rooms with "motion detected", set filename and open file
    roomslist = []
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
                        if room in roomslist:
                            continue
                        else:
                            roomslist.append(room)
    print(roomslist)

def read_emf(location_name):
    filename = "data/" + location_name + ".emf.txt"
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if(isinstance(line, str)):
                print(line)

if __name__ == "__main__": 
    main()