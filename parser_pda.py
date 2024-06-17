from token_recognizer import DFATokenRecognizer

class PDAHTMLParser:
    def __init__(self):
        self.token_recognizer = DFATokenRecognizer()

    def parse(self, sentence):
        tokens = sentence.split()
        structure = []

        for token in tokens:
            token_type = self.token_recognizer.recognize(token)
            if not token_type:
                return f"{token} Rejected", structure

            structure.append(token_type)

        valid_structures = [
            ["S", "P", "O", "K"],
            ["S", "P", "K"],
            ["S", "P", "O"],
            ["S", "P"]
        ]

        if structure in valid_structures:
            return "Accepted", structure
        else:
            return "Rejected", structure
