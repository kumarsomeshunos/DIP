import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        root.title("EdiImg")
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLabel_155=tk.Label(root)
        self.GLabel_155["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_155["font"] = ft
        self.GLabel_155["fg"] = "#333333"
        self.GLabel_155["justify"] = "center"
        self.GLabel_155["text"] = ""
        self.GLabel_155.place(x=20,y=20,width=300,height=400)

        GButton_655=tk.Button(root)
        GButton_655["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_655["font"] = ft
        GButton_655["fg"] = "#000000"
        GButton_655["justify"] = "center"
        GButton_655["text"] = "Black & White"
        GButton_655.place(x=350,y=90,width=100,height=30)
        GButton_655["command"] = self.GButton_655_command

        GButton_168=tk.Button(root)
        GButton_168["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_168["font"] = ft
        GButton_168["fg"] = "#000000"
        GButton_168["justify"] = "center"
        GButton_168["text"] = "Color Negative"
        GButton_168.place(x=350,y=40,width=100,height=30)
        GButton_168["command"] = self.GButton_168_command

        GButton_864=tk.Button(root)
        GButton_864["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_864["font"] = ft
        GButton_864["fg"] = "#000000"
        GButton_864["justify"] = "center"
        GButton_864["text"] = "Gray Negative"
        GButton_864.place(x=470,y=40,width=100,height=30)
        GButton_864["command"] = self.GButton_864_command

        GButton_115=tk.Button(root)
        GButton_115["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_115["font"] = ft
        GButton_115["fg"] = "#000000"
        GButton_115["justify"] = "center"
        GButton_115["text"] = "Blur"
        GButton_115.place(x=350,y=140,width=100,height=30)
        GButton_115["command"] = self.GButton_115_command

        GButton_514=tk.Button(root)
        GButton_514["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_514["font"] = ft
        GButton_514["fg"] = "#000000"
        GButton_514["justify"] = "center"
        GButton_514["text"] = "Upload Image"
        GButton_514.place(x=20, y=440, width=140, height=30)
        GButton_514["command"] = self.GButton_514_command

        self.thumbnail = None  # Retain the PhotoImage object

        GButton_498=tk.Button(root)
        GButton_498["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_498["font"] = ft
        GButton_498["fg"] = "#000000"
        GButton_498["justify"] = "center"
        GButton_498["text"] = "Clear Image"
        GButton_498.place(x=180,y=440,width=140,height=30)
        GButton_498["command"] = self.GButton_498_command

        GButton_349=tk.Button(root)
        GButton_349["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_349["font"] = ft
        GButton_349["fg"] = "#000000"
        GButton_349["justify"] = "center"
        GButton_349["text"] = "Red Tint"
        GButton_349.place(x=350,y=190,width=70,height=30)
        GButton_349["command"] = self.GButton_349_command

        GButton_129=tk.Button(root)
        GButton_129["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_129["font"] = ft
        GButton_129["fg"] = "#000000"
        GButton_129["justify"] = "center"
        GButton_129["text"] = "Green Tint"
        GButton_129.place(x=425,y=190,width=70,height=30)
        GButton_129["command"] = self.GButton_129_command

        GButton_950=tk.Button(root)
        GButton_950["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_950["font"] = ft
        GButton_950["fg"] = "#000000"
        GButton_950["justify"] = "center"
        GButton_950["text"] = "Blue Tint"
        GButton_950.place(x=500,y=190,width=70,height=30)
        GButton_950["command"] = self.GButton_950_command

        GButton_775=tk.Button(root)
        GButton_775["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_775["font"] = ft
        GButton_775["fg"] = "#000000"
        GButton_775["justify"] = "center"
        GButton_775["text"] = "Grain"
        GButton_775.place(x=470,y=140,width=100,height=30)
        GButton_775["command"] = self.GButton_775_command

        GButton_341=tk.Button(root)
        GButton_341["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_341["font"] = ft
        GButton_341["fg"] = "#000000"
        GButton_341["justify"] = "center"
        GButton_341["text"] = "Binary"
        GButton_341.place(x=470,y=90,width=100,height=30)
        GButton_341["command"] = self.GButton_341_command

        GButton_381=tk.Button(root)
        GButton_381["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_381["font"] = ft
        GButton_381["fg"] = "#000000"
        GButton_381["justify"] = "center"
        GButton_381["text"] = "Rotate 90"
        GButton_381.place(x=350,y=240,width=100,height=30)
        GButton_381["command"] = self.GButton_381_command

        GButton_443=tk.Button(root)
        GButton_443["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_443["font"] = ft
        GButton_443["fg"] = "#000000"
        GButton_443["justify"] = "center"
        GButton_443["text"] = "Rotate 180"
        GButton_443.place(x=470,y=240,width=100,height=30)
        GButton_443["command"] = self.GButton_443_command

        GButton_335=tk.Button(root)
        GButton_335["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_335["font"] = ft
        GButton_335["fg"] = "#000000"
        GButton_335["justify"] = "center"
        GButton_335["text"] = "Rotate 270"
        GButton_335.place(x=350,y=280,width=100,height=30)
        GButton_335["command"] = self.GButton_335_command

        GButton_892=tk.Button(root)
        GButton_892["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_892["font"] = ft
        GButton_892["fg"] = "#000000"
        GButton_892["justify"] = "center"
        GButton_892["text"] = "Rotate 360"
        GButton_892.place(x=470,y=280,width=100,height=30)
        GButton_892["command"] = self.GButton_892_command

        GButton_552=tk.Button(root)
        GButton_552["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_552["font"] = ft
        GButton_552["fg"] = "#000000"
        GButton_552["justify"] = "center"
        GButton_552["text"] = "Render"
        GButton_552.place(x=360,y=440,width=200,height=30)
        GButton_552["command"] = self.GButton_552_command

        GLabel_505=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_505["font"] = ft
        GLabel_505["fg"] = "#000000"
        GLabel_505["justify"] = "center"
        GLabel_505["text"] = "EdiImg"
        GLabel_505.place(x=360,y=360,width=200,height=30)

        GButton_536=tk.Button(root)
        GButton_536["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_536["font"] = ft
        GButton_536["fg"] = "#000000"
        GButton_536["justify"] = "center"
        GButton_536["text"] = "X"
        GButton_536.place(x=570,y=0,width=20,height=25)
        GButton_536["command"] = lambda: self.GButton_536_command(root)

    def GButton_655_command(self):
        grayImage = cv2.imread("copied_image.png", 0)
        cv2.imwrite("copied_image.png", grayImage)


    def GButton_168_command(self):
        RGBImage = cv2.imread("copied_image.png")
        RGBNegative = 255 - RGBImage
        cv2.imwrite("copied_image.png", RGBNegative)


    def GButton_864_command(self):
        grayImage = cv2.imread("copied_image.png", 0)
        grayNegative = 255 - grayImage
        cv2.imwrite("copied_image.png", grayNegative)


    def GButton_115_command(self):
        image = cv2.imread('copied_image.png')
        kernel_size = (5, 5)
        blurred_image = cv2.GaussianBlur(image, kernel_size, 0)
        cv2.imwrite('copied_image.png', blurred_image)


    def GButton_514_command(self):
        file_path = filedialog.askopenfilename(title="Select Image")
        original_image = Image.open(file_path)
        save_path = "/Users/somesh/Documents/Sem V/DIP/Project/DIP/EdiImg/copied_image.png"
        original_image.save(save_path)
        new_width = 300
        new_height = 400
        thumbnail = original_image.resize((new_width, new_height), Image.BICUBIC)
        self.thumbnail = ImageTk.PhotoImage(thumbnail)
        self.GLabel_155.configure(image=self.thumbnail)
        self.GLabel_155.image = self.thumbnail


    def GButton_498_command(self):
        print("command")


    def GButton_349_command(self):
        image = cv2.imread('copied_image.png')
        b, g, r = cv2.split(image)
        red_tinted_image = np.zeros_like(image)
        red_tinted_image[:, :, 2] = r
        cv2.imwrite('copied_image.png', red_tinted_image)


    def GButton_129_command(self):
        image = cv2.imread('copied_image.png')
        b, g, r = cv2.split(image)
        green_tinted_image = np.zeros_like(image)
        green_tinted_image[:, :, 1] = g
        cv2.imwrite('copied_image.png', green_tinted_image)


    def GButton_950_command(self):
        image = cv2.imread('copied_image.png')
        b, g, r = cv2.split(image)
        blue_tinted_image = np.zeros_like(image)
        blue_tinted_image[:, :, 0] = b
        cv2.imwrite('copied_image.png', blue_tinted_image)


    def GButton_775_command(self):
        image = cv2.imread('copied_image.png')
        rows, cols, channels = image.shape
        mean = 0
        std_dev = 25
        noise = np.random.normal(mean, std_dev, (rows, cols, channels))
        noisy_image = np.clip(image + noise, 0, 255).astype(np.uint8)
        cv2.imwrite('copied_image.png', noisy_image)


    def GButton_341_command(self):
        image = cv2.imread('copied_image.png', cv2.IMREAD_GRAYSCALE)
        _, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
        cv2.imwrite('copied_image.png', binary_image)


    def GButton_381_command(self):
        image = cv2.imread('copied_image.png')
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite('copied_image.png', rotated_image)


    def GButton_443_command(self):
        image = cv2.imread('copied_image.png')
        rotated_image_180 = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imwrite('copied_image.png', rotated_image_180)


    def GButton_335_command(self):
        image = cv2.imread('copied_image.png')
        rotated_image_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite('copied_image.png', rotated_image_270)


    def GButton_892_command(self):
        image = cv2.imread('copied_image.png')
        rotated_image_360 = cv2.rotate(image, cv2.ROTATE_180)
        cv2.imwrite('copied_image.png', rotated_image_360)


    def GButton_552_command(self):
        original_image = Image.open("copied_image.png")
        new_width = 300
        new_height = 400
        thumbnail = original_image.resize((new_width, new_height), Image.BICUBIC)
        thumbnail = ImageTk.PhotoImage(thumbnail)
        self.GLabel_155.configure(image=thumbnail)
        self.GLabel_155.image = thumbnail

    def GButton_536_command(self, root):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
