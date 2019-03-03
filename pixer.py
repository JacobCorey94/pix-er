import tkinter
import PIL

class pixer:
    def __init__(self, master):
        self.master = master
        self.c_size = (300, 300)
        self.img = None
        self.initgui(self.c_size)

    def initgui(self,s):
        pixer_label = 'Pixer - A Free and Better Image Viewer'
        pixer_font = ('', 30)
        Label(self.master,text = pixer_label, pady = 5, bg = 'white', font = pixer_font).pack()
        
        # s = self.c_size
        self.canvas = Canvas(self.master, height = s[1], width = [0], bd = 10, bg = 'black', relief = 'ridge')
        self.canvas.pack()

        text = "No Image Selected"

        self.wt = self.canvas.create_text(((s[0]/2)-270), (s[1]/2), text = txt, font = pixer_font, fill = 'white')
        f = Frame(self.master, bg = 'white', padx = 10, pady = 10)
        
        # Continue at https://www.youtube.com/watch?v=EqqC88QszOc