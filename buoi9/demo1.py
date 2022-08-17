import re

pattern = "0[0-9]{9,10}"
s = input("Enter your pass")

print(s)
if re.match(pattern, s):
    print("Correct")
else:
    print("Incorrect")
