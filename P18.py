# Python programs to print patterns

for i in range(1,6):
    print(str(i) * i)
    
print("\n")
    
for i in range(1, 6):
 for j in range(65, 65+i):
  print(chr(j), end=" ")
 print()

print("\n")


for i in range(5, 0, -1):
 print("*" * i)