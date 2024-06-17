import streamlit as st
from parser_pda import PDAHTMLParser
from token_recognizer import DFATokenRecognizer

def main():
    st.title("Kalimat SPOK Validator")
    st.write("##### Anggota Kelompok: ")
    st.write("##### - Wisnu Satrio Agung     | 1301223456")
    st.write("##### - Muhammad Alvito Naufal | 1301223342")
    st.write("##### - Bintang Rizky          | 1301223104")
    st.write("")
    st.write("")

    st.write("""
    Masukkan kalimat berbahasa Indonesia untuk memeriksa kevalidan struktur SPOK-nya.
    Struktur yang dikenali adalah:
    - S – P – O – K
    - S – P – K
    - S – P – O
    - S – P
    """)

    # Tampilkan daftar kalimat yang dikenali oleh token recognizer
    st.write("### Daftar Kata yang Dikenali:")
    recognizer = DFATokenRecognizer()
    st.write("#### Subyek (S):")
    st.write(", ".join([key for key, value in recognizer.accepting_states.items() if value == "S"]))
    st.write("#### Predikat (P):")
    st.write(", ".join([key for key, value in recognizer.accepting_states.items() if value == "P"]))
    st.write("#### Obyek (O):")
    st.write(", ".join([key for key, value in recognizer.accepting_states.items() if value == "O"]))
    st.write("#### Keterangan (K):")
    st.write(", ".join([key for key, value in recognizer.accepting_states.items() if value == "K"]))

    sentence = st.text_area("Masukkan kalimat:")

    if st.button("Periksa"):
        parser = PDAHTMLParser()
        result, structure = parser.parse(sentence)
        st.write(f"Hasil: {result}")
        st.write(f"Struktur Kalimat: {'-'.join(structure)}")
        sentence = ""

if __name__ == "__main__":
    main()
