#File Read and Write

with open("demo.txt","w") as f:
    f.write("Hello Python")
    
with open("demo.txt","r") as f:
    content = f.read()
    print("Content is:",content)