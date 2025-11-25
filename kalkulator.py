import streamlit as st

st.title("Kalkulator")

# Input angka
num1 = st.number_input("Masukkan angka pertama:", value=0.0)
num2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilih operasi
operasi = st.selectbox(
    "Pilih operasi:",
    ("Tambah (+)", "Kurang (-)", "Kali (*)", "Bagi (/)")
)

# Tombol hitung
if st.button("Hitung"):
    if operasi == "Tambah (+)":
        hasil = num1 + num2
    elif operasi == "Kurang (-)":
        hasil = num1 - num2
    elif operasi == "Kali (*)":
        hasil = num1 * num2
    elif operasi == "Bagi (/)":
        if num2 == 0:
            hasil = "Error: Tidak bisa membagi dengan 0!"
        else:
            hasil = num1 / num2
    
    st.success(f"Hasil: {hasil}")