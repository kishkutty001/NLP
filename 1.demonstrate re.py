import re
text = "The quick brown fox jumps over the lazy dog. The number is 12345."
match = re.match(r"The", text)
if match:
    print("Match found:", match.group())
else:
    print("No match found")
search = re.search(r"\d+", text)  
if search:
    print("First number found:", search.group())
words = re.findall(r"\bT\w+", text) 
print("Words starting with 'T':", words)
modified_text = re.sub(r"\d", "#", text)
print("Text after replacing digits:",modified_text)
