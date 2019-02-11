#list

fruitbasket = ["banana","apple","mango"]
print("1. printing entire fruit basket: ")
print(fruitbasket)

print("2. Accessing second element in the list:")
print(fruitbasket[2]) 

print("3. Appending an element to the list : ")
fruitbasket.append("orange")

print(fruitbasket)

print("4. Changing the value in the list : ")
fruitbasket[2] = "avacado"
print(fruitbasket)

print("5.Check for duplicates in the list :")
fruitbasket.append("banana")
print(fruitbasket)

print("6.Looping through the list using for : ")
for fruit in fruitbasket :
 print(fruit)

print("7.checking if an item exist in the list:")
if "banana" in fruitbasket :
 print("Yes, banana is in the fruit basket! ")

print("8.Determine the length of the list :")
print(len(fruitbasket))

print("9.Add an element at specified index :")
fruitbasket.insert(3,"pineapple")
print(fruitbasket)

print("10.Remove an item using remove():")
fruitbasket.remove("avacado")
print(fruitbasket)

print("11.Remove an item using pop() :")
fruitbasket.pop(0)
print(fruitbasket)

print("12.Remove an item using del() :")
del fruitbasket[0]
if "apple" in fruitbasket :

 print(fruitbasket)

print("13. Clear the list : ")
fruitbasket.clear()
print(fruitbasket)


 
