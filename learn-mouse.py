# -*- coding: utf-8 -*-
import Tkinter as tk
import random
from PIL import Image, ImageTk
from subprocess import call, PIPE
import os, os.path

IMAGES_DIR = os.path.join(os.path.dirname(__file__), "images")

MODE_MOTION_NAME = u"Тренировать движение" # train motion in Russian 
MODE_CLICK_NAME = u"Тренировать клики" # train clicks in Russian

SOUND_PLAYER = "gst-play-1.0"
SOUNDS = ["/usr/share/sounds/freedesktop/stereo/bell.oga",
          "/usr/share/sounds/ubuntu/stereo/bell.ogg",
          "/usr/share/sounds/ubuntu/stereo/message.ogg",
]


class App():
    bg_color = "#ffffff"
    MODE_MOTION = 1
    MODE_CLICK = 2

    def __init__(self, master):
        self.master = master
        #self.master.geometry("800x600+200+200")
        # real fullscreen w/o titlebar
        #self.master.attributes('-fullscreen', True)
        self.master.attributes('-zoomed', True)
        self.master.configure(bg=App.bg_color, cursor="hand2")

        self.master.update()
        self.width = self.master.winfo_width()
        self.height = self.master.winfo_height()

        self.master.bind("<Button-1>", self.onclick)
        self.master.bind("<Key>", self.quit)
        self.master.bind("<Enter>", self.onenter)

        self.init_images()
        self.init_sounds()

        self.label = tk.Label(self.master, bg=App.bg_color)

        self.index = None
        self.mode = None
        self.select_mode()
        self.master.mainloop()

    def select_mode(self):
        self.button_motion = tk.Button(self.master, bg=App.bg_color, text=MODE_MOTION_NAME)
        self.button_click = tk.Button(self.master, bg=App.bg_color, text=MODE_CLICK_NAME)
        self.button_motion.place(x = 300, y = 200)
        self.button_click.place(x = 300, y = 400)

    def show(self):
        self.index = random.randrange(0, len(self.images))
        self.label.configure(image = self.images[self.index])
        self.label.place(x = random.randrange(0, self.width-self.images[self.index].width()), y = random.randrange(0, self.height-self.images[self.index].height()))
        #print self.label.winfo_width(), self.label.winfo_height()

    def onclick(self, event):
        if event.widget == self.master:
            return
        elif event.widget == self.button_motion:
            self.mode = App.MODE_MOTION
            self.button_motion.destroy()
            self.button_click.destroy()
        elif event.widget == self.button_click:
            self.mode = App.MODE_CLICK
            self.button_motion.destroy()
            self.button_click.destroy()
        elif event.widget == self.label:
            call([SOUND_PLAYER, self.sounds[random.randrange(0, len(self.sounds))]], stdout=PIPE)
        self.show()

    def onenter(self, event):
        if event.widget == self.label and self.mode == App.MODE_MOTION:
            call(["gst-play-1.0", self.sounds[random.randrange(0, len(self.sounds))]], stdout=PIPE)
            self.show()

    def quit(self, event):
        self.master.destroy()

    def init_images(self):
        images = os.listdir(IMAGES_DIR)
        self.images = [ImageTk.PhotoImage(Image.open(os.path.join(IMAGES_DIR,x))) for x in images]

    def init_sounds(self):
        self.sounds = SOUNDS # TODO: make it similar to images?


### main ###

root = tk.Tk()
app = App(root)

    
