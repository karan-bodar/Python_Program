# Dictionary Functions/Methods Example

d = {'name': 'Shyam', 'age': 20, 'city': 'Jamnagar'}

print("Original Dictionary: ", d)
print("length: ", len(d))
print("Get value of 'name': ", d.get('name'))
d.update({'gender': 'Male'})
print("Updated Dictionary: ", d)
d.pop('city')
print("Dictionary after pop 'city': ", d)
d['country'] = 'India'
print("Dictionary after adding 'country': ", d)
print("Keys of Dictionary: ", d.keys())
print("Values of Dictionary: ", d.values())
print("Items of Dictionary: ", d.items())
d2 = d.copy()
print("Copied Dictionary: ", d2)
d.clear()
print("Dictionary after clear: ", d)
