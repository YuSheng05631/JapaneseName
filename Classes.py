class Kana:
    def __init__(self):
        self.label = list()  # 五十音
        self.count = list()  # 對應的名字數

    def append(self, label, count):
        self.label.append(label)
        self.count.append(count)
