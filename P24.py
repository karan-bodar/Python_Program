# Return Multiple Values from Function

def studentDetails():
    name = "Shyam"
    age = 20
    city = "Jamnagar"
    return name,age,city

n,a,c = studentDetails()
print("Name: ", n)
print("Age: ", a)
print("City: ", c)