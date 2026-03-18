class TextSecurity:
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, text):
        result = ""

        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) - 65 + self.shift) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) - 97 + self.shift) % 26 + 97)
            else:
                result += ch  # keep numbers and symbols unchanged

        return result

    def decrypt(self, text):
        result = ""

        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) - 65 - self.shift) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) - 97 - self.shift) % 26 + 97)
            else:
                result += ch

        return result