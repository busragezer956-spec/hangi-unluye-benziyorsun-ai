import streamlit as st
import face_recognition
import cv2
import pickle
import numpy as np
from PIL import Image

st.title("Hangi Türk Ünlüye Benziyorsun?")

uploaded_file = st.file_uploader(
    "Fotoğraf yükle",
    type=["jpg", "jpeg", "png"]
)

with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Yüklenen Fotoğraf")

    face_locations = face_recognition.face_locations(image_np)
    face_encodings = face_recognition.face_encodings(
        image_np,
        face_locations
    )

    if len(face_encodings) > 0:

        face_encoding = face_encodings[0]

        face_distances = face_recognition.face_distance(
            data["encodings"],
            face_encoding
        )

        best_match = np.argmin(face_distances)

        celebrity_name = data["names"][best_match]

        similarity = (1 - face_distances[best_match]) * 100

        st.success(
            f"En çok benzediğin ünlü: {celebrity_name}"
        )

        st.write(
            f"Benzerlik Oranı: %{similarity:.2f}"
        )

    else:
        st.error("Yüz bulunamadı")