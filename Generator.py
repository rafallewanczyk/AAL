# -*- coding: utf-8 -*-
class Generator:
    array = []
    allowed = []
    number = int()

    def __init__(self, adress, n = 0):
        self.number = n
        f = open(adress, "r")
        for x in f:
            self.array.append(x)
        f.close()
        print("wczytalem slownik")
        for i in range(65, 91): self.allowed.append(chr(i))
        for i in range(97, 123): self.allowed.append(chr(i))
        polish = "ĄąĆćĘęŁłŃńŻżŹźŚśÓó"
        for ch in polish : self.allowed.append(ch)
        # for c in self.allowed: print(f"{c} {ord(c)}")


    def generate(self):
        wholeText = ""

        inside = False
        for line in self.array:
            for ch in line:
                if ch == '<': inside = True
                if ch == '>': inside = False
                if inside == False and ch != '>' and ch != '<' :wholeText += ch

        filteredList = []
        for word in wholeText.split():
            properWord = True
            for c in word:
                if c not in self.allowed: properWord = False

            if len(word) > 2 and properWord : filteredList.append(word)
            if self.number != 0 and len(filteredList) >= self.number : break
        print(f"wygenerowalem {len(filteredList)} slow")
        return filteredList
