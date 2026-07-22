def addBannedWord(word : String, fileName : String):
    with open(f"{fileName}.csv", "a") as file:
        file.write(f";{word}")

def sortBannedWord(wordsArr, fileName):
    with open(f"{fileName}.csv", "a+") as file:
        while
