import streamlit as st
import face_recognition
import pickle
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Hangi Ünlüye Benziyorsun?",
    page_icon="🎬",
    layout="centered"
)

st.markdown(
    """
    <h1 style='text-align:center;color:#ff4b4b;'>
    Hangi Türk Ünlüye Benziyorsun?
    </h1>
    """,
    unsafe_allow_html=True
)

st.write("Fotoğraf yükle veya kamerayı kullan 🎉")

# DATASET
with open("encodings.pkl", "rb") as f:
    data = pickle.load(f)

# FOTOĞRAF YÜKLEME
uploaded_file = st.file_uploader(
    "Fotoğraf Seç",
    type=["jpg", "jpeg", "png"]
)

# FOTOĞRAF ANALİZ
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    image_np = np.array(image)

    st.image(
        image,
        caption="Yüklenen Fotoğraf",
        width=300
    )

    with st.spinner("AI analiz yapıyor..."):

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

            st.progress(min(int(similarity), 100))

            st.write(
                f"Benzerlik Oranı: %{similarity:.2f}"
            )

        else:
            st.error("Yüz bulunamadı")

# KAMERA
show_camera = st.toggle("📷 Kamerayı Aç")

camera_image = None

if show_camera:

    camera_image = st.camera_input("Fotoğraf Çek")

# KAMERA ANALİZ
if camera_image is not None:

    image = Image.open(camera_image)

    image_np = np.array(image)

    st.image(
        image,
        caption="Kamera Görüntüsü",
        width=300
    )

    with st.spinner("AI analiz yapıyor..."):

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

            st.progress(min(int(similarity), 100))

            st.write(
                f"Benzerlik Oranı: %{similarity:.2f}"
            )

        else:
            st.error("Yüz bulunamadı")