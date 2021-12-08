from tkinter import *
from datapull import *

root = Tk()
# List for calling user inputs and loops
playerList = ["playerOne", "playerTwo", "playerThree", "playerFour", "playerFive"]

# creates the user input for player search
for count, players in enumerate(playerList):
    print(count)
    globals()[players] = Entry(root, bg="#ADD8E6")
    globals()[players].grid(row=0, column=count, padx=10, pady=10)
    globals()[players].insert(0, "Enter Player's Name: ")

# print(playerOne.type())

# Algorithm for searching players and outputting data
def playerDataSearch():
    for count, playerNames in enumerate(playerList):
        ign = globals()[playerNames].get()
        locals()[ign] = player_ids(ign)
        print(ign[1])



# creates the button for searching player data
searchButton = Button(root, text="Search Players", command=playerDataSearch).grid(row=2, column=6, padx=10, pady=10)

# canvas = Canvas(root, bg="#D13639")
# canvas.pack()

frame = Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# root.attributes('-fullscreen',True)

#



root.mainloop()
