# lakukan import array dulu
import array as arr
myArr = arr.array('i', [1,2,3])
print(myArr)
print(type(myArr))
print()
myCharArr = arr.array('u', ['a', 'b', 'c'])
print(myCharArr)
print(type(myCharArr))

# List mutable, data bisa diubah. heavy
print('\nList:')
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
print(myFruitList[-1])
print(myFruitList[-2])

myFruitList[0] = "orange"
myFruitList[1] = "kiwi"
myFruitList[2] = "strawberry"
print(myFruitList)
print(myFruitList[0])

# List 2D (Print List didalam List)
group = [
    [ "siraz", "tri", "denira"], 
    ["Jdoe", "Mmajor","Ljuan"]
]
print (group[0][0])
print (group[0][1])

print (group[1][2])
print (group[1][0])

# myFruitList[2] = "orange"
# print(myFruitList)


# Tuple
print('\nTuple:')
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

# Tuple, data tidak bisa diubah (immutable), Hasil akan Error. small. 
# biasanya dipakai di Mc. Learning, karena ringan.
# myFinalAnswerTuple[0] = "orange"

# Dictionary
print('\nDictionary:')
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

# SET = akan remove yang duplikat.
print("\nSet:")
mySet = {1,2,3,4}
print(mySet)

mySet = {1,2,3,3}
print(mySet)

