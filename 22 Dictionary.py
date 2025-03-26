# this file is for learning and practising dictionary/
# dictionary = a collection of Key: value pairs

captitals ={ "India": "Delhi",
            "USA": "Washington D C",
            "China": "Beijing"}

print(captitals)
print(captitals.get("India"))

if captitals.get("India"):
    print("The capital Exists")
else:
    print("The capital doesnt exist")

captitals.update({"Germany":"Berlin"})
captitals.pop("China")
captitals.popitem()

keys = captitals.keys

for key in captitals.keys():
    print(key)

values = captitals.values()
print(values)

for values in captitals.values():
    print(values)

items = captitals.items()

for item in captitals.items():
    print(item)

# Now the key value pairs
for key, values in captitals.items():
    print(f"{key} : {values}")
captitals.clear()