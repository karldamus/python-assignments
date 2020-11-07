# with open("test.txt", "w") as infile:
#     infile.write("Test!\n")

def main():
    read_motion("ravensnest")

def read_motion(location_name):
    bathroom = 0
    gameroom = 0
    kitchen = 0
    breakroom = 0
    closet = 0
    roomslist = []
    filename = "data/" + location_name + ".motion.txt"
    with open(filename, "r") as f:
        
        for line in f:
            line = line.strip()
            currentLine = line.split(",")

            if(currentLine[0] == "bathroom"):
                if "detected" in currentLine:
                    if bathroom == 0:
                        bathroom = 1
                        roomslist.append("bathroom")
            if(currentLine[0] == "gameroom"):
                if "detected" in currentLine:
                    if gameroom == 0:
                        gameroom = 1
                        roomslist.append("gameroom")
            if(currentLine[0] == "kitchen"):
                if "detected" in currentLine:
                    if kitchen == 0:
                        kitchen = 1
                        roomslist.append("kitchen")
            if(currentLine[0] == "breakroom"):
                if "detected" in currentLine:
                    if breakroom == 0:
                        breakroom = 1
                        roomslist.append("breakroom")
            if(currentLine[0] == "closet"):
                if "detected" in currentLine:
                    if closet == 0:
                        closet = 1
                        roomslist.append("closet")

    print(roomslist)

if __name__ == "__main__": 
    main()