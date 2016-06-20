import Classes
import requests

# 取得五十音列表
def getKana():
    # 取得首頁原始碼
    res = requests.get("http://name.m3q.jp/")
    kanaM = Classes.Kana()  # 男性五十音列表
    kanaF = Classes.Kana()  # 女性五十音列表

    # 取得男性五十音列表
    first = res.text.find("kana-list")  # 列表的開頭位置
    end = res.text.find("div", first)   # 列表的結尾位置
    first = res.text.find("kana-label", first) + 12
    while first < end:
        cutL = res.text[first:first + 1]
        first = res.text.find("kana-count", first) + 12
        last = res.text.find("<", first)
        cutC = res.text[first:last]
        if cutC != "-":
            kanaM.append(cutL, cutC)
        first = res.text.find("kana-label", first) + 12

    # 取得女性五十音列表
    first = res.text.find("kana-list") + 1
    first = res.text.find("kana-list", first)   # 列表的開頭位置
    end = res.text.find("div", first)           # 列表的結尾位置
    first = res.text.find("kana-label", first) + 12
    while first < end and first != -1 + 12:
        cutL = res.text[first:first + 1]
        first = res.text.find("kana-count", first) + 12
        last = res.text.find("<", first)
        cutC = res.text[first:last]
        if cutC != "-":
            kanaF.append(cutL, cutC)
        first = res.text.find("kana-label", first) + 12

    return kanaM, kanaF

# 印出五十音列表
def printKana(kanaM, kanaF):
    ct = 1
    print("男性的名字")
    for i in range(0, len(kanaM.label), 5):
        for j in range(i, i + 5):
            if j < len(kanaM.label):
                print(str(ct).rjust(2) + ": " + kanaM.label[j] + " (" + kanaM.count[j].rjust(4), end=")\t")
                ct += 1
        print()
    print("\n女性的名字")
    for i in range(0, len(kanaF.label), 5):
        for j in range(i, i + 5):
            if j < len(kanaF.label):
                print(str(ct).rjust(2) + ": " + kanaF.label[j] + " (" + kanaF.count[j].rjust(4), end=")\t")
                ct += 1
        print()
    print()

# 選擇五十音代碼
def chooseNum(kanaM, kanaF):
    num = input("請輸入五十音代碼: ")
    if not num.isdigit() or not int(num) >= 1 or not int(num) <= len(kanaM.label) + len(kanaF.label):
        print("輸入錯誤，請重新輸入。\n")
        chooseNum(kanaM, kanaF)
        return
    getName(int(num), kanaM, kanaF)

# 取得名字
def getName(num, kanaM, kanaF):
    # 組合網址
    url = ""
    if num <= len(kanaM.label):
        url = "http://name.m3q.jp/list?s=" + kanaM.label[num - 1] + "&g=1"
    else:
        num -= len(kanaM.label)
        url = "http://name.m3q.jp/list?s=" + kanaF.label[num - 1] + "&g=2"

    # 取得首頁原始碼
    res = requests.get(url)
    first = res.text.find("<td class=\"cel-kana\">")
    while first != -1:
        first = res.text.find("<a href", first)
        first = res.text.find(">", first) + 1
        last = res.text.find("<", first)
        cutKana = res.text[first:last]
        first = res.text.find("<a href", first)
        first = res.text.find(">", first) + 1
        last = res.text.find("<", first)
        cutKanji = res.text[first:last]
        print(cutKanji + " (" + cutKana + ")")
        first = res.text.find("<td class=\"cel-kana\">",  first)
