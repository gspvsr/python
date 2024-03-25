import re

text = "banana, apple, orange"

pattern = ","

split = re.split(pattern, text)

print("splitted:", split)