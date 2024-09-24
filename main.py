meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "GHOSt": "Yok olmak",
            "CAP": "Yalan olarak düşünülen şeyler",
            "FAKE": "Sahte"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("kelime sözlükte yok")
