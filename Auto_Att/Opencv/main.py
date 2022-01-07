# import cv2
# import numpy as np
# import face_recognition
#
# imgElon = face_recognition.load_image_file('ImageBasic/VV.jpg')
# imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)#Converts image to RGB
# imgTest = face_recognition.load_image_file('ImageBasic/Elon_Test.jpg')
# imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
#
# faceLoc = face_recognition.face_locations(imgElon)[0]# will locate Face in the image and as only one image is passed then [0] is written
# encodeElon = face_recognition.face_encodings(imgElon)[0]#returns 4 coordinates inside which face is reco
# cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
#
# results = face_recognition.compare_faces([encodeElon],encodeTest)#tells true or false
# faceDis = face_recognition.face_distance([encodeElon],encodeTest)#lower the distance better the match is
# print(results,faceDis)
# cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(100,500),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
#
# cv2.imshow('Elon Musk',imgElon)
# cv2.imshow('Elon Test',imgTest)
# cv2.waitKey(0)