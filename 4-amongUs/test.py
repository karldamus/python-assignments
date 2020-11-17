# Amidst Ourselves: A Game of Deception | test.py
# 
# ©2020 Karl Damus, All Rights Reserved
#

PLAYERS = ['blue', 'brown', 'green', 'orange', 'pink', 'red', 'yellow']
testDict = {'upper engine': ['cafeteria', 'reactor', 'security', 'lower engine', 'medbay'], 'reactor': ['security', 'upper engine', 'lower engine'], 'security': ['upper engine', 'lower engine', 'reactor'], 'lower engine': ['electrical', 'storage', 'upper engine', 'reactor', 'security'], 'medbay': ['upper engine', 'cafeteria'], 'cafeteria': ['storage', 'admin', 'weapons', 'upper engine', 'medbay'], 'weapons': ['o2', 'navigation', 'cafeteria', 'shields'], 'o2': ['weapons', 'navigation', 'shields'], 'navigation': ['weapons', 'o2', 'shields'], 'shields': ['communications', 'storage', 'weapons', 'o2', 'navigation'], 'communications': ['storage', 'shields'], 'storage': ['admin', 'cafeteria', 'lower engine', 'electrical', 'shields', 'communications'], 'electrical': ['storage', 'lower engine'], 'admin': ['cafeteria', 'storage'],}

def main():
    # testLoad()
    testSimplify()

def testSimplify():
    chat = "green: Then I went to storage."
    # if the line is a vote simply use the line. if not, follow else statement
    checkForVote = chat.find("voted")
    if checkForVote >= 0:
        print(chat)
    else:
        chat = chat.split(":")
        
        speaker = chat[0]
        message = chat[1]

        for val in PLAYERS:
            checkSubject = message.find(val)
            if checkSubject >= 0:
                subject = val
                break
            else:
                subject = ""
        for key in testDict:
            checkLocation = message.find(key)
            if checkLocation >= 0:
                location = key
                break
            else:
                location = ""

        if location != "" and subject != "":
            simplifiedChat = (speaker + ": " + subject + " in " + location)
        if location != "" and subject == "":
            simplifiedChat = (speaker + ": " + speaker + " in " + location)
        if location == "":
            simplifiedChat = "No info was obtained"
        print(simplifiedChat)
        
        
            
# for key in testDict:
#         print(key)


"""
def testLoad():
    testList = ["room1: room2, room3", "room2: room1, room3"]
    testDict = {}

    for line in testList:
        line = line.split(":")
        line[1] = line[1].strip(" ")
        line[1] = line[1].split(",")
        
        testDict[line[0]] = line[1]
    print(testDict)

    with open("data/skeld.txt", "r") as f:
        map_dictionary = {}
        for line in f:
            line = line.strip().split(":")
            line[1] = line[1].strip(" ").split(",")
            print(line)
            # add to dictionary
            map_dictionary[line[0]] = line[1]
        print(map_dictionary)

    for line in testList:
        line = line.strip().split(":")
        line[1] = line[1].strip(" ").split(", ")
        testDict[line[0]] = line[1]
    print(testDict)
"""

main()
