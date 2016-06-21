class Kana:
    def __init__(self):
        self.label = list()  # 五十音
        self.count = list()  # 對應的名字數

    def append(self, label, count):
        self.label.append(label)
        self.count.append(count)

class Name:
    def __init__(self):
        self.kana = list()
        self.kanji = list()

    def append(self, kana, kanji):
        self.kana.append(kana)
        self.kanji.append(kanji)
