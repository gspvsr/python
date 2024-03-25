import re

text = "santh prakash is studying in US"

pattern = "prakash"

search = re.search(pattern, text)

if search:
    print("search found:", search.group())
else:
    print("search not found")