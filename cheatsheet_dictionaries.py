# DECLARING A DICTIONARY
dictionary01 = {"key01":"value01", 2:"value02", 3:"value03"}
print(dictionary01)
dictionary02 = {"k01":"v01", "k02":"v02", "k03":"v03", "k04":"v04"}

# RETRIEVING DICTIONARY VALUES WITH THE KEYS
print(dictionary02["k02"])

value01 = dictionary02.get("k01",False)
print(value01)
value02 = dictionary02.get("k0",False)
print(value02)

# ADDING KEYS AND VALUES TO THE DICTIONARY
dictionary02["k05"] = "v05"
print(dictionary02)

# EXPAND DICTIONARY WITH CONTENTS OF ANOTHER DICTIONARY
dictionary03 = {"k11":"v11", "k12":"v12", "k13":"v13", "k14":"v14"}
print(dictionary03)
dictionary03.update(dictionary01)
print(dictionary03)

# GET ALL DICTIONARY KEYS
keys = dictionary03.keys()
print(keys)

# GET ALL DICTIONARY VALUES
values = dictionary03.values()
print(values)

# GET ALL DICITIONARY ITEMS
items = dictionary03.items()
print(items)

# IN AND NOT IN TO FIND IF ELEMENTS EXIST IN A DICTIONARY
isItThere = "k11" in dictionary03
print(isItThere)
isItNotThere = "k31" not in dictionary03
print(isItNotThere)

# SORT A DICTIONARY
dictionary04 = {1:"d", 2:"f", 3:"a", 4:"c", 5:"b", 6:"e"}
print(dictionary04)
sort = sorted(dictionary04.items(), key = lambda x: x[1])
print(sort)

# REMOVING ELEMENTS FROM A DICTIONARY
print(dictionary01)
del dictionary01["key01"]
print(dictionary01)

dictionary01.pop(2)
print(dictionary01)
