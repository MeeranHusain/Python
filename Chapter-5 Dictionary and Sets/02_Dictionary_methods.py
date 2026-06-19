# Dictionary is a collection of keys-value pairs.
marks = {
    "Meeran"    : 100,
    "Pankaj"    : 90,
    "Faiz"      : 80,
    "List"      : [1,2,3],
    0           :  "Harry"
}

print("Items:- ",marks.items())    # It gives a list of key value pair and which we get are in the form of "Tuples".

print("\n")

print("Keys:- ",marks.keys())     # It give only keys in the form of "List".
print("Values:- ",marks.values())   # It give only value of a keys, in the form of "List".

marks.update({"Meeran" : 99, "Saif" : 100})   # this update the original dictionary, because dictionary is mutable.
print("Update:- ",marks)        # marks is updated and also added the Saif :100 into the dictionary.

print("Get:- ",marks.get("Pappu"))       # this check the dictionary and gives you the output if key is not present/exist then it shows "None". if exist then gives you the value.
# print(marks["Pappu"])      # this directly throw/Returns an error because it was not present into the dictionary, if exist then gives you the value.

# data = {
#     "a": 10,
#     "b": 20
# }

# print(data.get("a"))
# print(data.get("c"))
# print(data.get("c", 100)) 