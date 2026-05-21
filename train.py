import face_recognition
import os
import pickle

known_encodings = []
known_names = []

dataset_path = "dataset"

for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        image = face_recognition.load_image_file(image_path)

        face_encodings = face_recognition.face_encodings(image)

        if len(face_encodings) > 0:
            known_encodings.append(face_encodings[0])
            known_names.append(person_name)

print("Yüzler öğrenildi.")

data = {
    "encodings": known_encodings,
    "names": known_names
}

with open("encodings.pkl", "wb") as f:
    pickle.dump(data, f)

print("Model kaydedildi.")