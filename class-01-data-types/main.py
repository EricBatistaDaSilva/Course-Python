milk = "Leite"
volume = 2.5

print(type(milk))
print(type(volume))

preparation1 = volume + 1
preparation2 = milk + str(volume)

print(preparation1)
print(preparation2)

life_cat = str(volume + 5)

print("O gato bebe " + milk )
print("e tem " + life_cat + " vidas")

print("O gato bebe " + milk + " e tem " + life_cat + " vidas")
print(f"O gato bebe {milk} e tem {life_cat} vidas")