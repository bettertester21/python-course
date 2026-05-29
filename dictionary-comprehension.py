numbers = [("name", "Alice"), ("age", 30), ("city", "New York" )]
print("Original list of tuples:")
print(numbers)
print("Type of numbers:", type(numbers))
print("Creating a dictionary using the dict() constructor:")
print(dict(numbers))
print("Creating a dictionary using dictionary comprehension:")
dictionary = {key: value for key, value in numbers}
print(dictionary)
print("Type of dictionary:", type(dictionary))


d = {}
print("Empty dictionary:", d)
print("Type of d:", type(d))
for key, value in numbers:
    d[key] = value
print("Dictionary after adding items using a for loop:")
print(d)
