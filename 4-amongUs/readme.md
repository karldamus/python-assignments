# Among Us in Python
- - - -
### Introduction
There’s a popular new game in COMP1405 - Amidst Ourselves (definitely no relation to the real world game, Among Us…). In Amidst Ourselves, there are seven astronauts aboard a spaceship. Each astronaut is represented by a colour. They run around, performing daily jobs on the spaceship. One of those colours is not who they seem. One of them… is an alien. 

The crewmates want to get their tasks done. The alien wants them gone. Every once in a while, the players meet up and chat with each other to try and find the alien. They usually do this by talking about what they did since the last meeting. Then they vote for somebody to eject out of the airlock - hopefully saving the crew from destruction! 

However; the alien will lie. 

The main problem in finding the alien is that all of this chat can be really hard to follow. That’s where we come in. We’re going to be building a program that builds some representation of the in-game map and reads text logs from a round of the game. Using the map and our chat logs, we’ll find out just who is sus(picious) and lying about where they were…

### Program Overview
This assignment slowly evolves the functionality of our program, one step at a time. 
1. Read in game map data and store it in a useful way - as a dictionary 
2. Write a helpful function that takes in a chat message and returns only the useful parts 
3. Write a function which uses the previous helper function to reduce a full file worth of chat 
4. Write a function which goes through that simplified chat log and outputs the player’s votes for the round
5. Write a function which goes through that simplified chat log to check if the paths people claim to have taken are actually valid, based on the map information 
