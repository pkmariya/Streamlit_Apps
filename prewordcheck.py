
def pre_word(word):
    if word.startswith('pre'):
        if word.isalpha():
            print(word, " starts with \"pre\"!")
    else:
        print("* enter a word that starts with \"pre\"* ")


text = input("Enter a word")
pre_word(text)