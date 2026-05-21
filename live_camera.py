import face_recognition
import cv2
import pickle
import numpy as np

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(
        rgb,
        face_locations
    )

    for face_encoding, face_location in zip(
        face_encodings,
        face_locations
    ):

        face_distances = face_recognition.face_distance(
            data["encodings"],
            face_encoding
        )

        best_match = np.argmin(face_distances)

        celebrity_name = data["names"][best_match]

        similarity = (1 - face_distances[best_match]) * 100

        top, right, bottom, left = face_location

        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0,255,0),
            2
        )

        text = f"{celebrity_name} %{similarity:.1f}"

        cv2.putText(
            frame,
            text,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0,255,0),
            2
        )

    cv2.imshow(
        "Hangi Turk Unluye Benziyorsun?",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()