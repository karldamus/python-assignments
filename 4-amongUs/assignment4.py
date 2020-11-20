# Amidst Ourselves: A Game of Deception
# 
# ©2020 Karl Damus, All Rights Reserved
#
# Note: This program does not currently output anything. It is all "return" statements.
# Sample data can be found in '4-amongus/data'.
# The final function returns a list with the liar inside: ['blue'].

PLAYERS = ["red", "blue", "green", "yellow", "brown", "pink", "orange"]

def main():
    loadMap = load_map("data/skeld.txt")
    loadChat = load_chat_log("data/chatlog.txt", loadMap)
    tallyVotes = tally_votes(loadChat)
    getPaths = get_paths(loadChat)
    liars = get_sus_paths(getPaths, loadMap)

def load_map(file_path):
    with open(file_path, "r") as f:
        map_dictionary = {}
        for line in f:
            line = line.strip().split(":")
            line[1] = line[1].strip(" ").split(", ")
            # add to dictionary
            map_dictionary[line[0]] = line[1]
    return map_dictionary

def simplify_testimony(chat, rooms):
    # if the 'chat' is a vote simply use the line. if not, follow else statement
    checkForVote = chat.find("voted")

    if checkForVote >= 0:
        simplifiedChat = chat.strip()
    else:
        chat = chat.split(":")
        speaker = chat[0]
        message = chat[1]

        # check for player in message
        for val in PLAYERS:
            checkSubject = message.find(val)
            if checkSubject >= 0:
                subject = val
                break
            else:
                subject = ""
        # check for location in message
        for key in rooms:
            checkLocation = message.find(key)
            if checkLocation >= 0:
                location = key
                break
            else:
                location = ""

        # accusatory condition
        if location != "" and subject != "":
            simplifiedChat = (speaker + ": " + subject + " in " + location)
        # self condition
        if location != "" and subject == "":
            simplifiedChat = (speaker + ": " + speaker + " in " + location)
        # useless condition
        if location == "":
            pass
    
    try:
        return simplifiedChat
    except NameError:
        pass

def load_chat_log(filename, rooms):
    simplifiedChatLog = []
    with open(filename, "r") as f:
        for line in f:
            chatMessageSimplified = simplify_testimony(line, load_map("data/skeld.txt"))
            # if something was returned then push to array
            if chatMessageSimplified != None:
                simplifiedChatLog.append(chatMessageSimplified)
    return(simplifiedChatLog)

def tally_votes(chat_log):
    tally = {}
    # create a key for each player
    for player in PLAYERS:
        tally[player] = 0
    # add a key for 'skip'
    tally["skip"] = 0
    for val in chat_log:
        isVote = val.find("voted")
        if isVote >= 0:
            val = val.split(" ")
            tally[val[2]] = (int(tally[val[2]]) + 1)
    return tally

def get_paths(chat_log):
    pathDict = {}
    nonAccusatoryStatements = []
    # create keys in dictionary for each player
    for player in PLAYERS:
        pathDict[player] = [] 
    # run through chat_log -- skip if a vote or if accusatory
    for chatVal in chat_log:
        if chatVal.find("voted") >= 0:
            pass
        else:
            chatVal = chatVal.split(":")
            # check if accusatory
            if chatVal[1].find(chatVal[0]) >= 0:
                nonAccusatoryStatements.append(chatVal)
    for val in nonAccusatoryStatements:
        val[1] = val[1].split(" ")
        pathDict[val[0]].append(val[1][3])
    return pathDict

def get_sus_paths(path_dict, rooms):
    sus_players = []
    for player in PLAYERS:
        for location in range(len(path_dict[player])):
            try:
                path_dict[player][location + 1]
                if (path_dict[player][location + 1]) in rooms[path_dict[player][location]]:
                    pass
                else:
                    sus_players.append(player)
            except IndexError:
                pass
    return sus_players

if __name__ == '__main__':
    main()
