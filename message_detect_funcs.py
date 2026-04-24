contents = "\0"
word = "\0"

# might be enclosed to the new banned words instead

#with open("banned_words.csv", "r") as file:
 #   contents = file.split(";")
  #  for i in range(len(contents)):
   #     if word in contents:
    #        print("That word is not allowed! Do not say that in this discord server!\n")


# def detect(msg): # function prototype

def new_banned_words(contents, file_name):
    word = input("Input new banned word: ")

    with open(f"{file_name}", "+a") as file:
        while (word != "END"):
            file.write("word")
            contents.add(word)
            print("Banned word added to file.")
            word = input("Input new banned word: ")

    