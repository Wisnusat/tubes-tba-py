import streamlit as st
from parser_pda import PDAHTMLParser
from token_recognizer import DFATokenRecognizer

def main():
    st.set_page_config(page_title="Validator Struktur Kalimat", page_icon="📝")

    st.title("Validasi Struktur Kalimat SPOK")
    st.write("##### Anggota Kelompok: ")
    st.write("##### - Wisnu Satrio Agung     | 1301223456")
    st.write("##### - Muhammad Alvito Naufal | 1301223342")
    st.write("##### - Bintang Rizky          | 1301223104")
    st.write("")
    st.write("")
    st.write("""
    Selamat datang di aplikasi validasi struktur kalimat SPOK!
    Aplikasi ini memeriksa apakah kalimat yang Anda masukkan sesuai dengan pola SPOK yang valid.
    Pola yang dikenali meliputi:
    - Subyek (S) – Predikat (P) – Obyek (O) – Keterangan (K)
    - Subyek (S) – Predikat (P) – Keterangan (K)
    - Subyek (S) – Predikat (P) – Obyek (O)
    - Subyek (S) – Predikat (P)
    """)

    st.write("### Kata yang Dikenali")
    recognizer = DFATokenRecognizer()
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write("##### Subyek (S):")
        st.write("\n".join([f"- {key}" for key, value in recognizer.accepting_states.items() if value == "S"]))

    with col2:
        st.write("##### Predikat (P):")
        st.write("\n".join([f"- {key}" for key, value in recognizer.accepting_states.items() if value == "P"]))

    with col3:
        st.write("##### Obyek (O):")
        st.write("\n".join([f"- {key}" for key, value in recognizer.accepting_states.items() if value == "O"]))

    with col4:
        st.write("##### Keterangan (K):")
        st.write("\n".join([f"- {key}" for key, value in recognizer.accepting_states.items() if value == "K"]))

    st.write("### Masukkan Kalimat Anda di Bawah Ini")
    sentence = st.text_area("Kalimat:", placeholder="Contoh: aku membaca buku di taman")

    if st.button("Periksa"):
        parser = PDAHTMLParser()
        result, structure = parser.parse(sentence)
        st.write(f"Hasil: {result}")
        st.write(f"Struktur Kalimat: {'-'.join(structure)}")
        sentence = ""
    
    st.write("---")
    st.write("Dibuat dengan ❤️ oleh orang jawa x lampung x makassar")

if __name__ == "__main__":
    main()
