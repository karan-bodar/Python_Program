# Set Functions/Methods Example

s = {10,20,30}
print("Original Set: ", s)
s.add(40)
print("after adding: ", s)
s.update([50,60])
print("after updating: ", s)
s2 = s.copy()
print("Copied Set: ", s2)
s.pop()
print("after pop: ", s)
s.discard(20)
print("after discard: ", s)
s.remove(30)
print("after remove: ", s)
s.clear()
print("after clear: ", s)

# Set operations

a = {1,2,3}
b = {3,4,5}

print("Set A: ", a)
print("Set B: ", b)

print("Union: ", a.union(b))
print("Intersection: ", a.intersection(b))
print("Difference: ", a.difference(b))