import face_recognition
import os
import cv2
import numpy as np

def loadFacesAndNames(folderName):
    names=[]
    faces=[]
    
    if not os.path.exists(folderName):
        print("Folder name and path not found to train", folderName)
        return [], []

    for photos in os.listdir(folderName):
        if os.path.isfile and photos.lower().endswith(('.png', '.jpg', '.jpeg')):
            personName = os.path.splitext(photos)[0].replace("_", " ")
            fileNameWithPath = os.path.join(folderName, photos)
            image = face_recognition.load_image_file(fileNameWithPath)
            image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
            encodedImages = face_recognition.face_encodings(image)[0]

            if len(encodedImages) > 0:
                faces.append(encodedImages)
                names.append(personName)
                print("Trained and loaded the image file successfully")
            else:
                print("No Face / images Found in the specified path and file", fileNameWithPath)
    print("Result => name and encoding ", names)   
    return names, faces


def compareFacesFromPhoto(folder_name):
    names, faces = loadFacesAndNames(folder_name)

    if (not faces) or (len(faces) == 0):
        print("No images are provided for reference ( no training data )")
        return
    
    print("All training photo encoded successfully")
    photo_capture = cv2.VideoCapture(0)
    print("Starting webcam")

    while True:
        readImageFromCam, frame = photo_capture.read()
        if not readImageFromCam:
            print("Unable to read image from webcam")
            break

        modifiedFrame = cv2.resize(frame, (0,0), None, 0.25, 0.25)
        frame_color_rgb = cv2.cvtColor(modifiedFrame, cv2.COLOR_BGR2RGB)

        coordinates = face_recognition.face_locations(frame_color_rgb)

        face_Encoded = face_recognition.face_encodings(frame_color_rgb, coordinates)

        for (top, right, bottom, left), face_encoded in zip(coordinates, face_Encoded):
            match_faces = face_recognition.compare_faces(faces, face_encoded)
            label="Unknown"

            proximityVector = face_recognition.face_distance(faces, face_encoded)

            index_min = np.argmin(proximityVector)
            if match_faces[index_min]:
                label = names[index_min]
            top, left, right, bottom = top*4, left*4, right*4, bottom*4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)

            fontStyle = cv2.FONT_ITALIC
            cv2.putText(frame, label, (left + 6, bottom - 6), fontStyle, 1, (255, 255, 255), 2)
            cv2.imshow("Face Recognition", frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            print("**********Exiting Webcam**********")
            break

compareFacesFromPhoto("trained_images")    
