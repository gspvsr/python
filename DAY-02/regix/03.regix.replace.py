import re

text = "Santh is studying in USA, he will get job aftr completion of masters"

pattern = "job"

replacement = "DevOps Job"

new_text = re.sub(pattern, replacement, text)

print("modified text:", new_text)

