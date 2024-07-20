
def quote_me(text):
    if text.startswith("\""):
        print(text, " starts with \" double quotes")
        print("\'", text, "\'")
        print("\n")
    elif text.startswith("\'"):
        print(text, " starts with \' single quote")
        print("\"", text, "\"")
        print("\n")
    else:
        print(text, " doesn't start with any quote")
        print("\n")

quote_me("noQuoteString")
quote_me("'singleQuoteString'")
quote_me("\"doubleQuoteString\"")
