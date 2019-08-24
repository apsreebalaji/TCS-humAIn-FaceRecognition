import os,shutil


folderPath = 'D:/cam/testimages/'
croppedFol = 'D:/cam/Cropped_faces'
for image in os.listdir(folderPath):
    if os.path.exists(croppedFol):
        shutil.rmtree(croppedFol)
        os.makedirs(croppedFol)
        os.system("python D:/cam/spreadsheet.py")
        os.system("python D:/cam/detect.py " + os.path.join(folderPath, image))
        os.system("python D:/cam/spreadsheet.py")
        os.system("python D:/cam/identify.py")
