import csv
from tkinter import *

spotify_top50_artists = open('topartists.csv', 'r')
top = []
csv_reader = csv.reader(spotify_top50_artists, )
for i in csv_reader:
    top.append(i)
spotify_top50_artists.close()

root = Tk()
x = Entry(root, width=15)
xlabel = Label(root, text="Enter the End Range of Top Artists: ")
xlabel.grid(row=0, column=0)
x.grid(row=0, column=1)
x.get()


def click():
    labelheading = Label(root,
                         text="Top {} Artists with most songs in top 10000 songs from 1960s on Spotify".format(x.get()))
    labelheading.grid()
    for i in range(int(x.get())):
        myLabel = Label(root, text=top[i][0] + " : " + top[i][1])
        myLabel.grid()


button = Button(root, text="Enter", command=click)
button.grid()
root.mainloop()
