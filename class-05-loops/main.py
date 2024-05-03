print("start")

count = 0
while count < 10:
    count += 1
    print(count)

print("end")

musics = ["Bring Me To Life", "Time", "Clocks", "Bad Romance", "Giants"]

index_music = 0
while index_music <= len(musics) - 1:
    print(musics[index_music])
    index_music += 1


for i in range(0, 10):
    print(i)

for music in musics:
    print(music)

letters = [
    ["A", "B", "C"],
    ["A", "B", "C"]
]
for array in letters:
    for letter in array:
        print(letter)