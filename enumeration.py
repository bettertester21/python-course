animals = ["dog", "cat", "rabbit", "hamster"]
print(animals)
animals[0] = "fox"
print(animals)
for animal in animals:
    print(animal)

print("Implement enuretation")
for index, animal in enumerate(animals):
    print(f"{index}: {animal}")

    