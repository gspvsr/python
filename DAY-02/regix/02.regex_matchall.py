import re

text = "Santh prakash is studying in USA"
pattern = "Santh"
match = re.match(pattern, text) # Note. re.match() only will starting of string, if any thing middle of string, it should be re.search.
if match:
    print ("match found:", match.group())
else:
    print("No match")
