import streamlit as st

st.title("Pengatur Suhu Ruangan Menggunakan Presensi Face Recognition")
st.image("jarjit.png")

# menu
tab1, tab2 = st.tabs(["Suhu Ruangan Sekarang:","Jumlah Presensi Mahasiswa"])

# tab1
tab1.button("Hapus Chart", type="primary")
if tab1.button("Dapatkan chart suhu"):
    tab1.image("suhu.png")
else:
    tab1.write("Chart tidak tersedia !")

# tab2
tab2.button("Reset", type="primary")
if tab2.button("Dapatkan Data"):
    tab2.write("20 Orang")
else:
    tab2.write("Klik Tombol Untuk Aksi")