from tkinter import Frame, Button, Tk, BOTH
import socket
import sys


#tkinter boilerplate code from pythonprogramming.net


HOST, PORT = '''SERVER_IP''', '''SERVER_PORT'''





sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
def onoff():
    sock.connect((HOST, PORT))
    sock.sendall(bytes('passwordstring onoff' + "\n", "utf-8"))
    print('Done, AC turned on/off')
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        #reference to the master widget, which is the tk window
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window

    def init_window(self):

        # changing the title of our master widget
        self.master.title("AC Control")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        quitButton = Button(self, text="Off/On",command=onoff)

        # placing the button on my window
        quitButton.place(x=10, y=10)



    def client_exit(self):
        exit()

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

#creation of an instance
app = Window(root)

#mainloop
root.mainloop()
