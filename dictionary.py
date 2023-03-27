person1 = {"name": "Endesew", "age": 30, "weight": 55}
print(person1["age"])
for key in person1:
    print(key)
print(person1.get("height", 165))
person1["name"] = "daneil"
print(person1)

person1.pop("name")
print(person1)
person1["height"] = 165
person1["name"] = "Endesew"
print(person1)
for key in person1:
    print(key, person1[key])

syno = {"mountain": "peak", "forest": "jungle"}
print("1.", syno["mountain"])

syno["terrain"] = "land"
print("2.", syno)
syno.pop("forest")
print("3.", syno)

