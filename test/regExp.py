
import re


str = "hi Mariya, how are you?"
pattern = "mariya"

if re.search(pattern.lower(), str.lower(), ):
    print pattern + " exists in " + str
else:
    print pattern, " doesn't exist in ", str
