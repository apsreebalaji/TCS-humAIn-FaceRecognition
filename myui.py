import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk
import os
import sys
import shutil
import cognitive_face as CF
from global_variables import personGroupId 
Key = 'adc934ffada34e53944934fb87cd9442'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
window = tk.Tk()

window.title("Face_Recogniser")
canvas = Canvas(width = 250, height = 250, bg = 'white')
canvas.pack(expand = 'YES', fill = 'both')
image = ImageTk.PhotoImage(file = "D:/cam/tws1.png")
canvas.create_image(600, 10, image = image, anchor = 'nw')

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'

window.configure(background='blue')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="Automated Attendance System using Surveillance Camera " ,bg="white"  ,fg="black"  ,width=50  ,height=1,font=('Copperplate Gothic Bold', 20 , ' bold ')) 
message.place(x=220, y=190)
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
def demo():
    folderPath = 'D:/cam/testimages/'
    croppedFol = 'D:/cam/Cropped_faces'
    for image in os.listdir(folderPath):
        if os.path.exists(croppedFol):
            shutil.rmtree(croppedFol)
            os.makedirs(croppedFol)
            os.system("python D:/cam/detect.py " + os.path.join(folderPath, image))
            os.system("python D:/cam/spreadsheet.py")
            os.system("python D:/cam/identify.py")
def viewattendance():
    os.system("D:/cam/reports.xlsx")

liveVideo = tk.Button(window, text="Live Video",fg="black"  ,bg="#00CED1"  ,width=20  ,height=2, activebackground = "#DC143C" ,font=('Comic Sans MS', 15, ' bold '))
liveVideo.place(x=600, y=280)

trackImg = tk.Button(window, text="Update Attendance",command=demo ,fg="black"  ,bg="#00CED1"  ,width=20  ,height=2, activebackground = "#DC143C" ,font=('Comic Sans MS', 15, ' bold '))
trackImg.place(x=400, y=410)
viewatt=tk.Button(window, text="View Attendance",command=viewattendance,fg="black"  ,bg="#00CED1"  ,width=20  ,height=2, activebackground = "#DC143C" ,font=('Comic Sans MS', 15, ' bold '))
viewatt.place(x=830, y=410)
quitWindow = tk.Button(window, text="Quit",command=window.destroy  ,fg="black" ,bg="#DC143C"  ,width=20  ,height=2, activebackground = "Red" ,font=('Comic Sans MS', 15, ' bold '))
quitWindow.place(x=615, y=530)

window.mainloop()
