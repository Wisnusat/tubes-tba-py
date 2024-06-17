class DFATokenRecognizer:
    def __init__(self):
        # Mendefinisikan state penerimaan untuk setiap kelompok kata
        self.accepting_states = {
            "saya": "S", "dia": "S", "mereka": "S", "kita": "S", "kamu": "S",
            "makan": "P", "minum": "P", "bermain": "P", "membaca": "P", "menulis": "P",
            "nasi": "O", "air": "O", "bola": "O", "buku": "O", "surat": "O",
            "di-rumah": "K", "di-sekolah": "K", "di-kantor": "K", "pada-pagi-hari": "K", "dengan-cepat": "K"
        }

    def recognize(self, token):
        # Mengembalikan kelompok kata (S, P, O, K) atau None jika tidak valid
        return self.accepting_states.get(token.lower())
