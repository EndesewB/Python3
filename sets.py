animals = {"dog", "cat", "elephant"}
print(animals)
wild_animals = {"tiger", "leopard"}
animals.update(wild_animals, {"dolphin"})
print(animals)
animals.discard("cat")
print(animals)
# animals.clear()
print(animals)

for animal in animals:
    print(animal)

domestic ={"cat", "dog", "rat"}
wild = {"lion", "rat", "leopard"}
animal = domestic | wild  #/ domestic.union(wild)
print(animal)
animalss = domestic.intersection(wild) #/ domestic & wild
print(animalss)
