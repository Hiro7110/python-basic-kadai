# kadai
# listで週間天気を記載
list = ["月曜日は晴れです","火曜日は雨です","水曜日は晴れです","木曜日は晴れです","金曜日は曇りです","土曜日は曇りのち雨です","日曜日は雷雨です"]
print(list)

# listから水曜日の値のみを取り出す
print(list[2])

# dictonaryで週間天気を記載
dictonary = {
    "mon" : "晴れ",
    "tue" : "雨",
    "wed" : "晴れ",
    "thu" : "晴れ",
    "fri" : "曇り",
    "sat" : "曇りのち雨",
    "sun" : "雷雨"
    }
print(dictonary)

# dictonaryから水曜日の値のみを取り出す
print(dictonary["wed"])
