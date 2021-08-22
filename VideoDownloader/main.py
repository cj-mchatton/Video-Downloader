from pytube import YouTube
from tkinter import *

# tkinter object/window
root = Tk()
root.title('YouTube Video Downloader')

# make window not resizable
root.resizable(False, False)

# width and height variables
w = 750
h = 500

# get the resolution (w and h) of the user's screen
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# use data to find the "middle" coordinates
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# use the data to place the window in the middle of the user's screen
root.geometry("%dx%d+%d+%d" % (w, h, x, y-100))

# tkinter object


class VideoDownloader:

    # init function for window attributes and objects
    def __init__(self, master):

        # make the background a light grey color
        master.configure(background='#999999')

        # initiate the frame for placement/organization of other objects
        my_frame = Frame(master)
        my_frame.place(relx=1, rely=1)

        # labels to label the directory and link text entries
        self.titleLabel = Label(
            master,
            bg="#999999", fg="white",
            text="Cameron's YouTube Downloader", font="Times 24 italic bold",
        )
        self.titleLabel.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.nameLabel = Label(
            master,
            bg="#999999", fg="white",
            text="File Name:", font="Times 18 italic",
        )
        self.nameLabel.place(relx=0.195, rely=0.35, anchor=CENTER)

        self.dirLabel = Label(
            master,
            bg="#999999", fg="white",
            text="Directory:", font="Times 18 italic",
        )
        self.dirLabel.place(relx=0.198, rely=0.45, anchor=CENTER)

        self.linkLabel = Label(
            master,
            bg="#999999", fg="white",
            text="Link:", font="Times 18 italic",
        )
        self.linkLabel.place(relx=0.233, rely=0.55, anchor=CENTER)

        # text entries for directory and link
        self.nameTextBox = Entry(master)
        self.nameTextBox.insert(0, "New Song")
        self.nameTextBox.place(width=350, height=20, relx=0.5, rely=0.35, anchor=CENTER)

        self.dirTextBox = Entry(master)
        self.dirTextBox.insert(0, r"C:\Users\Cameron McHatton\Downloads")
        self.dirTextBox.place(width=350, height=20, relx=0.5, rely=0.45, anchor=CENTER)

        self.linkTextBox = Entry(master)
        self.linkTextBox.place(width=350, height=20, relx=0.5, rely=0.55, anchor=CENTER)

        # radio buttons to select mp4 or mp3 file type
        self.v = IntVar()
        self.v.set(0)
        self.mp3Button = Radiobutton(master, text=".mp3", bg="#999999", variable=self.v, value=0)
        self.mp3Button.place(relx=0.404, rely=0.625)

        self.mp4Button = Radiobutton(master, text=".mp4", bg="#999999", variable=self.v, value=1)
        self.mp4Button.place(relx=0.52, rely=0.625)

        # download button that points to a downloading function
        self.myButton = Button(master, width=10, height=1, text="Download", command=self.click)
        self.myButton.place(relx=0.5, rely=0.71, anchor=CENTER)

    # click function that starts the download process if the input presented is correct
    def click(self):
        fn = self.nameTextBox.get()
        direct = self.dirTextBox.get()
        print(len(direct))
        link = self.linkTextBox.get()

        try:
            filetype = None
            if self.v.get() == 0:
                filetype = '.mp3'
            elif self.v.get() == 1:
                filetype = '.mp4'

            yt = YouTube(link)
            yt.streams.get_highest_resolution().download(output_path=direct, filename=(fn+'{}'.format(filetype)))
        except:
            print("Couldn't download file...")


# pass the root so the class works as a window

vd = VideoDownloader(root)
# make tkinter run until the user exits
root.mainloop()
