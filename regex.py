import re
txt="aswin  manoj"
x=re.search("^aswin.*manoj$",txt)
if x:
    print("Found")
else:
    print("Not Found")