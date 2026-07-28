# Copy File Content
with open("demo.txt","r")as f1, open("copy.txt","w") as f2:
    f2.write(f1.read())