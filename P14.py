# Count Characters, Words, Lines

with open("test.txt","r") as f:
    text = f.read()
char = len(text)
word = len(text.split())
line = len(text.splitlines())
print("Characters:",char)
print("Words:",word)
print("Lines:",line)
    