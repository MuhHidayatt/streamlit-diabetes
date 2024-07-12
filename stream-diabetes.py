import pickle
import numpy as np
import streamlit as st

# Membaca model
model = pickle.load(open('diabetes_model.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Diabetes')

# Membagi Kolom
col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Kehamilan')
with col2:
    Glucose = st.text_input('Input nilai Glukosa')
with col1:
    BloodPressure = st.text_input('Input nilai Tekanan Darah')
with col2:
    SkinThickness = st.text_input('Input nilai Skin Thickness')
with col1:
    Insulin = st.text_input('Input nilai Insulin')
with col2:
    BMI = st.text_input('Input nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes Pedigree Function')
with col2:
    Age = st.text_input('Input nilai Umur')

# Code Untuk Prediksi
diab_diagnosis = ''

# Membuat Tombol Prediksi
if st.button('Tes Prediksi Diabetes'):
    try:
        # Konversi input ke tipe numerik
        Pregnancies = float(Pregnancies)
        Glucose = float(Glucose)
        BloodPressure = float(BloodPressure)
        SkinThickness = float(SkinThickness)
        Insulin = float(Insulin)
        BMI = float(BMI)
        DiabetesPedigreeFunction = float(DiabetesPedigreeFunction)
        Age = float(Age)
        
        # Membuat array input untuk prediksi
        input_data = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        # Melakukan prediksi
        diab_prediction = model.predict(input_data)

        if diab_prediction[0] == 0:
            diab_diagnosis = 'Pasien Tidak Terkena Diabetes'
        else:
            diab_diagnosis = 'Pasien Terkena Diabetes'
        
        st.success(diab_diagnosis)
    except ValueError:
        st.error('Masukkan semua nilai dengan benar sebagai angka.')
