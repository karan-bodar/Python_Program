# Local and Global Variables Example

x = 10  # Global variable

def show():
    x = 5  # Local variable
    print("Local variable:", x)

def display():
    global x  # Declare x as global to modify the global variable
    x = 15
    print("Global variable modified:", x)

show()      # Output: Local variable: 5
display()   # Output: Global variable modified: 15
print("Global variable after modification:", x)  # Output: Global variable after modification: 15