# Primitive Types

# milk = "Leite"
# volume = 2.5

# print(type(milk))
# print(type(volume))

# preparation1 = volume + 1
# preparation2 = milk + str(volume)

# print(preparation1)
# print(preparation2)

# life_cat = str(volume + 5)

# print("O gato bebe " + milk )
# print("e tem " + life_cat + " vidas")

# print("O gato bebe " + milk + " e tem " + life_cat + " vidas")
# print(f"O gato bebe {milk} e tem {life_cat} vidas")

name = "Eric"
age = 19
is_admin = True #boolean True or False

print(is_admin)
print(type(is_admin))

# Structural Types (Collections)

animes = ["Saint Seiya", "Dragon Ball", "Pokemon", "Nanatsu no Taizai", "Spy X Family"]
            # =>  0             1           2               3                 4
            # <= -5            -4          -3              -2                -1

print(animes)
print(type(animes))

print(animes[3])
print(animes[0])
print(animes[-1])

list = ["A", 123, True, ["B", "C"]]

print(list[0])
print(list[3])
print(list[-1])
print(list[-1][1])

list[2] = False
list[-1][0] = "D"
print(list)
print(len(list)) #length

# tuple
tuple = ("A", 123, True)
print(type(tuple))
print(tuple[1])

# tuple[1] = 456 # error: tuple is immutable

print(tuple)

# dict

dict = {
    "name": "Eric",
    "age": "19",
    "is_admin": True
}
print(dict)
print(type(dict))

print(dict["name"])
print(dict["age"])
print(dict["is_admin"])