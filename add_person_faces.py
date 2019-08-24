import sys
import os, time
import cognitive_face as CF
from global_variables import personGroupId
import urllib
import sqlite3
import os.path



Key = '63032336225341b39b2ac1728b7864b7'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)
def get_person_id():
	person_id = ''
	extractId = str(sys.argv[1])[-3:]
    #print(extractId)
	connect = sqlite3.connect(r"D:/cam/Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " +extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	connect.close()
	return person_id

if len(sys.argv)!= 1:
    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder ="D:/cam/dataset/" + sys.argv[1]
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
        	print(filename)
        	imgurl =imageFolder+"/"+filename
        	res = CF.face.detect(imgurl)
        	if len(res) != 1:
        		print("No face detected in image")
        	else:
        		res = CF.person.add_face(imgurl, personGroupId, person_id)
        		print(res)	
        	time.sleep(6)